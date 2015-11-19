#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility functions for the BIG RED BUTTON.
"""

from contextlib import contextmanager
import RPi.GPIO as gpio


BUTTON_PIN = 18
LED_PIN = 23


@contextmanager
def setup():
    """
    Context manager that ensures state is initialised and cleaned up correctly.
    """
    gpio.setmode(gpio.BCM)
    gpio.setup(BUTTON_PIN, gpio.IN, pull_up_down=gpio.PUD_UP)
    gpio.setup(LED_PIN, gpio.OUT)
    gpio.output(LED_PIN, False)
    try:
        yield
    finally:
        gpio.cleanup()


def button_pressed():
    """
    Returns True if the button is pressed, False otherwise.
    """
    return not gpio.input(BUTTON_PIN)


def set_led(state):
    """
    Set the LED to full-on (True) or full-off (False)
    """
    gpio.output(LED_PIN, state)


if __name__ == '__main__':
    main()
