#!/usr/bin/env python3
"""
Fabric script to pack web_static content
"""

from fabric.api import local
from datetime import datetime
import os

def do_pack():
    """Generates a .tgz archive from the contents of web_static."""
    try:
        if not os.path.exists("versions"):
            os.makedirs("versions")

        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        local("tar -cvzf {} web_static".format(archive_path))

        print("web_static packed: {} -> {}Bytes".format(archive_path, os.path.getsize(archive_path)))

        return archive_path
    except Exception as e:
        return None
