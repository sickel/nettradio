#!/usr/bin/python
import time

while True:
   f=open('/tmp/radiotitle',"r")

   lastline=''
   for line in iter(f):
      if len(line) > 1:
         lastline=line         
   print lastline
   time.sleep(5)

    
