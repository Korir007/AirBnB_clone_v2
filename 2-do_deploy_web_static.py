#!/usr/bin/env python3
"""
Fabric script to deploy web_static content to web servers
"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']
env.user = 'ubuntu'
env.key_filename = 'my_ssh_private_key'


def do_deploy(archive_path):
    """Deploys web_static to web servers."""
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/<archive filename without extension>
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        release_path = '/data/web_static/releases/web_static_{}/'.format(timestamp)
        run('mkdir -p {}'.format(release_path))
        run('tar -xzf /tmp/{} -C {}'.format(archive_path.split('/')[-1], release_path))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_path.split('/')[-1]))

        # Move contents to the correct location
        run('mv {}web_static/* {}'.format(release_path, release_path))

        # Delete unnecessary web_static directory
        run('rm -rf {}web_static'.format(release_path))

        # Delete the symbolic link /data/web_static/current
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('ln -s {} /data/web_static/current'.format(release_path))

        print('New version deployed!')

        return True
    except Exception as e:
        return False
