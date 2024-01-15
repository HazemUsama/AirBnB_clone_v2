#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *

env.hosts = ['54.197.43.224', '52.201.178.140']
env.user = 'ubuntu'


def do_clean(number=0):
    """ deletes out-of-date archives """
    number = int(number)
    path = '/data/web_static/releases'

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))