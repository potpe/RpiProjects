import RPi.GPIO as GPIO
import time
import signal
import sys

print "Rpi Revision: ",GPIO.RPI_REVISION
print "GPIO Version: ",GPIO.VERSION

#register ctrl+c handler for nice pin cleanup
def kill_handler(signal, frame):
    print "HANDLING PROCESS KILL"
    GPIO.cleanup()
    print "PINS CLEANED UP. BYE!"
    sys.exit(0)

# bind handler to handling routing
signal.signal(signal.SIGINT, kill_handler)    


#Modes: GPIO.BCM (BCM (broadcom) enumaration - rev1 vs rev2 are different)
#       GPIO.BOARD (physical pgpin numbers) => #1=3.3V, #2=5V, #6=GND

#pin = 12 #BCM_18 = BOARD_12 = GPIO1

#usable pins declaration in physical pin notation
p0 = 11
p1 = 12
p2 = 13
p3 = 15
p4 = 16
p5 = 18
p6 = 22
p7 = 7

GPIO.setmode(GPIO.BOARD)


#list of all pins
allPins = [p0,p1,p2,p3,p4,p5,p6,p7]
values = [0,0,0,0,0,0,0,0]

#init setup to false
print 'SETTING PINS TO 0:'
for pin in allPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

print "CYCLING:"

maxCycles = 1
cycleTime = 0.2
stripeWidth = 2 #1..8

cycles = 0
maxPin = len(allPins)
while cycles < maxCycles:
    for i in range(0, maxPin):
        #switch all off by default
        for pin in range(0, maxPin):
            values[pin] = 0
        
        for j in range(i,i+stripeWidth):
            values[j%maxPin] = 1 #switch on the one we want

        #set pins to values (avoid pin jitter)
        for pin in range(0, maxPin):
            GPIO.output(allPins[pin], values[pin])
            
        time.sleep(cycleTime)
    cycles += 1

print "ENDING"
GPIO.cleanup()

