#!/usr/bin/python

import os
import sys
from time import sleep

os.system('/usr/bin/gpio mode 7 out')

# on and off seem to be reversed
turn = 'on'
if sys.argv[1] == 'on':
    turn = 'off'

os.system('/usr/bin/gpio write 7 ' + turn)

flash = sys.argv[1]

if flash == 'flash':
    flash = '20';

if flash.isdigit():
    for x in range(0, int(flash)):
        os.system('/usr/bin/gpio write 7 on')
        sleep(0.2)
        os.system('/usr/bin/gpio write 7 off')
        sleep(0.2)
    os.system('/usr/bin/gpio write 7 on')
    
