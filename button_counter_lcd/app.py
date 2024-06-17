from gpiozero import Button

button = Button(17)

count = 0

def whenButtonPressed():
    count += 1
    print("Button is pressed, count is #{count}")


def loop():
    while(True):
        button.when_pressed = whenButtonPressed

def destroy():
    button.close()

if __name__ == '__main__':
    print ('Program is starting ... ') 
    try:
        loop()
    except KeyboardInterrupt:  # Press ctrl-c to end the program.
        destroy()
        print("Ending program")