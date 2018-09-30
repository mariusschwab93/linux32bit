The Memory_Map.pdf include the Memory Map. 

In the folder "image_LED" you find all scripts for the LCD-Display. 
In the folder "Toggle" you find all scripts for the Toggle excersise.

For the Toggle exercise you must "make". After that use the comand "cc -O3 -g  -o gpioThru gpioThru.c" and 
"cc -O3 -g  -o gpioToggle gpioToggle.c". Now you can run the gpioToggle with "./gpioToggle". Maybe you need the "sudo" comand. 
The LED on the Beagle is blinking.

The next step is to connect two buttons on the Beagle. I use the GPIO9_25 and GPIO9_23. 
Now you need the comand "cc -O3 -g  -o gpioToggle gpioToggle.c". Run it with "./gpioToggle". When you push a button, the LED on the Beagle is on.


In the folder image_LED you must run "install.sh" and "make".
If you want rotate a image, use the on.sh file with the rotate = 0. You see, that the picture is rotate of 90 degree. 
After that you use the comand of "sudo fbi -noverbose -T 1 -a boris.png". You see the picture on the screen 
(see at image 20180923_180140.jpg).

The same is with the video. Here you must use "./setup.sh."But the screen of the video is not the size of the LCD display. 
I hasn't adapt the video to the LCD display. 

When you run the text.sh, you can see my Name at the LCD Display. The picture is in the Folder (20180921_180928.jpg).
   
I two things in 'text.sh'. The first 'convert' command was edited so that it would display my name on the white background. 
The second convert command wrote the text 'tux' on the 'tux.png' image. The resulting image is 'append_label.jpg'. In order
to see the first image (my name written on a white background), you will have to comment out the second convert command.

I have not used pygame before so I did not run this on the display

========================
Professor Yoder's Comments

Looks good.
How does your toggle time compare with pervious times?

Score:  9/10