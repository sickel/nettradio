#!/usr/bin/python
# Copyright (c) 2014 Adafruit Industries
# Author: Tony DiCola
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
import codecs
from mikezlcd import *
lcd = lcd_module(2004, 17, 4, 25, 24, 23,22)
lcd.disp(0,3,"<-     ->       off ")
clearline="                    "


def getlast():
  "Get last text of interest from mp3 output"
  lastline=''
  try:
    f=codecs.open('/tmp/radiotitle',encoding="utf-8")
    for line in iter(f):
      if len(line) > 1:
         lastline=line
    lastline=lastline[:-3]
    splt=lastline.split('=')
#  print(splt)
    if len(splt)>0:
       
      return splt[1].strip("'")
  except:
     lastline=""
  return(lastline)


def showtext():
  
  ch="/var/www/html/ch2.txt"
  try:
    f=codecs.open(ch,encoding="utf-8")
    chname=f.readline()
  except:
    chname=""
  lcd.disp(0,0,clearline)
  lcd.disp(0,0,chname[:20])
  txt=getlast().split('med')
  # Write some text.
  lcd.disp(0,1,clearline)
  lcd.disp(0,1,txt[0][:20])
  lcd.disp(0,2,clearline)
  if len(txt) > 1:
     txt[1].strip(" ") 
     lcd.disp(0,2,txt[1][:20])

print 'Press Ctrl-C to quit.'
while True:
   lcd.disp(0,3,"<-     ->       off")
   showtext()
   time.sleep(5)
