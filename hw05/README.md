Project:
Done. I'am in the list.

make:
You can run the makefile with the comand "bone$ make". It build an 
app.arm. Run the app.arm wirht "bone$ ./app.arm" you will see 
"Hello World". I done part 1 and 2. 

Installing the Kernel Source: 
I done it with step 1.

Cross-Compiling:
Done. You can run the a.out file with "host$ ./a.out". I compiled the file on the host and send the executable arm file to the bone. 
Now I can run the arm file from the host, who is on the bone.   

Kernel-Modules:
For this excercise you go to run the install.sh file with "bone$ ./install.sh".
Now you can go into the folder "Kernel_Modules". There you see three different folders. At fist you go into the folder "hello". 
Use the comand "make", you can execute the Kernel model. 
Now use "sudo insmod hello.ko" and it runs. Quit it with "sudo rmmod hello". 
If you want see somemoreyou can use the following comands: "bone$ sudo bash", bone$ cd /var/log/ and "bone$ tail -f kern.log"

In the folder of the "gpio_test" you can use a button and led with the kernel. I use the GPIO9_15 for the LED  and GPIO9_16 for the button.
Use the comand "make", after that "sudo insmod gpio_test.ko". If you push the button the Led is going to high. Quit it with 
"sudo rmmod gpio_test". 

The "ebbchar" folder is a LKM to communicate with the Kernel. This is the result of the tutorial part 2 from Molloy.  

========================
Professor Yoder's Comments

Looks good.  

I don't see where you compiled a new kernel and got it installed.

Score:  8/10
