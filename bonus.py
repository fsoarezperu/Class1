#! /usr/bin/env python
import  time
from subprocess import call
import subprocess

call(['espeak "Alert" 2>/dev/null'], shell=True)
time.sleep(3)
call(['espeak "Intruder detected" 2>/dev/null'],shell=True)
time.sleep(3)
#p= subprocess.Popen("ls -lh", stdout=subprocess.PIPE, shell=True)
#print (p.communicate())
call(['espeak "The information its at risk" 2>/dev/null'],shell=True)
