<img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/UAB.png" align="center" width="300" alt="header pic"/>

# C.A.R.L.E.S. Robotics Project
 Card-playing Algorithmic Robot for Leisure and Elder Socializing (C.A.R.L.E.S.)
 


# Table of Contents
   * [What is this?](#what-is-this)
   * [Requirements](#requirements)
   <img src="https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/imgs/FotoPortadaC.A.R.L.E.S.png" align="right" width="300" alt="header pic"/>
   * [Documentation](#documentation)
   * [How to use](#how-to-use)
   * [Localization](#localization)
      * [Extended Kalman Filter localization](#extended-kalman-filter-localization)
      * [Particle filter localization](#particle-filter-localization)
      * [Histogram filter localization](#histogram-filter-localization)
   * [Description](#Description)
   * [MODULES](#modules)
      * [Kinematics](#kinematics)
      * [Ray casting grid map](#ray-casting-grid-map)
      * [Lidar to grid map](#lidar-to-grid-map)
      * [k-means object clustering](#k-means-object-clustering)

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



# Modules

## Kinematics

This is a animation example of the traslation simulation program that we made from zero.

![2](https://github.com/OriolMoreno/C.A.R.L.E.S/blob/master/gif/ik.gif)

## Ray casting grid map

This is a 2D ray casting grid mapping example.

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/Mapping/raycasting_grid_map/animation.gif)

## Lidar to grid map

This example shows how to convert a 2D range measurement to a grid map.

![2](Mapping/lidar_to_grid_map/animation.gif)

## k-means object clustering

This is a 2D object clustering with k-means algorithm.

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/Mapping/kmeans_clustering/animation.gif)

## Rectangle fitting

This is a 2D rectangle fitting for vehicle detection.

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/Mapping/rectangle_fitting/animation.gif)


# SLAM

Simultaneous Localization and Mapping(SLAM) examples

## Iterative Closest Point (ICP) Matching

This is a 2D ICP matching example with singular value decomposition.

It can calculate a rotation matrix and a translation vector between points to points.

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/SLAM/iterative_closest_point/animation.gif)

Ref:

- [Introduction to Mobile Robotics: Iterative Closest Point Algorithm](https://cs.gmu.edu/~kosecka/cs685/cs685-icp.pdf)


## FastSLAM 1.0

This is a feature based SLAM example using FastSLAM 1.0.

The blue line is ground truth, the black line is dead reckoning, the red line is the estimated trajectory with FastSLAM.

The red points are particles of FastSLAM.

Black points are landmarks, blue crosses are estimated landmark positions by FastSLAM.


![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/SLAM/FastSLAM1/animation.gif)


Ref:

- [PROBABILISTIC ROBOTICS](http://www.probabilistic-robotics.org/)

- [SLAM simulations by Tim Bailey](http://www-personal.acfr.usyd.edu.au/tbailey/software/slam_simulations.htm)


# Path Planning

## Dynamic Window Approach

This is a 2D navigation sample code with Dynamic Window Approach.

- [The Dynamic Window Approach to Collision Avoidance](https://www.ri.cmu.edu/pub_files/pub1/fox_dieter_1997_1/fox_dieter_1997_1.pdf)

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/DynamicWindowApproach/animation.gif)


## Grid based search

### Dijkstra algorithm

This is a 2D grid based shortest path planning with Dijkstra's algorithm.

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/Dijkstra/animation.gif)

In the animation, cyan points are searched nodes.

### A\* algorithm

This is a 2D grid based shortest path planning with A star algorithm.

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/AStar/animation.gif)

In the animation, cyan points are searched nodes.

Its heuristic is 2D Euclid distance.

### Potential Field algorithm

This is a 2D grid based path planning with Potential Field algorithm.

![PotentialField](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/PotentialFieldPlanning/animation.gif)

In the animation, the blue heat map shows potential value on each grid.

Ref:

- [Robotic Motion Planning:Potential Functions](https://www.cs.cmu.edu/~motionplanning/lecture/Chap4-Potential-Field_howie.pdf)

### Grid based coverage path planning

This is a 2D grid based coverage path planning simulation.

![PotentialField](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/GridBasedSweepCPP/animation.gif)

## State Lattice Planning

This script is a path planning code with state lattice planning.

This code uses the model predictive trajectory generator to solve boundary problem.

Ref: 

- [Optimal rough terrain trajectory generation for wheeled mobile robots](http://journals.sagepub.com/doi/pdf/10.1177/0278364906075328)

- [State Space Sampling of Feasible Motions for High-Performance Mobile Robot Navigation in Complex Environments](http://www.frc.ri.cmu.edu/~alonzo/pubs/papers/JFR_08_SS_Sampling.pdf)


### Biased polar sampling

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/StateLatticePlanner/BiasedPolarSampling.gif)


### Lane sampling

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/StateLatticePlanner/LaneSampling.gif)

## Probabilistic Road-Map (PRM) planning 

![PRM](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/ProbabilisticRoadMap/animation.gif)

This PRM planner uses Dijkstra method for graph search.

In the animation, blue points are sampled points,

Cyan crosses means searched points with Dijkstra method,

The red line is the final path of PRM.

Ref:

- [Probabilistic roadmap \- Wikipedia](https://en.wikipedia.org/wiki/Probabilistic_roadmap)

　　

## Rapidly-Exploring Random Trees (RRT)

### RRT\*

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/RRTstar/animation.gif)

This is a path planning code with RRT\*

Black circles are obstacles, green line is a searched tree, red crosses are start and goal positions.

Ref:

- [Incremental Sampling-based Algorithms for Optimal Motion Planning](https://arxiv.org/abs/1005.0416)

- [Sampling-based Algorithms for Optimal Motion Planning](http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.419.5503&rep=rep1&type=pdf)

### RRT\* with reeds-shepp path

![Robotics/animation.gif at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/RRTStarReedsShepp/animation.gif))

Path planning for a car robot with RRT\* and reeds shepp path planner.

### LQR-RRT\*

This is a path planning simulation with LQR-RRT\*.

A double integrator motion model is used for LQR local planner.

![LQRRRT](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/LQRRRTStar/animation.gif)

Ref:

- [LQR\-RRT\*: Optimal Sampling\-Based Motion Planning with Automatically Derived Extension Heuristics](http://lis.csail.mit.edu/pubs/perez-icra12.pdf)

- [MahanFathi/LQR\-RRTstar: LQR\-RRT\* method is used for random motion planning of a simple pendulum in its phase plot](https://github.com/MahanFathi/LQR-RRTstar)


## Quintic polynomials planning

Motion planning with quintic polynomials.

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/QuinticPolynomialsPlanner/animation.gif)

It can calculate 2D path, velocity, and acceleration profile based on quintic polynomials.

Ref:

- [Local Path Planning And Motion Control For Agv In Positioning](http://ieeexplore.ieee.org/document/637936/)

## Reeds Shepp planning

A sample code with Reeds Shepp path planning.

![RSPlanning](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/ReedsSheppPath/animation.gif?raw=true)

Ref:

- [15.3.2 Reeds\-Shepp Curves](http://planning.cs.uiuc.edu/node822.html) 

- [optimal paths for a car that goes both forwards and backwards](https://pdfs.semanticscholar.org/932e/c495b1d0018fd59dee12a0bf74434fac7af4.pdf)

- [ghliu/pyReedsShepp: Implementation of Reeds Shepp curve\.](https://github.com/ghliu/pyReedsShepp)


## LQR based path planning

A sample code using LQR based path planning for double integrator model.

![RSPlanning](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/LQRPlanner/animation.gif?raw=true)


## Optimal Trajectory in a Frenet Frame 

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathPlanning/FrenetOptimalTrajectory/animation.gif)

This is optimal trajectory generation in a Frenet Frame.

The cyan line is the target course and black crosses are obstacles.

The red line is predicted path.

Ref:

- [Optimal Trajectory Generation for Dynamic Street Scenarios in a Frenet Frame](https://www.researchgate.net/profile/Moritz_Werling/publication/224156269_Optimal_Trajectory_Generation_for_Dynamic_Street_Scenarios_in_a_Frenet_Frame/links/54f749df0cf210398e9277af.pdf)

- [Optimal trajectory generation for dynamic street scenarios in a Frenet Frame](https://www.youtube.com/watch?v=Cj6tAQe7UCY)


# Path Tracking

## move to a pose control

This is a simulation of moving to a pose control

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathTracking/move_to_pose/animation.gif)

Ref:

- [P. I. Corke, "Robotics, Vision and Control" \| SpringerLink p102](https://link.springer.com/book/10.1007/978-3-642-20144-8)


## Stanley control

Path tracking simulation with Stanley steering control and PID speed control.

![2](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathTracking/stanley_controller/animation.gif)

Ref:

- [Stanley: The robot that won the DARPA grand challenge](http://robots.stanford.edu/papers/thrun.stanley05.pdf)

- [Automatic Steering Methods for Autonomous Automobile Path Tracking](https://www.ri.cmu.edu/pub_files/2009/2/Automatic_Steering_Methods_for_Autonomous_Automobile_Path_Tracking.pdf)



## Rear wheel feedback control

Path tracking simulation with rear wheel feedback steering control and PID speed control.

![PythonRobotics/figure_1.png at master · AtsushiSakai/PythonRobotics](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathTracking/rear_wheel_feedback/animation.gif)

Ref:

- [A Survey of Motion Planning and Control Techniques for Self-driving Urban Vehicles](https://arxiv.org/abs/1604.07446)


## Linear–quadratic regulator (LQR) speed and steering control

Path tracking simulation with LQR speed and steering control.

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathTracking/lqr_speed_steer_control/animation.gif)

Ref:

- [Towards fully autonomous driving: Systems and algorithms \- IEEE Conference Publication](http://ieeexplore.ieee.org/document/5940562/)


## Model predictive speed and steering control

Path tracking simulation with iterative linear model predictive speed and steering control.

<img src="https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathTracking/model_predictive_speed_and_steer_control/animation.gif" width="640" alt="MPC pic">

Ref:

- [notebook](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathTracking/model_predictive_speed_and_steer_control/Model_predictive_speed_and_steering_control.ipynb)

- [Real\-time Model Predictive Control \(MPC\), ACADO, Python \| Work\-is\-Playing](http://grauonline.de/wordpress/?page_id=3244)

## Nonlinear Model predictive control with C-GMRES

A motion planning and path tracking simulation with NMPC of C-GMRES 

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/PathTracking/cgmres_nmpc/animation.gif)

Ref:

- [notebook](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathTracking/cgmres_nmpc/cgmres_nmpc.ipynb)


# Arm Navigation

## N joint arm to point control

N joint arm to a point control simulation.

This is a interactive simulation.

You can set the goal position of the end effector with left-click on the ploting area. 

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/ArmNavigation/n_joint_arm_to_point_control/animation.gif)

In this simulation N = 10, however, you can change it.

## Arm navigation with obstacle avoidance 

Arm navigation with obstacle avoidance simulation.

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/ArmNavigation/arm_obstacle_navigation/animation.gif)


# Aerial Navigation

## drone 3d trajectory following 

This is a 3d trajectory following simulation for a quadrotor.

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/AerialNavigation/drone_3d_trajectory_following/animation.gif)

## rocket powered landing

This is a 3d trajectory generation simulation for a rocket powered landing.

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/AerialNavigation/rocket_powered_landing/animation.gif)

Ref:

- [notebook](https://github.com/AtsushiSakai/PythonRobotics/blob/master/AerialNavigation/rocket_powered_landing/rocket_powered_landing.ipynb)

# Bipedal

## bipedal planner with inverted pendulum

This is a bipedal planner for modifying footsteps with inverted pendulum.

You can set the footsteps and the planner will modify those automatically.

![3](https://github.com/AtsushiSakai/PythonRoboticsGifs/raw/master/Bipedal/bipedal_planner/animation.gif)

# License 

MIT

# Use-case

If this project helps your robotics project, please let me know with creating an issue.

Your robot's video, which is using PythonRobotics, is very welcome!!

This is a list of other user's comment and references:[users\_comments](https://github.com/AtsushiSakai/PythonRobotics/blob/master/users_comments.md)

# Contribution

Any contribution is welcome!!

If your PR is merged multiple times, I will add your account to the author list.

# Citing

If you use this project's code for your academic work, we encourage you to cite [our papers](https://arxiv.org/abs/1808.10703) 

If you use this project's code in industry, we'd love to hear from you as well; feel free to reach out to the developers directly.

# Support

If you or your company would like to support this project, please consider:

- [Sponsor @AtsushiSakai on GitHub Sponsors](https://github.com/sponsors/AtsushiSakai)

- [Become a backer or sponsor on Patreon](https://www.patreon.com/myenigma)

- [One-time donation via PayPal](https://www.paypal.me/myenigmapay/)

# Authors

- [Atsushi Sakai](https://github.com/AtsushiSakai/)

- [Daniel Ingram](https://github.com/daniel-s-ingram)

- [Joe Dinius](https://github.com/jwdinius)

- [Karan Chawla](https://github.com/karanchawla)

- [Antonin RAFFIN](https://github.com/araffin)

- [Alexis Paques](https://github.com/AlexisTM)

- [Ryohei Sasaki](https://github.com/rsasaki0109)

- [Göktuğ Karakaşlı](https://github.com/goktug97)

- [Guillaume Jacquenot](https://github.com/Gjacquenot)

- [Erwin Lejeune](https://github.com/guilyx)

