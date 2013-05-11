#!/usr/bin/python

# -----------------------
# Import required Python libraries
# -----------------------

#lib to handle wii remote
import cwiid
#lib to handle timing
import time
#lib to handle serial
import serial
#lib to handle robot board
from raspirobotboard import *

#try to set up serial, if not there quit
try:
    ser = serial.Serial('/dev/ttyACM0', 9600)
except RuntimeError:
    # If serial fails, signal with strobing light
    led_strobe_1()
    quit()

#init serial connection
ser = serial.Serial('/dev/ttyACM0', 9600)
#init robot board
rr = RaspiRobot()
#init button delay
button_delay = 0.1
#init headlight bool
headlights = 0


#function for flash
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

#function for strobe
def led_strobe():
  count = 0
  while count < 4:
      rr.set_led1(1)
      rr.set_led2(1)
      time.sleep(0.25)
      rr.set_led1(0)
      rr.set_led2(0)
      time.sleep(0.25)

#function for strobe 1
def led_strobe_1():
    count = 0
    while count < 4:
        rr.set_led2(1)
        time.sleep(0.25)
        rr.set_led2(0)
        time.sleep(0.25)

# Flash lights to signal pairing is ready
led_flash()
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
    # If pairing fails, signal with strobing lights
    led_strobe()
    quit()
  
#enable button reporting from wii remote
wii.rpt_mode = cwiid.RPT_BTN

#runloop
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
    ser.write('a')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    ser.write('b')
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    headlights = (headlights + 1) % 2
    rr.set_oc1(headlights)
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
    ser.write('b')
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    ser.write('a')
    time.sleep(button_delay)
