<!-- <img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/UAB.png" align="center" width="300" alt="header pic"/> -->

# C.A.R.L.E.S. Robotics Project
 Card-playing Algorithmic Robot for Leisure and Elder Socializing (_C.A.R.L.E.S._)



# Table of Contents
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/FotoPortadaC.A.R.L.E.S.png" align="right" width="300" alt="header pic"/>

   * [What is this?](#what-is-this)
   <!--* [Requirements](#requirements)
   * [Documentation](#documentation)
   * [How to use](#how-to-use)-->
   * [Description](#Description)
   * [Amazing contributions](#Amazing-contributions)
   * [Hardware Scheme](#Hardware-Scheme)   
   * [3D pieces](#3D-pieces)
   * [Software Architecture](#Software-Architecture)
   * [Modules](#modules)
      * [Brisca AI](#Brisca-AI)
      * [Card Detection with computer vision](#Card-Detection-with-computer-vision)
      * [Inverse kinematics algorithm visualizer](#Inverse-kinematics-algorithm-visualizer)
      * [Voice Recognition](#voice-recognition)
      * [Videogame Simulation](#videogame-simulation)

   * [Video](#video)
   * [Downloads](#downloads)
   * [Authors](#authors)



# What is this?

We are 3rd year Computer Science students and this is a robotics project for our subject on Robòtica, Llenguatge i Planificació - Robotics Language and Planning.


We have focused deeply on polishing the software part of the project, but due to the circumstances (this project was interrupted by the 2020 Coronavirus outbreak), we haven't been able to implement it on hardware. Instead, we have prepared a full-on videogame to act as a simulation for what this project can become. And it is prepared for anyone to take it and move our sofware modules to a phisical robot.

This is where you come in!


# Description
_C.A.R.L.E.S_ is a robot capable of playing 1vs1 (Human vs AI)  matches of the typical Spanish game card game Brisca.

The main mechanical part is a 3-axis anthropomorphical arm, which allows movement in a semicircular area on the board. At the end of the last joint there is a manipulator which in our case is a suction cup, able to pick up and move cards without any trouble. The pneumatic circuit is powered by the void created with a medical syringe, activated through a servomotor. 

The board adapts to the workspace of the arm, while maintaining the typical layout of the brisca game  as much as possible. The robot's hand is on its right and elevated so it is possible to fit a camera inside the box that holds them and thus be able to perform card recognition via computer vision. This way the robot is aware of what cards it has on it's hand. 
Each player's cards, the *triumfo* card and deck are in the center of the board. There is also a second camera lifted from the table that oversees the playing area. This way C.A.R.L.E.S. is also aware of the cards that are being played. 
Finally, to the left of the arm there is a mechanism that allows the robot to spin a card.

However, the hardware planification we just described was not possible to perform due to the educational context we found ourselves in. We had to change the main focus to pure software development and the polishing of each module itself and as a whole.

_C.A.R.L.E.S_ is able to:<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/cartas.png" align="right" width="300" alt="header pic"/>
- Recognize cards with the computer vision module (number and suit of the card).
- Play a brisca game with an AI algorithm that will do its best to outsmart the opponent.
- Control the actions to be performed (start and end game, steal a card, knowing it's C.A.R.L.E.S.' turn, etc.) by voice commands that the human will say during the game.
- Calculate the angles of rotation of the arm motors in order to move the manipulator (including the one that controls the pressure of the suction cup) from one point to another, according to the positions of everything else on the board.
- Unification of all the modules in a single workflow, which is what the physical robot would have had.



# Amazing contributions

The three most important contributions in which our robot stands up are:<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/braç.png" align="right" width="150" alt="header pic"/>
- Entertainment for seniors:  it is designed to entertain the elderly, for whom robots are a whole new thing.
- Classic Game Automation, the brisca: we give life to a classic and mythical game like the brisca combining it with technology and having it be even more enjoyable.
- Voice recognition with human interaction: Designed to bring the user closer to the robot and allows them to communicate with it.

# Hardware Scheme
This is the Hardware Scheme we planned for this project, within the 100€ budget we had. It's free for anyone to use it but we'd heavily recommend, if they're going to invest in making this project, to put some better hardware on it.

<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/carles_sketch_bb.png" align="center" width="600" alt="header pic"/>


# 3D pieces
In order to recreate the physical model of the robot, we had to design some of its parts as models to print with a 3D printer the university gave us access to. This are the models needed.  

<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/cam.png" width="100" align="center"/>
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/xeringa.png" width="250" align="center"/>
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/girador.png" width="200" align="center"/>
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/deck.png" width="250" align="center"/>
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/pila.png" width="200" align="center"/>

<!--![2](imgs/cam.png =100x)
![2](imgs/xeringa.png =250x)
![](imgs/girador.png =200x)
![](imgs/deck.png =250x)
![](imgs/pila.png =200x)-->


Files are avaliable under [stl](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/stl/). Of course they could be replaced by any other model or created with other methods rather than 3D printing.



# Software Architecture

In order to develop the idea we had, we must divide the software architecture in different modules. First to make them work separately and then be able to put them all together as one whole project. The modules are:
* Computer Vision module: card recognition
* Brisca AI 1vs1
* Inverse Kinematics
* Voice Recognition
* Controller: communication of all the above modules.

Initially all of them should have worked together, but after the project's objectives changed we decided to do different simulations in order to reproduce the functionality we were aiming for. These are:
* Computer Vision module: card recognition (as an independent simulation)
* Inverse Kinematics Simulation: not only doing the math but also visualizing it.
* Fully functional 3D game: This simulation involves 3D models, animation and game development to have a fully inmersive experience and getting the closest image to what the project was going to look like.

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/DiagramaModuls.png)



## Modules

### Brisca AI
Requirements for the algorithm: python 3

The first module is the AI that drives the game flow, it's the one who decides which card to choose from those on _C.A.R.L.E.S._' hand, based on what a human player could see, and more. It is explained in more detail in the [report](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/reports/RLP_SPRINT_5%20-%20Final%20Report.pdf)), both it's python version for the actual raspberry pi-driven robot and the rework we made for the Unity videogame.

### Card Detection with computer vision
We made a program based on computer vision able to detect the number and suit of a card with any rotation and different backgrounds and illuminations. Here we show a part of the process: 

Requirements: Python 3, and its libraries numpy, cv2, imutils, math and scipy.

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/gif/modulVisio.gif)


### Inverse kinematics algorithm + visualizer

This algorithm built from scratch is based on the geometric inverse kinematics method for calculating arm degrees from coordinates, and the smooth movement between two points is calculated using a continuous rectiliniar trajectory.

The visualizer takes an imput of an x,y,z position inside the workspace and shows an animation of _C.A.R.L.E.S._' arm doing the designated trajectory. As an example, this is the animation it'd play as a celebration when winning the game:

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/gif/ik.gif)

Requirements for the algorithm: Python 3 and the numpy and maths libraries. For visualization, matplotlib and scipy are also needed.


### Voice recognition

This module is based on google's speech recognition API, and it's used to analize the human opponent's orders, and guess which of the possible actions the user is requesting. This is sent to the main controller, which will send the information to the AI module if necessary.

Requirements: Python 3 and its libraries google-cloud-speech, google-auth-oauthlib, sounddevice and soundfile.

### Videogame Simulation
Finally, to show how it would have been had we been able to implement on harware, we've build a simulation videogame, in which you can play full Brisca matches against _C.A.R.L.E.S._! In it, there's the brisca player algorithm adapted for the simulation (further detail on the [report](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/reports/RLP_SPRINT_5%20-%20Final%20Report.pdf)), and we've also added some of the Human Interaction part of the project, as _C.A.R.L.E.S._ speaks and grunts during the match.

Here's a little demo of the game, but you can download it and try it yourself! See the [Downloads section](#Downloads).

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/gif/simulació%20brisca.gif)

# Video
Short video showing all the functionalities of the project.

[![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/gif/funcionalities.gif)](https://www.youtube.com/watch?v=alATNutyEoA&feature=youtu.be)

Click the animated gif for the full version!





# Downloads
[Windows](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/simulation.exe)

[Android](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/carles.apk)

For MacOs you'll have to clone the repo and you'll find it under unity_simulation/BuildMacOs


# Authors

- [ADRIÀ CARRASQUILLA](https://github.com/adriacarrasquilla) - 1492104

- [ORIOL MORENO](https://github.com/OriolMoreno) - 1496663

- [JAN MOROS](https://github.com/janMoros) - 1492333

- [VÍCTOR SUÁREZ](https://github.com/VictorSuarezVara) - 1493402
