#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
import time


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    local("mkdir -p versions")
    try:
        file_name = 'versions/web_static_{}.tgz'.format(time.strftime('%Y%m%d%H%M%S'))
        local('tar -cvzf {} web_static'.format(file_name)) 
        return file_name
    except:
        return None

