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

import Adafruit_Nokia_LCD as LCD
import Adafruit_GPIO.SPI as SPI

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont


# Raspberry Pi hardware SPI config:
DC = 23
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

# Raspberry Pi software SPI config:
# SCLK = 4
# DIN = 17
# DC = 23
# RST = 24
# CS = 8

# Beaglebone Black hardware SPI config:
# DC = 'P9_15'
# RST = 'P9_12'
# SPI_PORT = 1
# SPI_DEVICE = 0

# Beaglebone Black software SPI config:
# DC = 'P9_15'
# RST = 'P9_12'
# SCLK = 'P8_7'
# DIN = 'P8_9'
# CS = 'P8_11'


# Hardware SPI usage:
disp = LCD.PCD8544(DC, RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=4000000))

# Software SPI usage (defaults to bit-bang SPI interface):
#disp = LCD.PCD8544(DC, RST, SCLK, DIN, CS)


def getlast():
  "Get last text of interest from mp3 output"
  lastline=''
  try:
    f=codecs.open('/tmp/radiotitle',encoding="utf-8")
    for line in iter(f):
      if len(line) > 1:
         lastline=line
    splt=lastline.split('=')
#  print(splt)
    if len(splt)>0:
      return splt[1].strip("'")
  except:
     lastline=""
  return(lastline)

# Initialize library.
disp.begin(contrast=60)

# Clear display.
disp.clear()
disp.display()
#font = ImageFont.load_default()
font = ImageFont.truetype('Economica-Regular-OTF.ttf', 11)
def showtext():
  # Create blank image for drawing.
  # Make sure to create image with mode '1' for 1-bit color.
  image = Image.new('1', (LCD.LCDWIDTH, LCD.LCDHEIGHT))
  # Get drawing object to draw on image.
  draw = ImageDraw.Draw(image)
  # Draw a white filled box to clear the image.
  draw.rectangle((0,0,LCD.LCDWIDTH,LCD.LCDHEIGHT), outline=255, fill=255)
  ch="/var/www/html/ch.txt"
  try:
    f=codecs.open(ch,encoding="utf-8")
    chname=f.readline()
  except:
    chname=""
  draw.text((1,1),chname,font=font)
  txt=getlast().split('med')
  # Write some text.
  draw.text((1,20),txt[0], font=font)
  if len(txt) > 1:
     txt[1].strip(" ")
     draw.text((1,30),txt[1], font=font)
  #draw.text((6,8), 'test 2 - 6,8', font=font)
  # Display image.
  disp.image(image)
  disp.display()

print 'Press Ctrl-C to quit.'
while True:
   showtext()
   time.sleep(5)
