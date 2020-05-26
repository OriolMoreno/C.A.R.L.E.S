<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/UAB.png" align="center" width="300" alt="header pic"/>

# C.A.R.L.E.S. Robotics Project
 Card-playing Algorithmic Robot for Leisure and Elder Socializing (C.A.R.L.E.S.)
 


# Table of Contents 
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/FotoPortadaC.A.R.L.E.S.png" align="right" width="300" alt="header pic"/>

   * [What is this?](#what-is-this)
   * [Requirements](#requirements)
   * [Documentation](#documentation)
   * [How to use](#how-to-use) 
   * [Description](#Description)
   * [Amazing contributions](#Amazing-contributions)
   * [Hardware Scheme](#Hardware-Scheme)   
   * [3D pieces](#3D-pieces)
   * [Software Architecture](#Software-Architecture)
   * [MODULES](#modules)
      * [Brisca AI](#Brisca-AI)
      * [Card Detection with computer vision](#Card-Detection-with-computer-vision)
      * [Inverse kinematics algorithm visualizer](#kinematics)
      * [Human Interaction](#Human-Interaction)
      * [Simulation](#Simulation)

   * [Support](#support)
   * [Authors](#authors)



# What is this?
This is a robotic project made for the assignature of Robòtica, Llenguatge i Planificació. 



We made the software part deeply but we didn't get to the hardware due to Coronavirus. 
The poroject is prepared if some of the readers like you want to continue with C.A.R.L.E.S. and make it to the hardware part too.

Take a look at description part to know more about what C.A.R.L.E.S exactly is capable.

To take the first contact download this exe to see a soo realistic simulation of C.A.R.L.E.S:
"https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/simulation.exe" 


# Requirements

- Python 3.8.x

- numpy

- scipy

- matplotlib

- maths

- unity



# Documentation

This README only shows some part of this project. 

If you are interested on more information you can see the last report that we made for our assignature

You can also download the programs and some of them are made for people that dosen't have the knowledge of what this programs do or how. The program asks the client for some inputs to show the client some funcionalitis soo it will be easy for enyone, or that's whast we expect.

All animation gifs are stored here: [C.A.R.L.E.S/gif](https://github.com/OriolMoreno/C.A.R.L.E.S/tree/master/gif)


# How to use

1. Clone this repo.

> git clone https://github.com/OriolMoreno/C.A.R.L.E.S.git


2. Execute python script in each directory.
  Yow will need to download the libraries requiered for each think if you don't have-it downloaded yet. All the pythonic libraris that we used are free.

3. Add on or two stars to this repo if you like it :smiley:. 


# Description
C.A.R.L.E.S is a robot capable of playing 1vs1 (Human vs AI) games in the tipical spanish brisca game.
The main mechanism consists of a 3-axis anthropomorphic arm, which allows movement in a circular area on a board. At the end of the last shaft is a manipulator formed by a suction cup, which is controlled by a pneumatic mechanism with a servomotor and a syringe. The board adapts to the course of the arm, while maintaining as much as possible the typical layout of the brisca game. The robot's hand is on its right and elevated so that it can have a camera inside the box that holds them and thus be able to perform a card recognition by computer vision. Each player's cards, trump card and deck are in the center of the board. There is also a structure to have elevated a second camera that controls the playing area. Finally, to the left of the arm is a mechanism that allows the robot to spin a card. However, this part of the robot will not be able to be carried out for logical reasons in a pandemic situation. Then the project focuses on developing exclusively the robot software and being able to polish each module as a group and as a whole. In C.A.R.L.E.S it is able to:<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/cartas.png" align="right" width="300" alt="header pic"/>
- Recognize cards with the vision module (number and stick).
- Play a brisket game with an AI algorithm that will try to beat the opponent.
- Control the actions to be performed (start and end game, steal a card, know that it is the turn of the shift, etc.) by means of voice commands that the human will use during execution.
- Calculate the angles of rotation of the arm motors in order to move the manipulator (including the one that controls the pressure of the suction cup) from one point to another, according to the movements that should be made in case of its physical creation. .
- Unification of all the skills amended in a single workflow, which should be what the physical robot had.



# Amazing contributions
<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/braç.png" align="right" width="150"/>
the three most important contributions that brings this robot are:
- Entertainment for seniors:   it is designed to entertain the elderly, for whom robots are a whole new thing.
- Classic Game Automation, the brisca: we give life to a classic and mythical game like the brisca combining it with technology and having it be even more enjoyable.
- Voice recognition with human interaction: Designed to bring the user closer to the robot and allows it to communicate with it to a certain extent.

# Hardware Scheme
This is the exactly Hardware Shceme that we didn't make due to coronavirus but we expect its wright.

<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/carles_sketch_bb.png" align="center" width="600" alt="header pic"/>


# 3D pieces
Edited and personalitzed pices for C.A.R.L.E.S with name anotation.

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/girador.png)
![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/xeringa.png)



* [Software Architecture](#Software-Architecture)
   * [MODULES](#modules)
      * [Brisca AI](#Brisca-AI)
      * [Card Detection with computer vision](#Card-Detection-with-computer-vision)
      * [Inverse kinematics algorithm visualizer](#kinematics)
      * [Human Interaction](#Human-Interaction)
      * [Simulation](#Simulation)
      
      
      
# Software Architecture
this is the software architecture of the project with the hardware components to, is not the ones we have finally done cause the changes of the evaluation method made us change a few thinks.
We finally separte from the prject a few parts and we have maded them a partt. Thes are the parts we separate:
* The module of Computer Vision
* The human interaction 
* The realistic cinematic.

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/DiagramaModuls.png)





# Modules

## Inverse kinematics algorithm visualizer

This is a animation example of the traslation simulation program that we made from zero.

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/gif/ik.gif)



# Support

If you or your company would like to support this project, please consider writing a message to us and we will attend the call:



# Authors

- ADRIÀ CARRASQUILLA - 1492104

- ORIOL MORENO - 1496663

- JAN MOROS - 1492333

- VÍCTOR SUÁREZ - 1493402
