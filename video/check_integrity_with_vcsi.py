#!/usr/bin/env python3
import glob
import os
from pprint import pprint
import subprocess

errors = dict()
# videos = []
for i in glob.glob('2_*'):
    if '.' not in i:
        if not os.path.isfile('{}.jpg'.format(i)):
            # videos.append(i)
            try:
                subprocess.call(['vcsi', i, '-g', '2x3'])
            except Exception as e:
                errors[i] = e

pprint(errors)
