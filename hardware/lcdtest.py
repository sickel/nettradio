#!/usr/bin/python
from mikezlcd import *
lcd = lcd_module(2004, 17, 4, 25, 24, 23,22)
lcd.disp(0,0,"20x4 character LCD's")
lcd.disp(0,1,"make great embedded")
lcd.disp(0,2,"status displays!")
lcd.disp(0,3,"<-     ->       off")

