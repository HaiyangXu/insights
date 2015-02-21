#!/usr/bin/python env
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
import os
env.hosts=['aws.codeidea.cn']
# env.password='xxxxxx'
#env.key_filename = "~/.ssh/id_rsa"
env.key_filename = './amazon.pem'
project_dir='~/insights'


def cmd(commd):
    run(commd)
    
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
        sudo('ln -s -f  ~/insights/deploy/nginx.conf ')
        sudo('/etc/init.d/nginx reload')
        
def gunicorn():
    with cd(project_dir):
        run('gunic')
        
def github(message='commit with fabric'):
    with lcd(os.path.join(os.path.abspath('.'), '..')):
        local('git add -A')
        local('git commit -m "{0}" '.format(message))
        local('git push origin master')
        
def celery_broker():
    with cd(project_dir):
        try:
            run('sh celery-task/broker.sh')
        except Exception, e:
            pass
        
        
def celery_worker():
     with cd(project_dir+'/celery-task'):
        sudo('cat worker.sh |bash')
        
def celery_monitor():
     with cd(project_dir):
        run('sh celery-task/monitor.sh')
        
def celery():
    execute(celery_broker)
    execute(celery_worker)
    execute(celery_monitor)
    
      
def deploy():
    execute(git)
    execute(nginx)