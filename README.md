# 2019Vision
Collaboration!

Goal is to have groups of people collaborate to create a larger scale project than any one person would be able to alone.

## Git
Getting remote repo on local pc
* cd <directory>  # Change into a directory you want the folder in
* git clone <url>  # Download the remote repository to local pc

Before working
* git pull  # pull other peoples work to your local machine
* <edit code>
* git status  # see what git sees
* git add <files you want updated on repo>
* git commit -m "Description of changes here."
* git push  # push your updates to the remote repo

## SCRUM
* Most people work alone but then code all comes together at end
* Create branches to Isolate code 
* * git checkout -b feature/<featurename>  # When creating novel code
* * git checkout -b hotfix/<hotfixname>  # When combining / patching features
* Switch between branches
* * git checkout <feature/hotfix>/<branchname>

## Unit testing
Ensure every feature responds to input the way you expect in an automated way.

[Python unit testing library](https://docs.python.org/3/library/unittest.html)

Create robust unit tests so when you change your code, unit tests do not need to change much.

## Project Ideas
Ant sim - autonomy
OpenCL voroni tesselation
Cell tracking
Spacial body identification
Digit classification w/ KNN/NN

Classy group
	Detect planets in space pictures?

	Object tracking

ML group
	Recognize handwritten numbers given in some sort of on screen drawing. 

    * Make model agnostic so you may switch out model or what
    * * start w/ KNN?
    * * use pytorch to create a nn that will recognize digits -- this will better scale to recognizing more classes


    Create a reinforcement learning algorithm to play DOOM.
    * Can have leaderboard for which does best?
    * resources I gave ayden here


## Resources
[Intro to Numpy](https://github.com/coledie/Monte-Carlo-Simulation)

[Intro to CV w/ Numpy](https://www.kaggle.com/coledie/intro-to-computer-vision)

[CV w/ Scipy and OpenCV](https://www.kaggle.com/coledie/intro-to-computer-vision-2)

[Vision overview in team drive](https://drive.google.com/open?id=1dT2ow6sCkQifk0xZS4s1N0_G-nCKfon1znZfymsH39w)
