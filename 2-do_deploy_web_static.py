#!/usr/bin/python3
"""
    Deploy archive!
    Fabric script (based on the file 1-pack_web_static.py) that distributes
    an archive to your web servers, using the function do_deploy
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
env.hosts = ['3.88.198.237', '54.83.236.78']


def do_deploy(archive_path):
    """ Deploy web static """
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        new_comp = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + new_comp.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xzf /tmp/{} -C {}".
            format(new_comp, new_folder))
        run("sudo rm /tmp/{}".format(new_comp))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run('sudo rm -rf /data/web_static/current')
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        return True
    except Exception:
        return False
