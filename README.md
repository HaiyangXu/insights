
#Install rabbitmq

    sudo apt-get install rabbitmq-server
    
#Run rabbitmq
    
    sudo rabbitmq-server
    
#Start Celery Worker 

    celery  worker -A tasks --loglevel=info # daemon
    
    
    
