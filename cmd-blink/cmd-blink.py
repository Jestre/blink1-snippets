#!/usr/bin/python

""" 
    cmd-blink.py
    
    Demo code: Scott Schulz <swschulz@gmail.com> 

    Version: 0.1    2013-01-21
    
"""

import blink1
from time import sleep

millis = 300
delay  = 500

def blink(dev, reps, red, green, blue):
    """ Implements a --blink command, as found in blink1-tool.c """
    print "Blink {0} times rgb: {1},{2},{3}\n".format(reps, red, green, blue)
    for i in range(reps):
        blink1.fadeToRGB(dev, millis, red, green, blue)
        blink1.sleep(delay)
        sleep(1)
        blink1.fadeToRGB(dev, millis, 0, 0, 0)
        blink1.sleep(delay)
        sleep(1)
        
def main():
    """ Demo code """
    dev = blink1.open()
    blink(dev, 3, 255, 0, 0)
    blink1.close(dev)

if __name__ == '__main__':
    main()
