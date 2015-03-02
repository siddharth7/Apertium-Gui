#!/bin/sh
procs=`ps -fA | grep  ./servlet.py | grep /usr | awk '{print $2}'`
for pid in $procs; do
    kill $pid
done ;
