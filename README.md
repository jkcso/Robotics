# Robotics

A course in Imperial College London Department of Computing, attended by third years and MSc students.  This is a one term course which focuses on mobile robotics, and aims to cover the basic issues in this dynamic field via lectures and a large practical element where students work in groups and implement robotics ideas using the Lego Mindstorms NXT kits and, since 2014, the Raspberry Pi single board computer and Python using BrickPi interface boards.

## Core Content

#### Robot Motion	Practical ####
Getting Started and Accurate Motion	Practical and concepts included Motion planning (also known as the navigation problem or the piano mover's problem) is a term used in robotics for the process of breaking down a desired movement task into discrete motions that satisfy movement constraints and possibly optimize some aspect of the movement.

For example, consider navigating a mobile robot inside a building to a distant waypoint. It should execute this task while avoiding walls and not falling down stairs. A motion planning algorithm would take a description of these tasks as input, and produce the speed and turning commands sent to the robot's wheels. Motion planning algorithms might address robots with a larger number of joints (e.g., industrial manipulators), more complex tasks (e.g. manipulation of objects), different constraints (e.g., a car that can only drive forward), and uncertainty (e.g. imperfect models of the environment or robot).

#### Sensors	Practical ####
Investigating Sensors	Practical and concepts including sensors that come with the EV3, you can make a robot respond to being touched, react when someone or something comes too close, follow a line, or measure how far they have turned.

##### Touch sensor #####
The touch sensor gives your robot a sense of touch. The touch sensor detects when it is being pressed or released. It can even be programmed to wait until it is both pressed and released (we call this bumped).

##### Colour sensor (colour, light) #####
The colour (or color) sensor can detect either the colour or intensity of light.  The colour sensor has three different modes: colour, reflected light intensity, and ambient light intensity.

##### Ultrasonic sensor (distance) #####
The ultrasonic sensor measures distance to an object up to a maximum of 255cm (or 100 inches) away. It does this by sending out high frequency sound waves that bounce off any object in range, and measuring how long it takes the sound to return to the sensor. In the software, you can select whether the distance is given in centimetres or inches.

The ultrasonic sensor also has a “listen only” mode that can detect whether another robot is using an ultrasonic sensor nearby. In this mode, the sensor listens for signals but does not send them.

##### Gyro sensor (rotation/orientation) #####
The gyro sensor detects rotational motion in the plane indicated by the arrows on the top of the sensor housing. The sensor measures the rate of rotation in degrees per second and keeps track of the total angle of rotation in degrees.

Note: When connecting the gyro sensor to your EV3 brick, you should hold it completely still in order to minimise drift. For best results, reset the angle using the reset mode of the gyro sensor block before every angle of motion you want to measure.

##### Large and medium motors (rotation) #####

Both the large and medium servo motors are equipped with internal rotation sensors. The rotation sensor is used to measure how far a motor has turned (or has been turned). Rotation sensors can detect an amount of rotation in degrees or full rotations. You can also use the rotation sensor to find out what power level a motor is currently running at.

##### Infrared sensor (distance) #####

The infrared sensor can measure distance or detect signals that are sent from the infrared beacon (see below).  The infrared sensor can be used in three different modes: proximity, beacon, and remote.

#### Probabilistic Robotics	Practical ####
Probabilistic Motion and Sensing	Practical including concepts on Bayes Filter implementatoin where we a customised transition model is required.  In our case, Odometry-based models were used because our robot was equipped with wheel encoders.

#### Monte Carlo Localisation	Practical ####
Monte Carlo Localisation Practical including the theory behind the aforemetioned algorithm (also known as particle filter localization).  It is essentially an algorithm used from robots to localize using a particle filter.  Given a map of the environment, the algorithm estimates the position and orientation of a robot as it moves and senses the environment.  The algorithm uses a particle filter to represent the distribution of likely states, with each particle representing a possible state, i.e., a hypothesis of where the robot is.  

The algorithm typically starts with a uniform random distribution of particles over the configuration space, meaning the robot has no information about where it is and assumes it is equally likely to be at any point in space.  Whenever the robot moves, it shifts the particles to predict its new state after the movement. Whenever the robot senses something, the particles are resampled based on recursive Bayesian estimation, i.e., how well the actual sensed data correlate with the predicted state. Ultimately, the particles should converge towards the actual position of the robot.

#### Advanced Sonar Sensing	Practical ####
Place Recognition	Practical and concepts including Localisation which involves one question: Where is the robot now? Or, robo-centrically, where am I, keeping in mind that "here" is relative to some landmark (usually the point of origin or the destination) and that you are never lost if you don't care where you are.

Although a simple question, answering it isn't easy, as the answer is different depending on the characteristics of your robot. Localization techniques that work fine for one robot in one environment may not work well or at all in another environment. For example, localizations which work well in an outdoors environment may be useless indoors.

All localization techniques generally provide two basic pieces of information:
* what is the current location of the robot in some environment?
* what is the robot's current orientation in that same environment?

The first could be in the form of Cartesian or Polar coordinates or geographic latitude and longitude. The latter could be a combination of roll, pitch and yaw or a compass heading.

#### SLAM and Planning	Practical ####
Simultaneous Localization and Mapping (SLAM) is the computational problem of constructing or updating a map of an unknown environment while simultaneously keeping track of an agent's location within it.  While this initially appears to be a chicken-and-egg problem there are several algorithms known for solving it, at least approximately, in tractable time for certain environments.  Popular approximate solution methods include the particle filter, extended Kalman filter, and GraphSLAM.

SLAM algorithms are tailored to the available resources, hence not aimed at perfection, but at operational compliance.  Published approaches are employed in self-driving cars, unmanned aerial vehicles, autonomous underwater vehicles, planetary rovers, newer domestic robots and even inside the human body.

#### Path Planning Challenge ####
The course always finishes with a competition where the groups compete to build and program the robot which can most effectively complete a certain challenge against the clock.
