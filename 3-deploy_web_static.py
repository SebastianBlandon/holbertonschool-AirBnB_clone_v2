#!/usr/bin/python3
"""
    Full deployment
    Fabric script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the function deploy
"""
import os.path
from fabric.api import *
from fabric.operations import run, put, sudo
import time
env.hosts = ['3.88.198.237', '54.83.236.78']


def do_pack():
    """ Pack the contents of the web_static folder """
    timestr = time.strftime("%Y%m%d%H%M%S")
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(timestr))
        return ("versions/web_static_{}.tgz".format(timestr))
    except Exception:
        return None


def do_deploy(archive_path):
    """ Do deploy web static """
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


def deploy():
    """ Deploy web static """
    try:
        archive_address = do_pack()
        val = do_deploy(archive_address)
        return val
    except Exception:
        return False
