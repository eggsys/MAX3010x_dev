from __future__ import print_function
import qwiic_max3010x
import time
from time import perf_counter
import sys

def millis():
	return int(round(time.time() * 1000))



def get_hr():
    print('#'*20)
    print("Getting HeartRate")
    print('#'*20)

    irValue = 25000
    beatsPerMinute = 67
    beatAvg  = 79
    Hz = 69.9
    return irValue, beatsPerMinute, beatAvg, Hz  


def loop_test():
    while True:
        print("X")
        break

def runAll():

    runDelta()
    heartRateData = runHeartRate()
    return heartRateData

def runDelta():

	print("\nSparkFun MAX3010x Photodetector - Example 1\n")
	sensor = qwiic_max3010x.QwiicMax3010x()

	if sensor.begin() == False:
		print("The Qwiic MAX3010x device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return
	else:
		print("The Qwiic MAX3010x is connected.")

  	# Setup to sense up to 18 inches, max LED brightness
	ledBrightness = 0xFF # Options: 0=Off to 255=50mA
	sampleAverage = 4 # Options: 1, 2, 4, 8, 16, 32
	ledMode = 2 # Options: 1 = Red only, 2 = Red + IR, 3 = Red + IR + Green
	sampleRate = 400 # Options: 50, 100, 200, 400, 800, 1000, 1600, 3200
	pulseWidth = 411 # Options: 69, 118, 215, 411
	adcRange = 2048 # Options: 2048, 4096, 8192, 16384

	if sensor.setup(ledBrightness, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange) == False:
		print("Device setup failure. Please check your connection", \
			file=sys.stderr)
		return
	else:
		print("Setup complete.")        

	sensor.setPulseAmplitudeRed(0) # Turn off Red LED
	sensor.setPulseAmplitudeGreen(0) # Turn off Green LED

	samplesTaken = 0       # Counter for calculating the Hz or read rate
	unblockedValue = 0     # Average IR at power up
	startTime = 0          # Used to calculate measurement rate

	# Take an average of IR readings at power up
	unblockedValue = 0
	for i in range(0,32):
		unblockedValue += sensor.getIR() # Read the IR value
	unblockedValue /= 32

	startTime = millis()
    
    
    
	while True:
                samplesTaken += 1

                IRSample = sensor.getIR()
                hertz = samplesTaken / ((millis() - startTime) / 1000)
                currentDelta = (IRSample - unblockedValue)

                hertz = round(hertz, 2)
                currentDelta = round(currentDelta, 2)

                message = ' ' # blank message
                print("currentDelta : ", currentDelta)
                if currentDelta > 100:
                    message = 'Something is there!'

                

                if currentDelta >= 10000:
                    print("Finger is there ! ")
                    break
        




def runHeartRate():
    #tic = time.perf_counter()
	print("\nSparkFun MAX3010x Photodetector - Example 5\n")
	sensor = qwiic_max3010x.QwiicMax3010x()

	if sensor.begin() == False:
		print("The Qwiic MAX3010x device isn't connected to the system. Please check your connection", \
			file=sys.stderr)
		return
	else:
		print("The Qwiic MAX3010x is connected.")

	print("Place your index finger on the sensor with steady pressure.")

	if sensor.setup() == False:
		print("Device setup failure. Please check your connection", \
			file=sys.stderr)
		return
	else:
		print("Setup complete.")

	sensor.setPulseAmplitudeRed(0x0A) # Turn Red LED to low to indicate sensor is running
	sensor.setPulseAmplitudeGreen(0) # Turn off Green LED

	RATE_SIZE = 4 # Increase this for more averaging. 4 is good.
	rates = list(range(RATE_SIZE)) # list of heart rates
	rateSpot = 0
	lastBeat = 0 # Time at which the last beat occurred
	beatsPerMinute = 0.00
	beatAvg = 0
	samplesTaken = 0 # Counter for calculating the Hz or read rate
	startTime = millis() # Used to calculate measurement rate
	count = 0
    
	while True:
                    
                irValue = sensor.getIR()
                samplesTaken += 1
                if sensor.checkForBeat(irValue) == True:
                    # We sensed a beat!
                    print('BEAT')
                    delta = ( millis() - lastBeat )
                    lastBeat = millis()	
            
                    beatsPerMinute = 60 / (delta / 1000.0)
                    beatsPerMinute = round(beatsPerMinute,1)
            
                    if beatsPerMinute < 255 and beatsPerMinute > 20:
                        rateSpot += 1
                        rateSpot %= RATE_SIZE # Wrap variable
                        rates[rateSpot] = beatsPerMinute # Store this reading in the array

                        # Take average of readings
                        beatAvg = 0
                        for x in range(0, RATE_SIZE):
                            beatAvg += rates[x]
                        beatAvg /= RATE_SIZE
                        beatAvg = round(beatAvg)
                
                Hz = round(float(samplesTaken) / ( ( millis() - startTime ) / 1000.0 ) , 2)
                if (samplesTaken % 200 ) == 0:
                                
                    print(\
                        'IR=', irValue , ' \t',\
                                    'BPM=', beatsPerMinute , '\t',\
                                                                                        #'DCE', getDCE() , '\t',\
                                    'Avg=', beatAvg , '\t',\
                        'Hz=', Hz, \
                        )
                
                count = count + 1
                print("Count :: ",count)
                if(count == 400):
                    #break
                    return irValue, beatsPerMinute, beatAvg, Hz  
                
    
    