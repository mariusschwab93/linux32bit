#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import curses
import time
import smbus
import math

#GRID_SIZE = int(input("size: "))  #The etch-a-sketch dimensions will be size x $

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

blk1=1
blk2=2
blk3=4
blk4=8
blk5=16
blk6=32
blk7=64
blk8=128
blk9=256

#This maps column positions to binary values so that the correct pixels will light up as you move around the display
map={y1:blk1,y2:blk2,y3:blk3,y4:blk4,y5:blk5,y6:blk6,y7:blk7,y8:blk8,y9:blk9}

#GPIOs initialization
Button1="P9_15"
Button2="P9_16"
Button3="P9_17"
Button4="P9_18"
Button5="P9_13"
Button6="P9_14"


#initialization the Buttons as GPIO outputs
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)
GPIO.setup(Button5, GPIO.IN)
GPIO.setup(Button6, GPIO.IN)

playGame=True #True until the user quits the game

#Detect button pushes and change curser position
def updateBoard(channel):
        global Button1
        global Button2
        global Button3
        global Button4
	global Button5
	global Button6
	global wireboard
	global currentIndex
	global yPos
	global playGame

        time.sleep(0.3)

        if channel == Button1:
		if yPos!=8:
			yPos+=1 #This increases to keep track of where you are in the column
			wireboard[currentIndex-1]=map[yPos] #Changes the users current position to yellow
			wireboard[currentIndex]=wireboard[currentIndex] | map[yPos] #Or the correct binary value with the i2c data for the current column. Oring this value allows the users trail to be left 
			bus.write_i2c_block_data(matrix, 0, wireboard)


        elif channel == Button2:                        #go up
		if yPos!=8:
			yPos-=1 #This increases to keep track of where you are in the column
			wireboard[currentIndex-1]=map[yPos] #Changes the users current position to ye
			wireboard[currentIndex-1]=wireboard[currentIndex-1] & map[yPos]			
			wireboard[currentIndex]=wireboard[currentIndex] | map[yPos] #Or the correct binary value with the i2c data for the current column. Oring this value allows the users trail to be left 
			bus.write_i2c_block_data(matrix, 0, wireboard)
	elif channel == Button3:
		if currentIndex!=15:
			wireboard[currentIndex-1]=0
			currentIndex+=2
			wireboard[currentIndex-1]=map[yPos]
			wireboard[currentIndex]=wireboard[currentIndex] | map[yPos]
			bus.write_i2c_block_data(matrix, 0, wireboard)                        #go right


        elif channel == Button4:                        #go left
		if currentIndex!=1:
			wireboard[currentIndex-1]=0
			currentIndex-=2
			wireboard[currentIndex-1]=map[yPos]
			wireboard[currentIndex]=wireboard[currentIndex] | map[yPos]
			bus.write_i2c_block_data(matrix, 0, wireboard)

	elif channel == Button5:
		wireboard=[0x01, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
        		0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
		bus.write_i2c_block_data(matrix, 0, wireboard)
		currentIndex=1
		yPos=1

	elif channel == Button6:
		playGame=False

time.sleep(0.03)


GPIO.add_event_detect(Button1, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button4, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button5, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button6, GPIO.RISING, callback=updateBoard)


while playGame:
	time.sleep(0.3)
