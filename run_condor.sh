#!/bin/bash

LOGDIR=log
mkdir -p $LOGDIR
TASK_FILE=$LOGDIR/task_1             ​
echo "
    executable =  /extra/scratch05/fjvigil/webdataset/sumary.py    
    output = ${TASK_FILE}.log
    error = ${TASK_FILE}.err
    log = ${TASK_FILE}.clog
    queue
" > $TASK_FILE                ​
condor_submit.sh -c 1 -r 3900 --config $TASK_FILE
