#!/usr/bin/python

# -----------------------
# Import required Python libraries
# -----------------------
import cwiid
import time
from raspirobotboard import *

rr = RaspiRobot()
button_delay = 0.1

def led_flash():
  rr.set_led1(1)
  time.sleep(0.5)
  rr.set_led2(1)
  rr.set_led1(0)
  time.sleep(0.5)
  rr.set_led1(1)
  rr.set_led2(0)
  time.sleep(0.5)
  rr.set_led2(1)
  rr.set_led1(0)
  time.sleep(0.5)
  rr.set_led1(1)
  rr.set_led2(0)
  time.sleep(0.5)
  rr.set_led2(1)
  rr.set_led1(0)
  time.sleep(0.5)
  rr.set_led2(0)

def led_strobe():
  rr.set_led1(1)
  rr.set_led2(1)
  time.sleep(0.25)
  rr.set_led1(0)
  rr.set_led2(0)
  time.sleep(0.25)
  rr.set_led1(1)
  rr.set_led2(1)
  time.sleep(0.25)
  rr.set_led1(0)
  rr.set_led2(0)
  time.sleep(0.25)
  rr.set_led1(1)
  rr.set_led2(1)
  time.sleep(0.25)
  rr.set_led1(0)
  rr.set_led2(0)
  time.sleep(0.25)


led_flash()
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
    led_strobe()
    quit()
  

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    rr.right(0.1)
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    rr.left(0.1)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    rr.forward()        
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    rr.reverse()      
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    rr.set_oc1(1)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    rr.set_oc1(0)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    led_strobe()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    rr.stop()
    wii.rumble = 1
    time.sleep(0.25)
    wii.rumble = 0
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    rr.right(0.3)
    rr.left(0.3)
    rr.right(0.3)
    rr.left(0.3)
    rr.right(0.3)
    rr.left(0.3)
    wii.rumble = 1
    time.sleep(0.5)
    wii.rumble = 0
    time.sleep(button_delay)           
    
  if (buttons & cwiid.BTN_MINUS):
    rr.left()
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    rr.right()
    time.sleep(button_delay)
