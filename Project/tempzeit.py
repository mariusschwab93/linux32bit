from Tkinter import *
import time
#import tmp102

import smbus
import time
bus = smbus.SMBus(2)
#address1 = 0x48
address2 = 0x49


#while True:
 #   temp1 = bus.read_byte_data(address1, 0)*(9/5)+32
temp = bus.read_byte_data(address2, 0)*(9/5)+32
#temp2 = bus.read_byte_data(address2, 0)*(9/5)+32

#print ('Temp2 in Fahrenheit', temp2)
#return temp2

root = Tk()
l = Label( root, text=temp)
l.pack()
root.update()

while True:
        temp = bus.read_byte_data(address2, 0)*(9/5)+32
        #print ('Temp in Fahrenheit', temp, end="\r" )
        print ('Temp in Fahrenheit', temp)



       # time.sleep( 1 )
        l[ "text" ]=temp
        root.update()
#
mainloop()

