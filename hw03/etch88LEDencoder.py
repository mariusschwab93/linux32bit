#!/usr/bin/env python3
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import Adafruit_BBIO.GPIO as GPIO
import curses
import time
import smbus
import math

myEncoder = RotaryEncoder(eQEP1)
myEncoder.setAbsolute()
myEncoder.enable()


myEncoder2 = RotaryEncoder(eQEP2)
myEncoder2.setAbsolute()
myEncoder2.enable()

bus = smbus.SMBus(2)  #use the i2c bus 2
matrix=0x70
bus.write_byte_data(matrix, 0x0000, 2)


#Matrix setup
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

wireboard=[0x01, 0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
	0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

bus.write_i2c_block_data(matrix, 0, wireboard)

#Track of the current index
currentIndex=1

#Vertical position and the current column on the 8x8 matrix
yPos=1

y1=1
y2=2
y3=3
y4=4
y5=5
y6=6
y7=7
y8=8
y9=9

b1=1
b2=2
b3=4
b4=8
b5=16
b6=32
b7=64
b8=128
b9=256

#This maps column positions to binary values so that the correct pixels will light up as you move around the display
map={y1:b1,y2:b2,y3:b3,y4:b4,y5:b5,y6:b6,y7:b7,y8:b8,y9:b9}

#GPIOs initialization
button1="P9_13"
button2="P9_14"


#initialization the Buttons as GPIO outputs
GPIO.setup(button1, GPIO.IN)
GPIO.setup(button2, GPIO.IN)

playGame=True #True until the user use q on the keyboard

#Detect button and change curser position
def updateBoard(channel):
	global button1
	global button2
	global wireboard
	global currentIndex
	global yPos
	global playGame


	#clear the matrix
	if channel == button1:
		wireboard=[0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        		0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		bus.write_i2c_block_data(matrix, 0, wireboard)
		currentIndex=1
		yPos=1

	#stop the game
	elif channel == button2:
		playGame=False



#use a event for the buttons
GPIO.add_event_detect(button1, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(button2, GPIO.RISING, callback=updateBoard)

# set the old encoder value to zero
olde1 = 0
olde2 = 0

while playGame:
	time.sleep(0.1) #sleep time, without the sleep time is the program to fast a run to much pixel at the matrix

	myEncoderPos = myEncoder.position    #update the encoder position 1 and 2
	myEncoder2Pos = myEncoder2.position



	if myEncoderPos < olde1:    #go down

		if yPos!=8:
			yPos+=1 #This increases to keep track of where you are in the column
			wireboard[currentIndex-1]=map[yPos] #Changes the users current position to yellow
			wireboard[currentIndex]=wireboard[currentIndex] | map[yPos] #Or the correct binary value with the i2c data for the cu$
			bus.write_i2c_block_data(matrix, 0, wireboard)




	elif myEncoderPos > olde1:                        #go up
                if yPos!=1:
                        yPos-=1
                        wireboard[currentIndex-1]=map[yPos]
                        wireboard[currentIndex-1]=wireboard[currentIndex-1] & map[yPos]
                        wireboard[currentIndex]=wireboard[currentIndex] | map[yPos]
			bus.write_i2c_block_data(matrix, 0, wireboard)


	elif myEncoder2Pos < olde2:		#go right
                if currentIndex!=15:
                        wireboard[currentIndex-1]=0
                        currentIndex+=2
                        wireboard[currentIndex-1]=map[yPos]
                        wireboard[currentIndex]=wireboard[currentIndex] | map[yPos]
			bus.write_i2c_block_data(matrix, 0, wireboard)




	elif myEncoder2Pos > olde2:                        #go left
                if currentIndex!=1:
                        wireboard[currentIndex-1]=0
                        currentIndex-=2
                        wireboard[currentIndex-1]=map[yPos]
                        wireboard[currentIndex]=wireboard[currentIndex] | map[yPos]
			bus.write_i2c_block_data(matrix, 0, wireboard)



	olde1 = myEncoderPos
	olde2 = myEncoder2Pos

