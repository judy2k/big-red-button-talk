#!/usr/bin/env python

from subprocess import Popen, PIPE
import time

process = Popen('espeak', stdin=PIPE)

for i in range(3):
    process.stdin.write('hello')
    time.sleep(10)
