import brickpi
import time
import numpy

interface=brickpi.Interface()
interface.initialize()

port = 2 # port which ultrasoic sensor is plugged in to

interface.sensorEnable(port, brickpi.SensorType.SENSOR_ULTRASONIC);

sonar_values = [] * 100

def generate_report(trial):

	sonar_list = []

	for t in sonar_values:
		sonar_list.append(t[0])
        
    # STATISTICS
    mean = numpy.mean(sonar_values)
    var = numpy.var(sonar_values)
    std = numpy.std(sonar_values)
        
    # ANALYSIS
    accurate = sonar_list.count(trial)
    plus1 = sonar_list.count(trial+1)
    plus2 = sonar_list.count(trial+2)
    plus3 = sonar_list.count(trial+3)
    plus4 = sonar_list.count(trial+4)
    plus5 = sonar_list.count(trial+5)
    minus1 = sonar_list.count(trial-1)
    minus2 = sonar_list.count(trial-2)
    minus3 = sonar_list.count(trial-3)
    minus4 = sonar_list.count(trial-4)
    minus5 = sonar_list.count(trial-5)
    maximums = sonar_list.count(255)
    extremes = len(sonar_values) - (len(accurate) + len(plus1) + len(plus2) + len(plus3) + len(plus4) + len(plus5) + len(minus1) + len(minus2) + len(minus3) + len(minus4) + len(minus5) + len(maximums))

    # REPORT GENERATION
	print "\n---------- SONAR REPORT ----------\n"
        
    print "\n----------- STATISTICS -----------\n"
    print "Mean: " + str(mean)
    print "Variance: " + str(var)
    print "Standard deviation: " + str(std)
        
    print "\n------------ ANALYSIS ------------\n"
	
    print "\n------------- RANGE --------------\n"
    print "Trial distance " + str(trial) + ": " + str(len(accurate))
	print "+1 :" + str(len(plus1))
	print "+2 :" + str(len(plus2))
	print "+3 :" + str(len(plus3))
	print "+4 :" + str(len(plus4))
	print "+5 :" + str(len(plus5))
	print "-1 :" + str(len(minus1))
	print "-2 :" + str(len(minus2))
	print "-3 :" + str(len(minus3))
	print "-4 :" + str(len(minus4))
	print "-5 :" + str(len(minus5))
	
    print "\n------------ EXTREMES ------------\n"
    print "255 :" + str(len(maximums))
    print "Extreme values outside of range +/-5: " + str(len(extremes))

while True:
	
	trial = input("What distance are you measuring? -> ")

	# get 100 measurements
	for i in range(0, 100):

        	usReading = interface.getSensorValue(port)
        	if usReading :
                	sonar_values.append(usReading)
        	else:
			sonar_values.append("N/M")
        	time.sleep(0.05)

	generate_report(trial)	
	break

interface.terminate()

