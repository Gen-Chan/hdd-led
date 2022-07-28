#!/usr/bin/env python3

##
## (C) 2020 Simon Osborne
## No warranties, express or implied.
## Use entirely at your own risk
## Freely distrubutable subject to the following:
##  1. Don't claim credit for my work.
##  2. Do not charge for this software and its acompanying files
##  3. All acompanying files must be distributed with this script
##  4. Derivative works must comply with the above
##
## This script origanally published at https://github.com/thagrol/hdd-led
##

import argparse
import gpiozero
import logging
import time
import re


STATSFILE = '/proc/diskstats'
FIELD = 20


# parse cmdline args
#    Default    Description
# -i 0.05       poll interval
# -g 21         gpio to use
# -l            active low
parser = argparse.ArgumentParser(description='Simple python3 script to monitor /proc/diskstats and flash an LED depending on activity indicated there in.',
                                 epilog='The shorter the poll interval the more responsive the LED will be but more CPU time will be used by the script.'
                                )
parser.add_argument('-i', '--interval',
                    action='store',
                    type=float,
                    default=0.05,
                    help='poll interval in seconds. Default: 0.05'
                   )
parser.add_argument('-g1', '--gpio1',
                    action='store',
                    type=int,
                    default=17,
                    help='GPIO pin to use. BCM numbering. Default: 17'
                   )
parser.add_argument('-g2', '--gpio2',
                    action='store',
                    type=int,
                    default=27,
                    help='GPIO pin to use. BCM numbering. Default: 27'
                   )
parser.add_argument('-l', '--active_low',
                    action='store_true',
                    default=False,
                    help='GPIO is active when low.'
                   )
parser.add_argument('-d', '--debug',
                    action='store_const',
                    const=logging.DEBUG,
                    default=logging.WARNING,
                    help='enable debug output.'
                   )
args = parser.parse_args()

logging.basicConfig(level=args.debug)
logging.debug(args)

INTERVAL = args.interval
GPIO1 = args.gpio1
GPIO2 = args.gpio2
ACTIVE_HIGH = not(args.active_low)

led1 = gpiozero.LED(GPIO1,
                   active_high=ACTIVE_HIGH,
                   )
led2 = gpiozero.LED(GPIO2,
                   active_high=ACTIVE_HIGH,
                   )

logging.debug('Starting mian polling loop')
while True:
    try:
        with open(STATSFILE,mode='r') as s:
            for line in s:
                if re.search('sda', line):
                    hdd1 = line
                if re.search('sdb', line):
                    hdd2 = line

            disc1_active = False
            disc2_active = False

            print(hdd2.split(' '))

        for l in hdd1.split(' ')[FIELD]:
            try:
                if int(l):
                    disc1_active = True
                    break
            except IndexError:
                pass
        for l in hdd2.split(' ')[FIELD - 1]:
            try:
                if int(l):
                    disc2_active = True
                    break
            except IndexError:
                pass
        led1.value = disc1_active
        led2.value = disc2_active
        time.sleep(INTERVAL)
    except Exception:
        if args.debug:
            raise
        else:
            logging.exception('')
