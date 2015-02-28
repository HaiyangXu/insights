#!/usr/bin/python env
# -*- coding:utf-8 -*-  
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *
from datetime import datetime
import os

# 服务器登录用户名:
env.user = 'ubuntu'
# sudo用户为root:
env.sudo_user = 'root'
# 服务器地址，可以有多个，依次部署:
env.hosts=['52.74.25.58']
# env.password='xxxxxx'
#env.key_filename = "~/.ssh/id_rsa"
env.key_filename = './amazon.pem'

project_dir='~/www'
virtual_dir='.'


#virtualenv 
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
    run(path + command.strip())
    
def virtualsrun(command):
    """
    Run a command as sudo in the virtualenv. This prefixes the command with the virtualenv path.
    Usage:
        virtualrun('pip install django')
    """
    path =getVirtualPath()
    srun(path + strip(command))
    

        
#git related 
def mkdir():
    try:
        run('mkdir {directory}'.format(directory=project_dir))
    except Exception, e:
        pass
    
def pull():
    with cd(project_dir):
        run('git reset --hard')
        run('git pull')

def github(message='commit with fabric'):
    with lcd(os.path.join(os.path.abspath('.'), '.')):
        local('git add -A')
        local('git commit -m "{0}" '.format(message))
        local('git push origin master')

def clone():
    mkdir()
    with cd(project_dir):
        run('git clone https://github.com/HaiyangXu/insights.git .')
        
        
#nginx reload
def nginx():
    with cd('/etc/nginx/sites-enabled'):
        print("Remember to remove the default config!")
        sudo('ln -s -f  {0}/nginx.conf '.format(project_dir))
        sudo('/etc/init.d/nginx reload')
        
#supervisor 

def supervisor():
    with cd(project_dir):
        sudo('killall -r supervisor')
        sudo('supervisord -c supervisord.conf')
def supervisor_reload():
    with cd(project_dir):
        sudo('supervisorctl reload -c supervisord.conf')
def gunicorn():
    with cd(project_dir):
        sudo('supervisorctl start insights')
           
def celery_broker():
    with cd(project_dir):
        sudo('supervisorctl start celerybroker')

        
def celery_worker():
     with cd(project_dir):
        sudo('supervisorctl start celeryworker')
        
def celery_monitor():
     with cd(project_dir):
        sudo('supervisorctl start celerymonitor')
        
        
#local depoy
_TAR_FILE = 'dist-awesome.tar.gz'

def build():
    includes = ['admin', 'celery-task', 'insights', 'RESTful','utility', '*.py','*.conf','*.txt','*.md']
    excludes = ['test', '.*', '*.pyc', '*.pyo']
    local('rm -f dist/%s' % _TAR_FILE)
    with lcd(os.path.abspath('.')):
        cmd = ['tar', '--dereference', '-czvf', '../dist/%s' % _TAR_FILE]
        cmd.extend(['--exclude=\'%s\'' % ex for ex in excludes])
        cmd.extend(includes)
        local(' '.join(cmd))
        
_REMOTE_TMP_TAR = '/tmp/%s' % _TAR_FILE
_REMOTE_BASE_DIR = '/home/ubuntu/'

def deploy():
    newdir = 'www-%s' % datetime.now().strftime('%y-%m-%d_%H.%M.%S')
    # 删除已有的tar文件:
    run('rm -f %s' % _REMOTE_TMP_TAR)
    # 上传新的tar文件:
    put('../dist/%s' % _TAR_FILE, _REMOTE_TMP_TAR)
    # 创建新目录:
    with cd(_REMOTE_BASE_DIR):
        sudo('mkdir %s' % newdir)
    # 解压到新目录:
    with cd('%s/%s' % (_REMOTE_BASE_DIR, newdir)):
        sudo('tar -xzvf %s' % _REMOTE_TMP_TAR)
    # 重置软链接:
    with cd(_REMOTE_BASE_DIR):
        sudo('rm -f www')
        sudo('ln -s %s www' % newdir)
        sudo('chown www-data:www-data www')
        sudo('chown -R www-data:www-data %s' % newdir)
    # 重启Python服务和nginx服务器:
    nginx()
    supervisor_reload()
        
#shotcut commd 
def cmd(commd):
    run(commd)
    
def scmd(commd):
    sudo(commd)

def update():
    """
    Update code to github and pull code on remote host
    """
    github()
    pull()
    
def upload():
    build()
    deploy()
        
def testnginx():
    update()
    nginx()
    
def celery():
    celery_broker()
    celery_worker()
    celery_monitor()
    

def gitdeploy():
    clone()
    nginx()
    supervisor()