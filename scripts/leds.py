"""
This library provides basic functions to turn the
LED-lights on and off. Please be careful, not to turn the LEDs on for too
long, as the transistors might overheat!
"""

import RPi.GPIO as GPIO

_whitePort = 14
_redPort = 15
_irPort = 18
_PWMFreq = 420


GPIO.setmode(GPIO.BCM)
GPIO.setup(_whitePort, GPIO.OUT)
GPIO.setup(_redPort, GPIO.OUT)
GPIO.setup(_irPort, GPIO.OUT)
GPIO.setwarnings(False)
whitePWM = GPIO.PWM(_whitePort, _PWMFreq)
redPWM = GPIO.PWM(_redPort, _PWMFreq)
irPWM = GPIO.PWM(_irPort, _PWMFreq)


def setRed(brightness):
    """
    self explanatory
    """
    redPWM.ChangeDutyCycle(brightness)


def setIR(brightness):
    irPWM.ChangeDutyCycle(brightness)


def setWhite(brightness):
    whitePWM.ChangeDutyCycle(brightness)


def initLEDs():
    """
    starts the PWM Processes for the LEDs
    """
    whitePWM.start(0)
    redPWM.start(0)
    irPWM.start(0)
