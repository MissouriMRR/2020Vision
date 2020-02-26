# Monte-Carlo-Simulation
Monte Carlo Simulation of the game Craps. 

The goal is to use Numpy for a significantly faster run time than pure Python and demonstrate that whole numpy arrays can be treated as a single object.

All solutions here give a 49.2% chance of winning. Over 1 million iterations, the craps_masked function takes 1.8 seconds to run while the craps_optimzed function takes .16 seconds and the pure python implementation takes 7.9 seconds. The optimized numpy version has an 11x speed increase over the masked version and a 49x speed increase over the pure python version. 

[A more fleshed out example and problem description.](https://crunchingnumbers.live/2016/01/24/monte-carlo-simulations-craps/)
