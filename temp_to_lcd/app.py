from ADCDevice import *
from LCD1602 import CharLCD1602
import math
import time

lcd1602 = CharLCD1602()  

def setup():
    global adc
    if(adc.detectI2C(0x48)): # Detect the pcf8591.
        adc = PCF8591()
    elif(adc.detectI2C(0x4b)): # Detect the ads7830
        adc = ADS7830()
    else:
        print("No correct I2C address found, \n"
        "Please use command 'i2cdetect -y 1' to check the I2C address! \n"
        "Program Exit. \n");
        exit(-1)

def displayTemp(temp):
    lcd1602.clear()
    lcd1602.write( 0, 0, "Temperature: " )
    lcd1602.write( 0, 1, temp )

def getTemp():
    value = adc.analogRead(0)
    voltage = value / 255.0 * 3.3
    Rt = 10 * voltage / (3.3 - voltage)
    tempK = 1/(1/(273.15 + 25) + math.log(Rt/10)/3950.0)
    tempC = tempK -273.15
    return str(tempC)
    
def loop():
    lcd1602.init_lcd()
    while True:
        tempString = getTemp()
        displayTemp(tempString)
        time.sleep(0.01)

def destroy():
    adc.close()
    lcd1602.clear()
    
if __name__ == '__main__':  # Program entrance
    print ('Program is starting ... ')
    setup()
    try:
        loop()
    except KeyboardInterrupt: # Press ctrl-c to end the program.
        destroy()
        print("Ending program")