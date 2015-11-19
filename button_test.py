#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function

import datetime
from itertools import chain, repeat
from subprocess import call
import sys
import time

import RPi.GPIO as gpio


NUMBER_WORDS=["one", "two", "three", "four", "five", "six", "seven", "eight","nine", 
       "ten", "eleven", "twelve", "thirteen", "fourteen", "quarter", "sixteen",
       "seventeen", "eighteen", "nineteen", "twenty", "twenty one", 
       "twenty two", "twenty three", "twenty four", "twenty five", 
       "twenty six", "twenty seven", "twenty eight", "twenty nine", "half"]
 

def speak(message):
    call(["/usr/bin/espeak", message])


def time_text():
    dd=datetime.datetime.now()
    hrs = dd.hour
    mins = dd.minute
    header="It is "
    msg=""
    if (hrs >12):
        hrs=hrs-12
    if (mins == 0):
        hr = NUMBER_WORDS[hrs-1]
        msg=header + hr + " o'clock."
    elif (mins < 31):      
           hr = NUMBER_WORDS[hrs-1]
           mn = NUMBER_WORDS[mins-1]
           msg = header + mn + "minutes past " + hr + "."
    else:
        hr = NUMBER_WORDS[hrs]
        mn =NUMBER_WORDS[(60 - mins-1)]
        msg = header + mn + " minutes to " + hr + "."
    return msg


class Responder(object):
    def __init__(self):
        self.tasks = chain([
            lambda: speak(time_text()),
            lambda: speak(time_text()),
            lambda: speak("stop it"),
            lambda: speak("that is really annoying"),
            lambda: speak("I'm warning you"),
            ],
            repeat(lambda: speak("I hate you")) 
        )
        self.next_task = next(self.tasks)

    def respond(self):
        self.next_task()
        self.next_task = next(self.tasks)


def main(argv=sys.argv[1:]):
    responder = Responder()
    try:
        gpio.setmode(gpio.BCM)
        gpio.setup(18, gpio.IN, pull_up_down=gpio.PUD_UP)
        gpio.setup(23, gpio.OUT)
        gpio.output(23, False)
        while True:
            input_state = gpio.input(18)
            if input_state == False:
                gpio.output(23, True)
                time.sleep(0.2)
                responder.respond()
                gpio.output(23, False)
    except KeyboardInterrupt:
        pass
    finally:
        gpio.cleanup()


if __name__ == '__main__':
    main()
