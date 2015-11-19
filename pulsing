#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import datetime
from itertools import chain, repeat
from subprocess import call
import sys
import time

import RPi.GPIO as gpio


def main(argv=sys.argv[1:]):
    gpio.setmode(gpio.BCM)
    gpio.setup(23, gpio.OUT)
    led = gpio.PWM(23, 100)
    led.start(0)

    try:
        while True:
            for i in range(101):
                led.ChangeDutyCycle(i)
                time.sleep(0.02)
            for i in range(101):
                led.ChangeDutyCycle(100-i)
                time.sleep(0.02)
    except KeyboardInterrupt:
        pass
    finally:
        led.stop()
        gpio.cleanup()


if __name__ == '__main__':
    main()
