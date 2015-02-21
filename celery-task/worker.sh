#celery  worker -A tasks  --loglevel=info # sechedule
source ../env/bin/activate
celery  worker -A tasks -B --detach --loglevel=info # sechedule and worker
#celery  worker  --detach -A tasks --loglevel=info # daemon