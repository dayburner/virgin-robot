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
  time.sleep(0.75)
  rr.set_led1(0)
  rr.set_led2(0)
  rr.sleep(0.25)
  rr.set_led1(1)
  rr.set_led2(1)
  time.sleep(0.75)
  rr.set_led1(0)
  rr.set_led2(0)
  rr.sleep(0.25)
  rr.set_led1(1)
  rr.set_led2(1)
  time.sleep(0.75)
  rr.set_led1(0)
  rr.set_led2(0)
  rr.sleep(0.25)


print 'Press 1 + 2 on your Wii Remote now ...'
led_flash()
time.sleep(1)

# Connect to the Wii Remote. If it times out
# then quit.
try:
  wii=cwiid.Wiimote()
except RuntimeError:
  print "Error opening wiimote connection"
  quit()

print 'Wii Remote connected...\n'
print 'Press some buttons!\n'
print 'Press PLUS and MINUS together to disconnect and quit.\n'

wii.rpt_mode = cwiid.RPT_BTN
 
while True:

  buttons = wii.state['buttons']

  # If Plus and Minus buttons pressed
  # together then rumble and quit.
  if (buttons - cwiid.BTN_PLUS - cwiid.BTN_MINUS == 0):  
    print '\nClosing connection ...'
    wii.rumble = 1
    time.sleep(1)
    wii.rumble = 0
    exit(wii)  
  
  # Check if other buttons are pressed by
  # doing a bitwise AND of the buttons number
  # and the predefined constant for that button.
  if (buttons & cwiid.BTN_LEFT):
    print 'Left pressed'
    rr.right(0.1)
    time.sleep(button_delay)         

  if(buttons & cwiid.BTN_RIGHT):
    print 'Right pressed'
    rr.left(0.1)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_UP):
    print 'Up pressed'
    rr.forward()        
    time.sleep(button_delay)          
    
  if (buttons & cwiid.BTN_DOWN):
    print 'Down pressed'
    rr.reverse()      
    time.sleep(button_delay)  
    
  if (buttons & cwiid.BTN_1):
    print 'Button 1 pressed'
    rr.set_oc1(1)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_2):
    print 'Button 2 pressed'
    rr.set_oc1(0)
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_A):
    print 'Button A pressed'
    led_strobe()
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_B):
    print 'Button B pressed'
    rr.stop()
    wii.rumble = 1
    time.sleep(0.25)
    wii.rumble = 0
    time.sleep(button_delay)          

  if (buttons & cwiid.BTN_HOME):
    print 'Home Button pressed'
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
    print 'Minus Button pressed'
    rr.left()
    time.sleep(button_delay)   
    
  if (buttons & cwiid.BTN_PLUS):
    print 'Plus Button pressed'
    rr.right()
    time.sleep(button_delay)
