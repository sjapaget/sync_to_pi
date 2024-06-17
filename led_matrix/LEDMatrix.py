#!/usr/bin/env python3
#############################################################################
# Filename    : LEDMatrix.py
# Description : Control LEDMatrix with 74HC595
# auther      : www.freenove.com
# modification: 2023/05/15
########################################################################
from gpiozero import OutputDevice
import time

LSBFIRST = 1
MSBFIRST = 2
# define the pins connect to 74HC595
dataPin   = OutputDevice(17)      # DS Pin of 74HC595(Pin14)
latchPin  = OutputDevice(27)      # ST_CP Pin of 74HC595(Pin12)
clockPin  = OutputDevice(22)      # CH_CP Pin of 74HC595(Pin11)
pic = [0x1c,0x22,0x51,0x45,0x45,0x51,0x22,0x1c]
    
def shiftOut(order,val):
    for i in range(0,8):
        clockPin.off()
        if(order == LSBFIRST):
            dataPin.on() if (0x01&(val>>i)==0x01) else dataPin.off()
        elif(order == MSBFIRST):
            dataPin.on() if (0x80&(val<<i)==0x80) else dataPin.off()
        clockPin.on()

def loop():
    while True:
        for j in range(0,500): # Repeat enough times to display the smiling face a period of time
            x=0x80
            for i in range(0,8):
                latchPin.off()
                shiftOut(MSBFIRST,pic[i]) #first shift data of line information to first stage 74HC959

                shiftOut(MSBFIRST,~x) #then shift data of column information to second stage 74HC959
                latchPin.on()         # Output data of two stage 74HC595 at the same time
                time.sleep(0.001) # display the next column
                x>>=1 
def destroy():  
    dataPin.close()
    latchPin.close()
    clockPin.close()
if __name__ == '__main__':  # Program entrance
    print ('Program is starting...' )
    try:
        loop()  
    except KeyboardInterrupt:   # Press ctrl-c to end the program.
        destroy()
        print("Ending program")

