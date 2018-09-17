To run the python script use the comand of "python". Maybe if you run with the comand of "chmod +x" and "./" there is a
TabError: inconsistent use of tabs and spaces in indentation. 

If the Beaglebone booted new and you use the P8_41 and P8_42 for the encoders, you must run a setup.sh file. 
Here is the path: ~/BeagleBoard-exercises/sensors/eQEP$ 
You also musst install the smbus.(Look at the install.sh) 

With the shell of temp101.sh you can read two temperaturs.
The same you can do with the script temp101.py.
 Connect the sensors to the i2c-Bus, like in the Lecture. Should it not work, 
trie it without the Pull up resistors. The value is print in Fahrenheit. 


With the script of etch88LED.py you can play the game at the 8x8 LEDmatrix. You need four buttons for up/down and left/right, one button 
to quit the game and one button to  clear the matrix. 

With the script of etch88LEDencoder.py you can play the game also at the 8x8 LEDmatrix.
You need 2 Encoders for Up/Down and Left/Right. 
One button to quite the game and one button to clear the matrix.

I have done all three tasks. 
