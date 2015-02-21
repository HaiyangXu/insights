#!/usr/bin/python env
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
import os
env.hosts=['aws.codeidea.cn']
# env.password='xxxxxx'
#env.key_filename = "~/.ssh/id_rsa"
env.key_filename = './amazon.pem'

def ls(directory='~/'):
    print(green("I'm local {0}".format(directory)))
    with cd('{0}'.format(directory)):
        run('ls -l')
def git():
    with cd('~/insights'):
        run('git pull')
        
def nginx():
    with cd('/etc/nginx/sites-enabled'):
        sudo('ln -s -f  ~/insights/deploy/nginx.conf ')
        sudo('/etc/init.d/nginx reload')
        
def github(message='commit with fabric'):
    with lcd(os.path.join(os.path.abspath('.'), '..')):
        local('git add -A')
        local('git commit -m "{0}" '.format(message))
        local('git push origin master')
        
        
def put_path():
    print(green("I'm put local's test file to 10 and 12"))
    put('/home/apps/test','/home/apps/')
    print(yellow("I'm 10 or 12 /home/apps/"))
    with cd('/home/apps'):
        run('ls -l')
def deploy():
    execute(ls_path)
    execute(put_path)