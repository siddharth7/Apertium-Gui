#!/bin/sh
chmod +x script1.sh
chmod +x script2.sh
nohup bash script1.sh &
nohup bash script2.sh &
