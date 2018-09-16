
#!/usr/bin/env python3
# Read a TMP101 sensor

import smbus
import time
bus = smbus.SMBus(2)
address1 = 0x48
address2 = 0x49


while True:
    temp1 = bus.read_byte_data(address1, 0)*(9/5)+32
    temp2 = bus.read_byte_data(address2, 0)*(9/5)+32

    print ('Temp1 in Fahrenheit:', temp1,'Temp2 in Fahrenheit', temp2, end="\r")
    time.sleep(0.25)
