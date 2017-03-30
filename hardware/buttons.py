#!/usr/bin/python

import time
from subprocess import call
import urllib2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(11,GPIO.IN)

prev9=1
prev10=1
prev11=1

print "Ready"
while True:
  in9=GPIO.input(9)
  in10=GPIO.input(10)
  in11=GPIO.input(11)
  if(in9 and in9!=prev9):
    print("Button 9 pressed - next")
    urllib2.urlopen("http://localhost/radio.php?browse=next")
    #call(["wget","-q","--output-document=/dev/null","localhost/radio.php?browse=next"],shell=True)
  prev9=in9
  if(in10 and in10!=prev10):
    print("Button 10 pressed - prev")
    urllib2.urlopen("http://localhost/radio.php?browse=prev")
    #call(["wget","-q -O /dev/null localhost/radio.php?browse=next"],shell=True)
  prev10=in10
  if(in11 and in11!=prev11):
    print("Button 11 pressed - off")
    urllib2.urlopen("http://localhost/radio.php?off=Av")
  prev11=in11
  time.sleep(0.05)
