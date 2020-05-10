#!/usr/bin/env python3
# https://superuser.com/questions/100288/how-can-i-check-the-integrity-of-a-video-file-avi-mpeg-mp4
import glob
import os
from pprint import pprint
import subprocess

errors = dict()
# videos = []
for i in glob.glob('*mp4'):
    t = os.popen('ffmpeg -v 5 -i "%s" -f null - 2>&1' % i).read()
    print(t)