#!/usr/bin/python env
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
import os
env.hosts=['aws.codeidea.cn']
# env.password='xxxxxx'
#env.key_filename = "~/.ssh/id_rsa"
env.key_filename = './amazon.pem'
project_dir=os.path.abspath('~/www')
try:
    run('mkdir {directory}'.format(directory=project_dir))
except Exception, e:
    pass
virtual_dir='.'

def cmd(commd):
    run(commd)
    
def scmd(commd):
    sudo(commd)

def create_virtual():
    """
    Create a virtualenv on Host
    """
    with cd(project_dir):
        run('virtualenv '+virtual_dir)
        virtualrun('pip install -r requirements.txt')
        
def getVirtualPath():
    return os.path.join(project_dir,virtual_dir,'bin','')

def virtualrun(command):
    """
    Run a command in the virtualenv. This prefixes the command with the virtualenv path.
    Usage:
        virtualrun('pip install django')
    """
    path =getVirtualPath()
    run(path + strip(command))
    
def virtualsrun(command):
    """
    Run a command as sudo in the virtualenv. This prefixes the command with the virtualenv path.
    Usage:
        virtualrun('pip install django')
    """
    path =getVirtualPath()
    srun(path + strip(command))
    
 
def ls(directory='~/'):
    print(green("I'm local {0}".format(directory)))
    with cd('{0}'.format(directory)):
        run('ls -l')
def git():
    with cd(project_dir):
        run('git reset --hard')
        run('git pull')
        
def nginx():
    with cd('/etc/nginx/sites-enabled'):
        sudo('ln -s -f  ~/insights/nginx.conf ')
        sudo('/etc/init.d/nginx reload')
        
def gunicorn():
    with cd(project_dir):
        sudo('supervisorctl start insights')
        
def github(message='commit with fabric'):
    with lcd(os.path.join(os.path.abspath('.'), '.')):
        local('git add -A')
        local('git commit -m "{0}" '.format(message))
        local('git push origin master')
        
def celery_broker():
    with cd(project_dir):
        sudo('supervisorctl start celerybroker')
        
def celery_worker():
     with cd(project_dir):
        sudo('supervisorctl start celeryworker')
        
def celery_monitor():
     with cd(project_dir):
        sudo('supervisorctl start celerymonitor')
        
def celery():
    celery_broker()
    celery_worker()
    celery_monitor()
    
      
def deploy():
    git()
    nginx()
    gunicorn()
    celery()