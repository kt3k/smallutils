#! /usr/bin/env python

import os
print 'content-type:text/plain;'
print
print 'Your User Agent is:', os.environ['HTTP_USER_AGENT']
