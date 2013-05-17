#! /usr/bin/env python

import os
print 'content-type:text/plain;'
print
print 'Your IP address is:', os.environ['REMOTE_ADDR']
