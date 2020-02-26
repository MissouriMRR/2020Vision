"""
Playing a lot of games of craps real fast with numpy.

The goal is to show how a numpy array can be thought of
the same as a single value with the help of broadcasting.
"""
import numpy as np
from random import randint


def python_roll(n):
    if n == 1:
        return randint(1, 6) + randint(1, 6)

    return [randint(1, 6) + randint(1, 6) for _ in range(n)]


def iterative_python(n_games):
    """
    Monte carlo search on the n_games games of craps.

    Pure python iterative implementation, very slow!
    
    Parameters
    ----------
    n_games: int
        Number of games to play.
    
    Returns
    -------
    Number of game wins.
    """
    wins = 0

    for _ in range(n_games):
        game1 = python_roll(1)

        # Act on winners, then loosers
        if game1 in [7, 11]:
            wins += 1
            continue

        if game1 in [2, 3, 12]:
            continue

        game2 = python_roll(1)

        while game2 not in [game1, 7]:
            game2 = python_roll(1)

        if game1 == game2:
            wins += 1

    return wins


def numpy_roll(n):
    """
    Roll two dice, n times.

    Parameters
    ----------
    n: int
        Number of dice rolls.

    Returns
    -------
    ndarray with n sums of dice rolls.
    """
    return np.random.randint(1, 7, size=n) + np.random.randint(1, 7, size=n)


def craps_masked(n_games):
    """
    A 'parrelelized' implementation of craps w/ masked arrays.
    
    Parameters
    ----------
    n_games: int
        Number of games to play.
    
    Returns
    -------
    Number of game wins.
    """
    wins = losses = 0

    ## Stage 1
    games = np.ma.array(numpy_roll(n_games), mask=[False] * n_games)

    # Act on winners, then loosers
    for value in [7, 11]:
        winlocs = np.where(games == value)

        wins += winlocs[0].size

        games.mask[winlocs] = True

    for value in [2, 3, 12]:
        losslocs = np.where(games == value)

        losses += losslocs[0].size

        games.mask[losslocs] = True

    ## Stage 2
    # note: the mask is shared between games 1 and 2 - proof!
    # >>> a = np.ma.array(np.arange(5), mask=[False] * 5)
    # >>> b = np.ma.array(np.arange(4, -1, -1), mask=a.mask)
    # >>> b
    # masked_array(data=[4, 3, 2, 1, 0],
    #              mask=[False, False, False, False, False],
    #        fill_value=999999)
    # >>> b.mask[2] = True
    # >>> b
    # masked_array(data=[4, 3, --, 1, 0],
    #              mask=[False, False,  True, False, False],
    #        fill_value=999999)
    # >>> a
    # masked_array(data=[0, 1, --, 3, 4],
    #              mask=[False, False,  True, False, False],
    #        fill_value=999999)
    games2 = np.ma.array(np.zeros(n_games), mask=games.mask)

    while wins + losses < n_games:
        games2 = np.ma.array(numpy_roll(n_games), mask=games.mask)

        winlocs = np.where(games2 == games)
        losslocs = np.where(games2 == 7)

        # Bugfix: Masked values return true when using == in
        #       winlocs! Fix win count being far too high by 
        #       subtracting count of already masked values.
        wins += winlocs[0].size - wins - losses
        losses += losslocs[0].size
        
        games2.mask[winlocs] = True
        games2.mask[losslocs] = True

    assert wins + losses == n_games, f"{wins + losses}, {n_games}"

    return wins


def craps_optimized(n_games):
    """
    An optimization of craps_masked, that implementation has a
    whole lot of recomputation - dice are rolled for games that 
    are already complete. To fix this, np.delete is used to remove
    completed games from the game arrays instead of masking them.

    Parameters
    ----------
    n_games: int
        Number of games to play.
    
    Returns
    -------
    Number of game wins.
    """
    wins = losses = 0

    ## Stage 1
    games = numpy_roll(n_games)

    # Act on winners, then loosers
    for value in [7, 11]:
        winlocs = np.where(games == value)

        wins += winlocs[0].size

        games = np.delete(games, winlocs)

    for value in [2, 3, 12]:
        losslocs = np.where(games == value)

        losses += losslocs[0].size

        games = np.delete(games, losslocs)

    ## Stage 2
    while wins + losses < n_games:
        assert n_games - wins - losses == games.size, f"{n_games - wins - losses} {games.size}"

        games2 = numpy_roll(games.size)

        winlocs = np.where(games2 == games)
        games = np.delete(games, winlocs)

        # bugfix: if dont delete from here, np.where(games2 == 7)
        #       will return values outside of games range.
        # note: numpy doesnt throw out of bounds errors w/ np.where
        games2 = np.delete(games2, winlocs)

        losslocs = np.where(games2 == 7)
        games = np.delete(games, losslocs)

        wins += winlocs[0].size
        losses += losslocs[0].size

    assert wins + losses == n_games, f"{wins + losses}, {n_games}"

    return wins


if __name__ == '__main__':
    N_GAMES = 10**6

    print(craps_masked(N_GAMES) / N_GAMES)
    print(craps_optimized(N_GAMES) / N_GAMES)

    print(iterative_python(N_GAMES) / N_GAMES)

    import timeit
    masked_time = timeit.timeit(lambda: craps_masked(N_GAMES), number=1)
    optimized_time = timeit.timeit(lambda: craps_optimized(N_GAMES), number=1)

    print(f'{N_GAMES} iterations, masked time: {masked_time:.3f}s, optimized time: {optimized_time:.3f}s')
    print(f'Optimized version is {masked_time / optimized_time:.2f}x faster than the masked version.')
    
    iterative_time = timeit.timeit(lambda: iterative_python(N_GAMES), number=1)
    print(f'{N_GAMES} iterations, pure python time: {iterative_time:.3f}s')
    print(f'Optimized numpy version is {iterative_time / optimized_time:.2f}x faster than the pure python version.')

