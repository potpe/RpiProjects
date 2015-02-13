#include <wiringPi.h>
#include <stdio.h>

int main(void)
{
	int pin = 0;
	printf("LED blink on pin 0\n");

	/*
	  WIRINGPI SETUP USES WIRING PI ENUMERATION
	  wiringpisetupPhys - physical pins
	  wiringpisetupGPIO - native bcm (revision 1/2 issues)
	  wiringpisetupsYS -  uses gpio system level calls -> doesn't require root but gpio pins need to be exported (sys level calls uses native bcm enumeration)

	*/

	if(wiringPiSetup() == -1)
	{
		exit(1);
	}
	
	pinMode(pin, OUTPUT);

	for(;;)
	{
		printf("LED ON\n");
		digitalWrite(pin, 1);
		delay(2000);
		printf("LED OFF\n");
		digitalWrite(pin, 0);
		delay(2000);
	}

	return 0;

}
