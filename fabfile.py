# coding=utf-8

from fabric.api import *

repo_name = 'smallutils'

env.use_ssh_config = True
env.shell = '/bin/sh -c'
env.hosts = ['sakura']

def sakura():

  target_dir = 'www/' + repo_name

  with settings(warn_only=True):
    if run('test -d %s' % target_dir).failed:
      run('git clone git@github.com:kt3k/smallutils.git %s' % target_dir)

  with cd(target_dir):
    run('git pull')
