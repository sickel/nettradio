#!/usr/bin/python
#
# charlcd.py
#
# Nov.11/2014: v1.00 released
#
# HD44780 and compatible character LCD module Python library
# for the Raspberry Pi. Please see URL below for the introductory article.
#
# http://www.mikronauts.com/raspberry-pi/raspberry-pi-1602-and-2004-lcd-interfacing/
#
# Copyright 2014 William Henning
# http://Mikronauts.com
#
# supports multiple character LCD modules simultaneously, requires unique 'E'
# clock signal per module, RS, D7, D6, D5, D4 can be shared between modules.
#
# tested with: 16x2, 20x4
#
# should also work unchanged with: 8x1, 8x2, 16x1, 20x1, 20x2
#
 
import RPi.GPIO as GPIO
import time
 
class lcd_module:
 
  lines = (0x80, 0xC0, 0x94, 0xD4)
  delay = 0.00001

  # output a nibble followed by E strobe 
  def nib(self, val):
    GPIO.output(self.d7, val&8)
    GPIO.output(self.d6, val&4)
    GPIO.output(self.d5, val&2)
    GPIO.output(self.d4, val&1)
    time.sleep(self.delay)
    GPIO.output(self.e, 1)
    time.sleep(self.delay)
    GPIO.output(self.e, 0)
    time.sleep(self.delay)

  # output a command byte
  def cmd(self, command):
    GPIO.output(self.rs, 0)
    self.nib(command>>4)
    self.nib(command&15)
    # allow for 1ms to execute the command
    time.sleep(0.001) 
  
  # output a character
  def chr(self, character):
    GPIO.output(self.rs, 1)
    self.nib(character>>4)
    self.nib(character&15)
 
  # clear the screen
  def cls():
    self.cmd(0x01)

  # set the cursor location to 0,0
  def home():
    self.cmd(0x02)

  # set the cursor location to x,y    
  def setxy(self,x,y):
    self.cmd(self.lines[y]+x)

  # output a string at the current cursor location      
  def str(self, message):
    for i in range(0,len(message)):
      self.chr(ord(message[i]))

  # set the cursor location, and output string
  def disp(self, x, y, message):
    self.setxy(x,y)
    self.str(message)

  # output an integer value
  def dec(self,val):
    self.str('%(v)d' % {"v": val})
      
  # output an integer value as an octal number
  def oct(self,val):
    self.str('%(v)o' % {"v": val})
      
  # output an integer value as a hexadecimal number
  def hex(self,val):
    self.str('%(v)X' % {"v": val})
      
  # output a floating point value
  def float(self,val):
    self.str('%(v)F' % {"v": val})
  
  # initialize the LCD    
  def __init__(self, type, rs, e, d7, d6, d5, d4):
    self.type = type
    self.rows = type % 100
    self.cols = type / 100
    self.rs   = rs
    self.e    = e
    self.d7   = d7
    self.d6   = d6
    self.d5   = d5
    self.d4   = d4
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    for pin in (e, rs, d7, d6, d5, d4):
      GPIO.setup(pin, GPIO.OUT)
    for dat in (0x33,0x32,0x28,0x0C,0x060,0x01):
      self.cmd(dat)
    self.cls
    
def main():
 
  lcd = lcd_module(2004, 17, 4, 25, 24, 23,22)

  lcd.disp(0,0,"http:/Mikronauts.com")
  lcd.disp(0,1,"20x4 character LCD's")
  lcd.disp(0,2,"make great embedded")
  lcd.disp(0,3,"status displays!")
  lcd.dec(lcd.type)

  lcd2 = lcd_module(1602, 17, 27, 25, 24, 23,22) 
  lcd2.str("Hello World!")
  lcd2.dec(lcd2.type)
  lcd2.disp(1,1,"Dual Screen Pi")

if __name__ == '__main__':
  main()
