#!/bin/sh
procs=(`ps -fA | grep  ./servlet.py | grep /usr | awk '{print $2}'`)
for pid in $procs; do
	kill $pid
done ;
chmod +x script1.sh
chmod +x script2.sh
nohup bash script1.sh &
sleep 2
nohup bash script2.sh &
