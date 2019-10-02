# 2019Vision
Goal is to create some interesting projects while waiting for Mission 9 details to be released.

## Using Git
Getting remote repo on local pc
* cd <directory&gt;  # Change into a directory you want the folder in
* git clone <url&gt;  # Download the remote repository to local pc

Before working
* git pull  # pull other peoples work to your local machine
* <edit code&gt;
* git status  # see what git sees
* git add <files you want updated on repo&gt;
* git commit -m "Description of changes here."
* git push  # push your updates to the remote repo

## Unit testing
Ensure every feature responds to input the way you expect _in an automated way._

[Python unit testing library](https://docs.python.org/3/library/unittest.html)

Create robust unit tests so when you change your code, unit tests do not need to change much.

## Project Ideas

__Numpy Basics -- Should check these out before anything else!__

* [Monte carlo simulation](https://crunchingnumbers.live/2016/01/24/monte-carlo-simulations-craps/) of the game [craps.](http://www.crapsage.com/craps_rules.php) [Example here.](https://github.com/MissouriMRR/2019Vision/tree/master/Monte-Carlo-Simulation)

* [Image convolver](https://en.wikipedia.org/wiki/Kernel_(image_processing)) with Numpy -- [blurring](https://www.youtube.com/watch?v=C_zFhWdM4ic), [sobel operator for edge detection.](https://www.youtube.com/watch?v=uihBwtPIBxM)


__Interested in Autonomy?__

* [Flocking algorithm](https://www.red3d.com/cwr/boids/), all agents think independantly but create emergent behavior.

* [Ant colony simulator](https://web.stanford.edu/~jayantt/data/ants.pdf), trying to mimic the use of pheremones to create intelligent, efficient communities.


__Interested in writing code for the Graphics Card?__

* Follow this [CUDA tutorial.](https://towardsdatascience.com/writing-lightning-fast-code-with-cuda-c18677dcdd5f)

* Write a [voroni tesselation](https://en.wikipedia.org/wiki/Voronoi_diagram) program with [CUDA.](https://towardsdatascience.com/writing-lightning-fast-code-with-cuda-c18677dcdd5f)

* Compute planet orbits really fast with [CUDA.](https://towardsdatascience.com/writing-lightning-fast-code-with-cuda-c18677dcdd5f)


__Interested in analytic Computer Vision methods?__

* Shrink images to 1/2, 2/3, 3/4 scale with selective column dropping.

* Expand images to 2x, 3x scale with [interpolation.](https://en.wikipedia.org/wiki/Interpolation)

* Use scipy [generic_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generic_filter.html) to simulate a [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton) game. [Wolfram 1D Automaton](https://natureofcode.com/book/chapter-7-cellular-automata/), [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant), [Wireworld.](https://en.wikipedia.org/wiki/Wireworld)

* Use scipy [convolve](https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.convolve.html) to create an [edge detector](https://www.youtube.com/watch?v=uihBwtPIBxM), [blur filter](https://www.youtube.com/watch?v=C_zFhWdM4ic) or a [shape detector on space images(?).](http://www.ijcte.org/papers/428-G1120.pdf)

* Perform image [skeletonization](https://en.wikipedia.org/wiki/Morphological_skeleton) or clean up images with [erosion](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_erosion.html#scipy.ndimage.binary_erosion) and [dialation](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.binary_dilation.html#scipy.ndimage.binary_dilation) convolutions.

* Track cells or any simple object with [blob tracking](http://www.camera-sdk.com/p_97-how-to-implement-blob-binary-large-object-tracking-onvif.html), might use [mean shift.](https://www.youtube.com/watch?v=FsFreHtLXss) This likely applicable to our Mission 9 tasks. [This blog post.](https://www.pyimagesearch.com/2015/09/21/opencv-track-object-movement/)


__Interested in Machine Learning?__

* Write a [K-Nearest Neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm) model to predict the best background color to go with any given text color using [this already written GUI](https://github.com/MissouriMRR/2019Vision/tree/master/Background-Chooser-Shell) or your own interface. Alternatively write a model for automated weather prediction.

* Use [k-means](https://www.datascience.com/blog/k-means-clustering) unsupervised clustering algorithm to change the color of [tomatoes in a salad to blue](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.YCwt0csrYMHvB2aPOqESqwHaLH%26pid%3DApi&f=1) with [sklearn.](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

* Make a handwritten numerical digit classifier w/ [K-Nearest Neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), and upgrade it to a Neural Network! Use the [MNIST dataset to train the model.](http://yann.lecun.com/exdb/mnist/)

* Create a [reinforcement learning algorithm](https://www.cse.unsw.edu.au/~cs9417ml/RL1/index.html) to play some [openai-gym games](https://gym.openai.com/docs/), use [q-learning](https://en.wikipedia.org/wiki/Q-learning)! [Sample code.](https://github.com/coledie/q-learning)

* Currently working on a PyTorch / Deep learning notebook, in the meantime check out [these videos.](https://www.youtube.com/watch?v=aircAruvnKk&t=94s) This will be directly applicable to Mission 9 tasks.

## Resources
[Intro to Numpy](https://www.kaggle.com/coledie/intro-to-numpy/)

[Intro to CV w/ Numpy](https://www.kaggle.com/coledie/intro-to-computer-vision)

[CV w/ Scipy and OpenCV](https://www.kaggle.com/coledie/intro-to-computer-vision-2)

[Vision Overview in team drive](https://drive.google.com/open?id=1dT2ow6sCkQifk0xZS4s1N0_G-nCKfon1znZfymsH39w)
