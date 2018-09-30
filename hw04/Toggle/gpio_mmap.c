//This program uses the GPIO1 and GPIO3 registers along with mmap() to detect t$

#include <stdio.h>
#include <stdlib.h>
#include <sys/mman.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <signal.h>
#include "beaglebone_gpio.h"


#define GPIO1_START_ADDR 0x4804C000   //define Addresse of the GPIO1
#define GPIO1_END_ADDR 0x4804CFFF
#define GPIO1_SIZE (GPIO1_END_ADDR - GPIO1_START_ADDR)

#define GPIO3_START_ADDR 0x481AE000  //define Addresses of the GPIO3
#define GPIO3_END_ADDR 0x481AEFFF
#define GPIO3_SIZE (GPIO3_END_ADDR - GPIO3_START_ADDR)

#define USR2 (1<<23)

#define GPIO_SETDATAOUT 0x194
#define GPIO_CLEARDATAOUT 0x190
#define USR3 (1<<24)

#define GPIO_DATAIN 0x138

 

int main(int argc, char *argv[]){
volatile void *gpio1_addr;
volatile void *gpio3_addr;
volatile unsigned int *gpio1_setdataout_addr;
volatile unsigned int *gpio1_cleardataout_addr;
volatile unsigned int *gpio1_datain_addr;
volatile unsigned int *gpio3_setdataout_addr;
volatile unsigned int *gpio3_cleardataout_addr;
volatile unsigned int *gpio3_datain_addr;
int fd=open("/dev/mem", O_RDWR);

gpio1_addr = mmap(0, GPIO1_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO1_START_ADDR);
gpio3_addr = mmap(0, GPIO3_SIZE, PROT_READ | PROT_WRITE, MAP_SHARED, fd, GPIO3_START_ADDR);

gpio3_setdataout_addr=gpio3_addr+GPIO_SETDATAOUT;
gpio3_cleardataout_addr=gpio3_addr+GPIO_CLEARDATAOUT;
gpio3_datain_addr=gpio3_addr+GPIO_DATAIN;

gpio1_setdataout_addr = gpio1_addr+GPIO_SETDATAOUT;
gpio1_cleardataout_addr=gpio1_addr+GPIO_CLEARDATAOUT;
gpio1_datain_addr=gpio1_addr+GPIO_DATAIN;

while (1){

int gpio1Status;
int gpio3Status;

//Check for button presses in the gpio data register

gpio1Status = *gpio1_datain_addr >> 17;   //define the use of the GPIO Inputs with the shift operator
gpio1Status=gpio1Status & 0x01;
gpio3Status= *gpio3_datain_addr >> 21;
gpio3Status=gpio3Status & 0x01;

//The switches used pull down to ground, so only turn on the internal LEDs

if(gpio1Status==0){

*gpio1_setdataout_addr=USR3;

}

else{

*gpio1_cleardataout_addr=USR3;

}

if(gpio3Status==0){

*gpio1_setdataout_addr=USR2;

}

else{

*gpio1_cleardataout_addr=USR2;

}

}

}
