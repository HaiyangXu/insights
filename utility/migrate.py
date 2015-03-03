#!--coding=utf-8--
"""
migrate 说明

在根目录执行

初始化
    
    python utility/migrate.py db init
    
对数据库更改，产生Migrate脚本：

    python utility/migrate.py db migrate --message 'Message'
    
将更改应用到数据库：

    python utility/migrate.py db upgrade
    
撤销：

    python utility/migrate.py db downgrade
"""

from insights import app,db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()