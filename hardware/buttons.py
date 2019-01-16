#!/usr/bin/python
  
import time
import urllib2
import RPi.GPIO as GPIO

# TODO - use internal pulldowns or pullups and adjust code if needed
bt= {}
prevval={}


bt[9]='browse=next'
bt[10]='browse=prev'
bt[11]='off=Av'

GPIO.setmode(GPIO.BCM)
for btn in bt:
  GPIO.setup(btn,GPIO.IN)
  prevval[btn]=0
  
debug=False

url="http://localhost/index.php?"

if debug:
  print "Ready"
while True:
  for btn in bt:
    value=GPIO.input(btn)
    if value:
      print btn,value
    if(value and value!=prevval[btn]):
      if debug:
        print("Button {} pressed - {}").format(btn,bt[btn])
      else:
        urllib2.urlopen(url+bt[btn])
      prevval[btn]=value
  time.sleep(0.05) # Debouncing
