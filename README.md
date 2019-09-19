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

# TODO - Link everythin

Interested in Autonomy?

* Flocking algorithm, all agents think independantly but create emergent flocking behavior

* Create an ant simulator where all of the ants think independantly with simple logic and create complex emergent behaviors.

Interested in writing code for the Graphics Card?

* Write a voroni tesselation program in OpenCL

* Apply convolutions to images super fast

Interested in more complex Computer Vision?

* Perform skeletonization on an image w/ erosion and dialation convolutions.

* Use scipy-generic filter to simulate the game of life or another cellular automaton game.

* Track cells w/ blob tracking.

* Identify objects in space with shape detection[or something else cool].

Interested in Machine Learning?

* Use k-means to to change the color of tomatoes in a salad to blue.

* Make a handwritten digit classifier w/ K-Nearest Neighbors, and upgrade it to a Neural Network!

* Create a reinforcement learning algorithm to play some openai-gym games!


## Resources
[Intro to Numpy](https://github.com/coledie/Monte-Carlo-Simulation)

[Intro to CV w/ Numpy](https://www.kaggle.com/coledie/intro-to-computer-vision)

[CV w/ Scipy and OpenCV](https://www.kaggle.com/coledie/intro-to-computer-vision-2)

[Vision overview in team drive](https://drive.google.com/open?id=1dT2ow6sCkQifk0xZS4s1N0_G-nCKfon1znZfymsH39w)
