# run rabbitmq-server and start celery worker
#ubuntu 14.04 bug python-librabbitmq包,这样celery会回到使用python-amqp包
# http://smilejay.com/2014/09/celery-worker-segmentation-fault-on-startup/

#sudo apt-get install rabbitmq-server
#sudo apt-get remove  python-librabbitmq 

sudo  rabbitmq-server #-detached  #daemon
