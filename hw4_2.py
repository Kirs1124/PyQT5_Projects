import RPi.GPIO as GPIO
import time

def change_brightness():
    GPIO.setmode(GPIO.wpi)
    GPIO.setup(4, GPIO.OUT)
    pwm = GPIO.PWM(4, 100)
    pwm.start(0)
    time.sleep(5)
    pwm.ChangeDutyCycle(20)
    time.sleep(5)
    pwm.stop()
    GPIO.cleanup()
