#!/usr/bin/python3
"""Fabric script module"""
from fabric.api import *
import os


env.hosts = ['54.197.43.224', '52.201.178.140']


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False

    put('versions/{}'.format(archive_path), 'tmp/{}'.format(archive_path))
    run('mkdir -p /data/web_static/releases/{}/'.format(archive_path))
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'.format(archive_path, archive_path[:-4]))
    run('rm /tmp/{}'.format(archive_path))
    run('mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/'.format(archive_path[:-4], archive_path[:-4]))
    run('rm -rf /data/web_static/releases/web_static')
    run('ln -sf /data/web_static/releases/{}/ /data/web_static/current'.format(archive_path[:-4]))
    print('New version deployed!')
    return True
