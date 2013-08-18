#!/bin/bash
set -e 
LOGFILE=guni.log
LOGDIR=$(dirname $LOGFILE)
NUM_WORKERS=3  # cpu core nums * 2 + 1
USER=nobody
GROUP=nogroup
# WORKER=gevent # install python gevent
ADDRESS=127.0.0.1:8000
test -d $LOGDIR || mkdir -p $LOGDIR
exec gunicorn_django -w $NUM_WORKERS --bind=$ADDRESS \
 # -k $WORKER 
  --daemon \
  --user=$USER --group=$GROUP --log-level=error \
  --log-file=$LOGFILE 2>>$LOGFILE
