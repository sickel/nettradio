#!/usr/bin/python

import time
import urllib2
import RPi.GPIO as GPIO

# TODO - use internal pulldowns or pullups and adjust code if needed

btnext=9
btback=10
btoff=11

GPIO.setmode(GPIO.BCM)
GPIO.setup(btnext,GPIO.IN)
GPIO.setup(btback,GPIO.IN)
GPIO.setup(btoff,GPIO.IN)

debug=True

prevnext=1
prevback=1
prevoff=1
url="http://localhost/index.php"
if debug:
  print "Ready"
while True:
  innext=GPIO.input(btnext)
  inback=GPIO.input(btback)
  inoff=GPIO.input(btoff)
  if(innext and innext!=prevnext):
    if debug:
        print("Button 9 pressed - next")
    urllib2.urlopen(url+"?browse=next")
  prevnext=innext
  if(inback and inback!=prevback):
    if debug:
      print("Button 10 pressed - prev")
    urllib2.urlopen(url+"?browse=prev")
  prevback=inback
  if(inoff and inoff!=prevoff):
    if debug:
      print("Button 11 pressed - off")
    urllib2.urlopen("http://localhost/radio.php?off=Av")
  prevoff=inoff
  time.sleep(0.05) # Debouncing
