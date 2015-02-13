import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.output(11, True)
print "ON"
time.sleep(10)

GPIO.output(11, False)
print "OFF"

