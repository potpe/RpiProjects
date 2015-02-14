import RPi.GPIO as GPIO;
import pygame.mixer;

pygame.mixer.init();
#PIN 3(BOARD) = PIN 2 (BCM)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

#Load sounds from preset samples
drum = pygame.mixer.Sound("samples/drum_tom_mid_hard.wav");
cymbal = pygame.mixer.Sound("samples/drum_cymbal_open.wav");
bell = pygame.mixer.Sound("samples/elec_bell.wav");
snare = pygame.mixer.Sound("samples/elec_hi_snare.wav");

#dictionary
sound_pins = {
    2: drum,
    3: cymbal
}

#core playing
def play(pin):
    print("playing %s" % pin);
    sounds_pins[pin].play();

#pin and event setup
for pin in sound_pins:
    GPIO.setup(pin, GPIO.IN, GPIO.PUD_DOWN);
    GPIO.add_event_detect(pin, GPIO.FALLING, play, 1000);

while True:
    pass;
