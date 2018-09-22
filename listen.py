#!/usr/bin/python

import dweepy
import os
import re

path = os.path.dirname(os.path.realpath(__file__))

for dweet in dweepy.listen_for_dweets_from(os.environ['DWEETID']):
    for k, v in dweet['content'].iteritems():
        fname = path + '/' + ('run-' + k + '.py').replace('/', '')
        if os.path.isfile(fname):
            v = re.sub('[^a-zA-Z0-9]', '', str(v))
            print fname, v
            os.system(fname + ' ' + v)

