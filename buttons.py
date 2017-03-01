#!/usr/bin/python

import time

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(22,GPIO.IN)
prev17=0
prev22=0


while True:
  in17=GPIO.input(17)
  in22=GPIO.input(22)
  if(in17 and in17!=prev17):
    print("Button 17 pressed")
  prev17=in17
  if(in22 and in22!=prev22):
    print("Button 22 pressed")
  prev22=in22
  time.sleep(0.05)
