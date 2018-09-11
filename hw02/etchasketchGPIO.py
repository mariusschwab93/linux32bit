#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import curses
import time

GRID_SIZE = int(input("size: "))  #The etch-a-sketch dimensions will be size x size

#GPIOs initialization
Button1="P9_15"
Button2="P9_16"
Button3="P9_17"
Button4="P9_18"

#initialization the Buttons as GPIO outputs
GPIO.setup(Button1, GPIO.IN)
GPIO.setup(Button2, GPIO.IN)
GPIO.setup(Button3, GPIO.IN)
GPIO.setup(Button4, GPIO.IN)

SPACING = 1 #Spacing between etch-a-sketch characters
stdscr = curses.initscr() #Initialization for the curses import
curses.noecho()
curses.cbreak()

position_x=0 #Give the actually position while the game
position_y=0
xnum = 1 #Used for the etch-a-sketch boundaries
ynum = 1

stdscr.addstr(position_y,position_x,'X') #Used to add an X to current position
playGame=True #True until the user quits the game

#Detect button pushes and change curser position
def updateBoard(channel):
	global Button1
	global Button2
	global Button3
	global Button4
	global ynum
	global xnum
	global GRID_SIZE
	global position_y
	global position_x
	global SPACING
	
	time.sleep(0.03)

	if channel == Button1:
		if ynum!=1:				#go down
			position_y = position_y - SPACING
			stdscr.addstr(position_y, position_x, "X")
			stdscr.refresh()
			ynum=ynum-1

	elif channel == Button2:			#go up
		if ynum != GRID_SIZE:
			position_y=position_y+SPACING
			stdscr.addstr(position_y, position_x, "X")
			ynum=ynum+1
			stdscr.refresh()

	elif channel == Button3:			#go right
		if xnum != 1:
			position_x=position_x-SPACING
			stdscr.addstr(position_y, position_x, "X")
			xnum = xnum-1
			stdscr.refresh()

	elif channel == Button4:			#go left
		if xnum!=GRID_SIZE:
			position_x=position_x + SPACING
			stdscr.addstr(position_y, position_x, "X")
			stdscr.refresh()
			xnum=xnum+1
	time.sleep(0.03)


GPIO.add_event_detect(Button1, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button2, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button3, GPIO.RISING, callback=updateBoard)
GPIO.add_event_detect(Button4, GPIO.RISING, callback=updateBoard)

try:
	while playGame:
		c=stdscr.getch() #Get keyboard input

		if c== ord('q'):
			playGame=False

		elif c== ord('c'):
			stdscr.clear()
			position_x=0
			position_y=0
			xnum=1
			ynum=1	
			stdscr.addstr(position_y, position_x, "X")

except KeyboardInterrupt:
	GPIO.cleanup()

curses.endwin()



