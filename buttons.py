#!/usr/bin/python

import time
from subprocess import call
import urllib2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.IN)
GPIO.setup(22,GPIO.IN)
prev17=0
prev22=0

print "Ready"
while True:
  in17=GPIO.input(17)
  in22=GPIO.input(22)
  if(in17 and in17!=prev17):
    print("Button 17 pressed - next")
    urllib2.urlopen("http://localhost/radio.php?browse=next")
    #call(["wget","-q","--output-document=/dev/null","localhost/radio.php?browse=next"],shell=True)
  prev17=in17
  if(in22 and in22!=prev22):
    print("Button 22 pressed - prev")
    urllib2.urlopen("http://localhost/radio.php?browse=prev")
    #call(["wget","-q -O /dev/null localhost/radio.php?browse=next"],shell=True)
  prev22=in22
  time.sleep(0.05)
