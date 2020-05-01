#!/usr/bin/python
  
import time
import urllib2
import RPi.GPIO as GPIO
import os
import syslog


debug=os.environ.get('DEBUG_BUTTONSPY')=='debugthis'

# TODO - use internal pulldowns or pullups and adjust code if needed
bt= {}
prevval={}

bt[9]='browse=next'
bt[10]='browse=prev'
bt[11]='off=Toggle'

GPIO.setmode(GPIO.BCM)
for btn in bt:
  GPIO.setup(btn,GPIO.IN)
  prevval[btn]=0

url="http://localhost/index.php?"

def read_buttons():
  if debug:
    syslog.syslog("Ready")
  while True:
    for btn in bt:
      value=GPIO.input(btn)
      if(value and value!=prevval[btn]):
        if debug:
          syslog.syslog("Button {} pressed - {}".format(btn,bt[btn]))
        else:
          urllib2.urlopen(url+bt[btn])
      prevval[btn]=value
    time.sleep(0.1) # Debouncing
