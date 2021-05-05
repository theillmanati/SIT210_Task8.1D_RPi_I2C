#!/usr/bin/python

# LIBRARIES #
import smbus
import time

# CONSTANTS #
bus = smbus.SMBUS(1)
DEVICE = 0x23 # Default device I2C address

# FUNCTIONS #
def readLight(address = DEVICE):
  # Read data from I2C interface
  data = bus.read_ISC_block_data(address, DEVICE)
  result = (data[1] + (256 * data[0]) / 1.2
  return result
           
try:
  while 1:
    lightLevel = readLight()
    print ("Light level = %.2f lx" % lightLevel)
    if(lightLevel <= 20):
      print ("Too dark")
    elif(lightLevel > 20 and lightLevel <= 100):
      print ("Dark")
    elif(lightLevel > 100 and lightLevel <= 200):
      print ("Medium")
    elif(lightLevel > 200 and lightLevel <= 500):
      print ("Bright")
    else:
      print ("Too bright")
    time.sleep(1)
         
except keyboardInterrupt:
  print ("Measurement stopped by user")
           
