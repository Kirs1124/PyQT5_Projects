import sys
from time import sleep
import hw4_2
LED4_PATH = "/sys/class/gpio/gpio4/"
SYSFS_DIR = "/sys/class/gpio/"

LED_NUMBER = "4"

delay_time = 0
close_time = 0

def writeLED(filename, value, path= LED4_PATH):
    fo = open(path+filename,"w")
    fo.write(value)
    fo.close()
    return

print("Starting the GPIO LED4 Python script")

if len(sys.argv) != 2:
    print("There is an incorrect number of arguments")
    print("usage is: pythonLED.py command")
    print("where command is one of setup, on, off, status, or close")
    sys.exit(2)

if sys.argv[1] == "on":
    sleep(delay_time)
    print("Turning the LED on")
    writeLED(filename="value", value=1)
elif sys.argv[1] == "off":
    print("Turning the LED off")
    writeLED(filename="value", value=0)
elif sys.argv[1] == "setup":
    print("Setting up the LED GPIO")
    writeLED(filename="export", value=LED_NUMBER,path=SYSFS_DIR)
    sleep(0.1)
    writeLED(filename="direction", value="out")
    delay_time = int(input("请输入延迟时间："))
    close_time = int(input("请输入关闭时间："))
elif sys.argv[1] == "close":
    print("Closing down the LED GPIO")
    writeLED(filename="unexport", value=LED_NUMBER, path=SYSFS_DIR)
elif sys.argv[1] == "status":
    print("Getting the LED state value")
    fo = open(LED4_PATH + "value","r")
    print(fo.read())
    fo.close()
elif sys.argv[1] == "Change_brightness":
    hw4_2.change_brightness()
else:
    print("Invalid Command!")
print("End of Python script")