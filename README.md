# 2019Vision
Collaboration!

Goal is to create some interesting projects while waiting for Mission 9 details to be released.

## Git
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

## SCRUM
* Ensure necessary tasks are being completed.
* Most people work alone but then code all comes together at end.
* Create branches to Isolate code
* * git checkout -b <team&gt;/feature/<featurename&gt;  # When creating novel code
* * git checkout -b <team&gt;/hotfix/<hotfixname&gt;  # When combining / patching features
* Switch between branches
* * git checkout <team&gt;/<feature/hotfix&gt;/<branchname&gt;

## Unit testing
Ensure every feature responds to input the way you expect _in an automated way._

[Python unit testing library](https://docs.python.org/3/library/unittest.html)

Create robust unit tests so when you change your code, unit tests do not need to change much.

## Project Ideas

Interested in Autonomy?

* [Flocking algorithm](https://www.red3d.com/cwr/boids/), all agents think independantly but create emergent behavior.

* [Ant colony simulator](https://web.stanford.edu/~jayantt/data/ants.pdf), trying to mimic the use of pheremones to create intelligent, efficient communities.

Interested in writing code for the Graphics Card?

* Write a [voroni tesselation](https://en.wikipedia.org/wiki/Voronoi_diagram) program with [OpenCL.](https://www.codeproject.com/articles/92788/introductory-tutorial-to-opencl)

* Apply [convolutions](https://en.wikipedia.org/wiki/Kernel_(image_processing)) to images super fast with [OpenCL.](https://www.codeproject.com/articles/92788/introductory-tutorial-to-opencl)

Interested in analytic Computer Vision methods?

* Use scipy [generic_filter](https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.generic_filter.html) to simulate a [cellular automaton](https://en.wikipedia.org/wiki/Cellular_automaton) game. [Wolfram 1D Automaton](https://natureofcode.com/book/chapter-7-cellular-automata/), [Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life), [Langton's Ant](https://en.wikipedia.org/wiki/Langton%27s_ant), [Wireworld](https://en.wikipedia.org/wiki/Wireworld).



* Perform skeletonization on an image w/ erosion and dialation convolutions.

* Track cells w/ blob tracking, .

* Identify objects in space with shape detection[or something else cool].



Interested in Machine Learning?

* Use [k-means](https://www.datascience.com/blog/k-means-clustering) unsupervised clustering algorithm to change the color of [tomatoes in a salad to blue](https://proxy.duckduckgo.com/iu/?u=https%3A%2F%2Ftse2.mm.bing.net%2Fth%3Fid%3DOIP.YCwt0csrYMHvB2aPOqESqwHaLH%26pid%3DApi&f=1) with [sklearn.](https://scikit-learn.org/stable/modules/generated/sklearn.cluster.KMeans.html)

* Make a handwritten numerical digit classifier w/ [K-Nearest Neighbors](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), and upgrade it to a Neural Network! Use the [MNIST dataset to train the model.](http://yann.lecun.com/exdb/mnist/)

* Create a [reinforcement learning algorithm](https://www.cse.unsw.edu.au/~cs9417ml/RL1/index.html) to play some [openai-gym games](https://gym.openai.com/docs/), use [q-learning](https://en.wikipedia.org/wiki/Q-learning)! [Sample code.](https://github.com/coledie/q-learning)


## Resources
[Intro to Numpy](https://github.com/coledie/Monte-Carlo-Simulation)

[Intro to CV w/ Numpy](https://www.kaggle.com/coledie/intro-to-computer-vision)

[CV w/ Scipy and OpenCV](https://www.kaggle.com/coledie/intro-to-computer-vision-2)

[Vision overview in team drive](https://drive.google.com/open?id=1dT2ow6sCkQifk0xZS4s1N0_G-nCKfon1znZfymsH39w)
