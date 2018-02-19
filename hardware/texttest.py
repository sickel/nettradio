#!/usr/bin/python
# Copyright (c) 2017 Morten Sickel
# 
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import time
import datetime
import os.path
import codecs
from mikezlcd import *
lcd = lcd_module(2004, 17, 4, 25, 24, 23,22)
lcd.disp(0,3,"<-     ->       off ")
oldchname=""
oldtext=""


def getlast():
  "Get last text of interest from mp3 output"
  lastline=''
  try:
    f=codecs.open('/tmp/radiotitle',encoding="utf-8")
    for line in iter(f):
      if len(line) > 1:
         lastline=line
    lastline=lastline[:-3]
    if "/usr/bin/jackd" in lastline:
    # happens when changing canal
       return("")
    splt=lastline.split('=')
    #  print(splt)
    if len(splt)>0:
       
      return splt[1].strip("'")
  except:
     lastline=""
  return(lastline)

idx=0
def showtext():
  # todo scroll text
  # Check if unchanged if so, scroll one char to left. If last char is shown, start from first 
  global oldchname
  global oldtext
  global idx
  ch="/var/www/html/ch2.txt"
  try:
    f=codecs.open(ch,encoding="utf-8")
    chname=f.readline()
  except:
    chname=""
  if chname!=oldchname:
     lcd.disp(0,0,chname[:20].ljust(20))
     # clears display if changed channel
     lcd.disp(0,1," ".ljust(20))
     lcd.disp(0,2," ".ljust(20))
  oldchname=chname
  filetext=getlast()
  txt=filetext.split('med')
  if filetext!=oldtext:
     idx=0
     lcd.disp(0,1,txt[0][:20].ljust(20))
     if len(txt) > 1:
        txt[1].strip(" ") 
        lcd.disp(0,2,txt[1][:20].ljust(20))
     else:
        lcd.disp(0,2," ".ljust(20))
  oldtext=filetext
  if len(txt[0])>20:
     lcd.disp(0,1,txt[0][idx:20+idx])
#     print(txt[0][idx:20+idx])
     if idx+20<len(txt[0]):
        idx=idx+3
     else:
        idx=0
     

while True:
   now=datetime.datetime.now()
   lcd.disp(0,3,"<-  ->  off".ljust(20))
   lcd.disp(15,3,str(now.hour))
   lcd.disp(17,3,":")
   lcd.disp(18,3,str(now.minute))
   if os.path.isfile("/tmp/radiopid"):
      showtext()
   else:
      lcd.disp(0,0," ".ljust(20))
      lcd.disp(0,1," ".ljust(20))
      lcd.disp(0,2," ".ljust(20))
   time.sleep(1)
