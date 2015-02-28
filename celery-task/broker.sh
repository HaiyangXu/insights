#!/bin/sh
# run rabbitmq-server and start celery worker
#http://smilejay.com/2014/09/celery-worker-segmentation-fault-on-startup/

#sudo apt-get install rabbitmq-server
#sudo apt-get remove  python-librabbitmq 

# call "rabbitmqctl stop" when exiting
trap "{ echo Stopping rabbitmq; rabbitmqctl stop; exit 0; }" EXIT

echo Starting rabbitmq
rabbitmq-server