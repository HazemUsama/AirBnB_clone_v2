#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
import time


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    local("mkdir -p versions")
    file_path = 'versions/web_static_{}.tgz'.format(
            time.strftime('%Y%m%d%H%M%S'))
    results = local('tar -cvzf {} web_static'.format(file_path))
    if results.success:
        return file_path
    return None
