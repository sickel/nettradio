#!/usr/bin/python

import time
import urllib2
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(9,GPIO.IN)
GPIO.setup(10,GPIO.IN)
GPIO.setup(11,GPIO.IN)

debug=False

prev9=1
prev10=1
prev11=1
url="http://localhost/index.php"

print "Ready"
while True:
  in9=GPIO.input(9)
  in10=GPIO.input(10)
  in11=GPIO.input(11)
  if(in9 and in9!=prev9):
    if Debug:
        print("Button 9 pressed - next")
    urllib2.urlopen(url+"?browse=next")
  prev9=in9
  if(in10 and in10!=prev10):
    if Debug:
      print("Button 10 pressed - prev")
    urllib2.urlopen(url+"?browse=prev")
  prev10=in10
  if(in11 and in11!=prev11):
    if Debug:
      print("Button 11 pressed - off")
    urllib2.urlopen("http://localhost/radio.php?off=Av")
  prev11=in11
  time.sleep(0.05)
