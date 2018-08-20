import brickpi
import time

interface=brickpi.Interface()
interface.initialize()

motors = [0,1]

interface.motorEnable(motors[0])
interface.motorEnable(motors[1])

motorParams = interface.MotorAngleControllerParameters()
motorParams.maxRotationAcceleration = 6.0
motorParams.maxRotationSpeed = 12.0
motorParams.feedForwardGain = 255/20.0
motorParams.minPWM = 18.0
motorParams.pidParameters.minOutput = -255
motorParams.pidParameters.maxOutput = 255
#motorParams.pidParameters.k_p = 340
#motorParams.pidParameters.k_i = 300
#motorParams.pidParameters.k_d = 300

motorParamsRight = motorParams
motorParamsLeft = motorParams

motorParamsRight.pidParameters.k_p = 340 
motorParamsRight.pidParameters.k_i = 300
motorParamsRight.pidParameters.k_d = 300

motorParamsLeft.pidParameters.k_p = 240
motorParamsLeft.pidParameters.k_i = 290
motorParamsLeft.pidParameters.k_d = 370

interface.setMotorAngleControllerParameters(motors[0],motorParamsLeft)
interface.setMotorAngleControllerParameters(motors[1],motorParamsRight)

def Left90deg():
    print("Turning 90 left")
    THRESHOLD = 3
    angle = 3.75
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
    angle = 3.75
    startTime = time.time()
    interface.increaseMotorAngleReferences(motors, [-angle, angle])
    while interface.motorAngleReferencesReached:
        timeNow = time.time()
        if timeNow - startTime > THRESHOLD:
                print "Done with turning 90 right -> Ready to execute next move!"
                break

def Forward40():
    print("Forward 40")
    THRESHOLD = 3
    distance = 11.75
    startTime = time.time()
    interface.increaseMotorAngleReferences(motors, [-distance, -distance])
    while interface.motorAngleReferencesReached:
        timeNow = time.time()
        if timeNow - startTime > THRESHOLD:
                print "Done with forward 40 -> Ready to execute next move!"
                break

def Backwards40():
    print("Backwards 40")
    THRESHOLD = 3
    distance = 11.75
    startTime = time.time()
    interface.increaseMotorAngleReferences(motors, [distance, distance])
    while interface.motorAngleReferencesReached:
        timeNow = time.time()
        if timeNow - startTime > THRESHOLD:
                print "Done with backwards 40 -> Ready to execute next move!"
                break
    

Forward40()
Left90deg()
Forward40()
Left90deg()
Forward40()
Left90deg()
Forward40()
Left90deg()

interface.terminate()
