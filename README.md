THIS IS NOT MY WORK !!
CREDITS BY thagrol
VISIT THE ORIGINAL https://github.com/thagrol/hdd-led

Simple python3 script to monitor /proc/diskstats and flash an LED depending on activity indicated there in.

Requires gpiozero (sudo apt install pyton3-gpiozero)

    usage: hddled.py [-h] [-i INTERVAL] [-g GPIO] [-l] [-d]

    optional arguments:
      -h, --help            show this help message and exit
      -i INTERVAL, --interval INTERVAL
                            poll interval in seconds. Default: 0.05
      -g1 GPIO, --gpio1 GPIO  GPIO pin to use. BCM numbering. Default: 17
      -g2 GPIO, --gpio2 GPIO  GPIO pin to use. BCM numbering. Default: 27
      -l, --active_low      GPIO is active when low.
  -d, --debug           enable debug output.
  
The shorter the poll interval the more responsive the LED will be but more CPU time will be used by the script.
Responsiveness will also drop on a heavily loaded system.
