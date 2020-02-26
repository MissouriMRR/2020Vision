import pygame
import time

from sampler import Sampler
from predictor import Predictor
from accuracy_tracker import AccuracyTracker


class TextColorChooser:
    """
    Assembly of smaller programs to make a bot predict what background
    would work best for a specific color

    Parameters
    ----------
    density: int, default=16
        How far of a gap between rgb values.

    map_size: tuple(int), default=(0,256)
        Either a size 2 tuple of min and max for all colors or a size 6 tuple of
        min and max for each of red, green and blue.

    use_file: bool, default=False
        Whether to pull data from file or make user input. True is to use file.
    """

    screen_size = (400, 400)

    window_timeout = 30

    def __init__(self, density=None, map_size=None):
        self.input_data = []

        self.density = density if density else 16

        map_size = map_size if map_size else (0, 255)

        assert len(map_size) == 2 or len(map_size) == 6, \
            "map_size tuple must be of size 2 or 6!"
        self.map_size = map_size * (6 // len(map_size))

        self.window()

    @property
    def data(self):
        """
        Returns complete set of data w/ predictions and user inputs.

        Returns
        -------
        list of pairs
            (color(int, int, int), value(string)) value starts with 'x'
            if user input then color value else just color value
        """
        return self.complete_data()

    @property
    def color_generator(self):
        """
        Returns generator that goes through every color

        Returns
        -------
        generator
            Goes through every r, g, b value in range with steps size of the density
        """

        return ((r, g, b)
                for r in range(self.map_size[0], self.map_size[1], self.density)
                for g in range(self.map_size[2], self.map_size[3], self.density)
                for b in range(self.map_size[4], self.map_size[5], self.density))

    def complete_data(self):
        """
        Generate prediction for all possible colors

        Returns
        -------
        list of pairs
            (color(int, int, int), value(string)) value starts with 'x'
            if user input then color value else just color value
        """

        print("Generating data...")

        predictor = Predictor(self.input_data)

        # Generate predictions at every point
        complete_data = [(color, predictor.predict(color)) for color in self.color_generator]

        # Overlay user input values
        for color, value in self.input_data:
            complete_data.append((color, 'x' + value))

        return complete_data

    def show_buttons(self, screen, color):
        """
        Shows buttons for each choice

        Parameters
        ----------
        screen: Pygame display
            Display for everything to be blitted on.

        color: (int, int, int)
            RGB color value for color being tested.

        Returns
        -------
        (color(int, int, int), value('w' or 'b'))

        Raises
        ------
        ValueError if the X button is pressed

        RuntimeError if window closes by timeout
        """

        # Generate GUI

        quartile_len_w = TextColorChooser.screen_size[0] / 4
        quartile_len_h = TextColorChooser.screen_size[1] / 2 - 25

        buttons = {
            'w': pygame.Rect(quartile_len_w - 50, quartile_len_h, 100, 50),
            'b': pygame.Rect(3 * quartile_len_w - 50, quartile_len_h, 100, 50)
        }

        for button in buttons.values():
            pygame.draw.rect(screen, color, button)

        font = pygame.font.SysFont("Arial", 30)
        white_text = font.render("White", True, ([255, 255, 255]))
        black_text = font.render("Black", True, ([0, 0, 0]))

        screen.blit(white_text, (quartile_len_w - 50 + 18, quartile_len_h + 5))
        screen.blit(black_text, (3 * quartile_len_w - 50 + 20, quartile_len_h + 5))

        pygame.display.update()  # Update screen

        # Get user input

        start_time = time.time()

        while time.time() - start_time < TextColorChooser.window_timeout:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    raise ValueError("Quit window")

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos  # get mouse pos

                    # Check if mouse position is over a button
                    for value, button in buttons.items():
                        if button.collidepoint(mouse_pos):
                            return [color, value]

        raise RuntimeError("Timeout!")

    def window(self):
        """
        Window for user to interact with
        """

        pygame.init()
        screen = pygame.display.set_mode(TextColorChooser.screen_size)
        pygame.display.set_caption('Input data')

        sampler = Sampler(self.map_size)

        # Generate first 10 values

        try:
            self.input_data = [self.show_buttons(screen, (sampler.sample(enable_iterator=False))) for _ in range(10)]  # Generate baseline
        except Exception as e:
            print(e)
            return []

        predictor = Predictor(self.input_data)
        accuracy_tracker = AccuracyTracker()

        # Continuously get values

        while True:
            current_bg = (sampler.sample(enable_iterator=False))

            predictor.data = self.input_data
            prediction = predictor.predict(list(current_bg))

            print("Prediction: {}".format('White' if prediction == 'w' else 'Black'))
            screen.fill([0, 0, 0] if prediction == 'b' else [255, 255, 255])

            try:
                self.input_data.append(self.show_buttons(screen, current_bg))
            except Exception as e:
                print(e)
                break

            accuracy_tracker += (prediction == self.input_data[-1][1])
            print(str(accuracy_tracker.accuracy) + '%')  # Show past 20 accuracy

        pygame.quit()


if __name__ == '__main__':
    # Spacing between color values when generating output, int default=16.
    # ie 0, DENSITY, 2*DENSITY
    DENSITY = None

    # Range of values to generate output for, tuple[int] default=(0, 256)
    # ie (all_min, all_max) or (red_min, red_max, green_min, green_max, blue_min, blue_max)
    MAP_SIZE = None

    # Gather data
    demo = TextColorChooser(DENSITY, MAP_SIZE)

    # visualize or do something cool if u want
    # get the classification for every color w/ demo.data or demo.complete_data()
