from time import sleep
from gpiozero import Button
from LCD1602 import CharLCD1602

button = Button(17)
lcd1602 = CharLCD1602()  

count = 0

def whenButtonPressed():
    global count 
    count += 1
    print(f"Button is pressed, count is {count}")


def loop():
    while(True):
        button.when_pressed = whenButtonPressed
        lcd1602.clear()
        lcd1602.write(0, 0, 'Button Presses:' )
        global count
        lcd1602.write(0, 1, str(count) )
        sleep(1)

def destroy():
    button.close()

if __name__ == '__main__':
    print ('Program is starting ... ') 
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")