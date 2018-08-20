import brickpi
import time
import random 

interface=brickpi.Interface()
interface.initialize()

# Settings from CW1 carried forward here to move forward, backwards and turn.
motors = [0,3]
speed = 6.0

# Motor ports.
interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255

# Option for different PID tuning among L/R motors.
motorParamsRight = motorParams
motorParamsLeft = motorParams

motorParamsLeft.pidParameters.k_p = 250
motorParamsLeft.pidParameters.k_i = 225
motorParamsLeft.pidParameters.k_d = 0

motorParamsRight.pidParameters.k_p = 250
motorParamsRight.pidParameters.k_i = 225
motorParamsRight.pidParameters.k_d = 0

interface.setMotorAngleControllerParameters(motors[0],motorParamsLeft)
interface.setMotorAngleControllerParameters(motors[1],motorParamsRight)

# Touch sensors, L/R for left and right.
L_touch_port = 1 
R_touch_port = 0 

interface.sensorEnable(L_touch_port, brickpi.SensorType.SENSOR_TOUCH);
interface.sensorEnable(R_touch_port, brickpi.SensorType.SENSOR_TOUCH);

# Function definitions.
# Non stop forward movement.
def Forward():
    print("Moving forward non stop")
    interface.setMotorRotationSpeedReferences(motors,[-speed, -speed])

# Moves backwards for provided amount of radians to avoid the obstacle in front of it.
def Backward(distance):
    print("Backward movement for " + str(distance) + " radians")
    THRESHOLD = 3 # can also be a fraction of time = distance/4 using CW1 working examples.
    startTime = time.time()
    interface.increaseMotorAngleReferences(motors, [distance, distance])
    while interface.motorAngleReferencesReached:
        timeNow = time.time()
        if timeNow - startTime > THRESHOLD:
                print "Done with backward movement -> Ready to execute next move!"
                break
                
# Left and Right angles movement should be calibrated in the program carpet_square.py
def Left90deg():
    print("Turning 90 left")
    THRESHOLD = 3
    angle = 4.85
    startTime = time.time()
    interface.increaseMotorAngleReferences(motors, [angle, -angle])
    while interface.motorAngleReferencesReached: 
        timeNow = time.time()
	if timeNow - startTime > THRESHOLD:
		print "Done with turning 90 left -> Ready to execute next move!"
		break
    
def Right90deg():
    print("Turning 90 right")
    THRESHOLD = 3
    angle = 4.85
    startTime = time.time()
    interface.increaseMotorAngleReferences(motors, [-angle, angle])
    while interface.motorAngleReferencesReached:
        timeNow = time.time()
        if timeNow - startTime > THRESHOLD:
                print "Done with turning 90 right -> Ready to execute next move!"
                break
                
# Program execution.
while True:
    # keep moving forward till you hit an obstacle
    Forward()    
   
    # touch sensors readings.
    L_touched = interface.getSensorValue(L_touch_port)
    R_touched = interface.getSensorValue(R_touch_port)
     
    # if both sensors are touched means we have a collision of type "->|OBSTACLE"
    if L_touched[0] and R_touched[0]:
        print "Hit obsacle - BOTH sensors"
        # to avoid it move backwards and then turn in a random Left or Right Direction.
        Backward(10)
        turn_options = [Left90deg, Right90deg]
        random.choice(turn_options)()
        Forward()
    
    # if left sensor is touched means we have a left diagonal collision "/>|OBSTACLE"
    elif L_touched[0]:
       print "Hit obstacle - LEFT sensor" 
       Backward(10)
       Left90deg()
       Forward()
    
    # if right sensor is touched means we have a rigth diagonal collision "\>|OBSTACLE"
    elif R_touched[0]:
       print "Hit obstacle - RIGHT sensor"
       Backward(10)
       Right90deg()
       Forward()
        
    time.sleep(0.5) # this is the time between feedback intervals.

interface.terminate()
