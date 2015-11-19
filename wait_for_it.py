#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

from subprocess import call, check_call
import sys
import time

import RPi.GPIO as gpio


def main(argv=sys.argv[1:]):
    cmd = ' '.join('"{}"'.format(arg) for arg in argv)
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(23, gpio.OUT)
        gpio.output(23, False)
        while True:
            input_state = gpio.input(18)
            if input_state == False:
                gpio.output(23, True)
                check_call(cmd, shell=True)
                gpio.output(23, False)
    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()


if __name__ == '__main__':
    main()
