#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

button1="P9_15"		#initializing of the buttons GPIO
button2="P9_16"
button3="P9_17"
button4="P9_18"

LED1="P9_11" 		#initializing of the LEDs GPIO
LED2="P9_12" 
LED3="P9_13" 
LED4="P9_14" 

GPIO.setup(LED1, GPIO.OUT) #define the LEDs as GPIO outputs
GPIO.setup(LED2, GPIO.OUT)
GPIO.setup(LED3, GPIO.OUT)
GPIO.setup(LED4, GPIO.OUT)

GPIO.setup(button1, GPIO.IN) #define the Buttons as GPIO inputs
GPIO.setup(button2, GPIO.IN)
GPIO.setup(button3, GPIO.IN)
GPIO.setup(button4, GPIO.IN)

map = {button1 : LED1, button2 : LED2, button3 : LED3, button4 : LED4}

def updateBoard(channel):			#update the status of the board 

	state = GPIO.input(channel)
  	GPIO.output(map[channel], state)


GPIO.add_event_detect(button1, GPIO.BOTH, callback=updateBoard)		#use the function event, so its only have a reaction if something happens. 
GPIO.add_event_detect(button2, GPIO.BOTH, callback=updateBoard)
GPIO.add_event_detect(button3, GPIO.BOTH, callback=updateBoard)
GPIO.add_event_detect(button4, GPIO.BOTH, callback=updateBoard)

try:
	while True:
    		time.sleep(100)

except KeyboardInterrupt:
	print("Cleaning Up")
  	GPIO.cleanup()
GPIO.cleanup()

#without the event function it is also possible the following:

#while True:
#       state1 = GPIO.input(button1)
#       state2 = GPIO.input(button2)
#       state3 = GPIO.input(button3)
#       state4 = GPIO.input(button4)    


#       GPIO.output(LED1, state1)
#       GPIO.output(LED2, state2)
#       GPIO.output(LED3, state3)
#       GPIO.output(LED4, state4)

