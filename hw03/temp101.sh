#!/bin/bash
for((;;))
do
#Read tmp101 at address 0x48
temp=`i2cget -y 2 0x48 0x00`
temp2=$(((temp*9/5)+32))
#echo "Temperature read from address 0x48 is" $temp2 "degrees Fahrenheit"

#Read tmp101 at address 0x49
temp3=`i2cget -y 2 0x49 0x00`
temp4=$(((temp3*9/5)+32))
echo "Temperature read from address 0x49 is" $temp4 "degrees Fahrenheit and adress 0x48 is " $temp2 "degrees Fahrenheit"
done
