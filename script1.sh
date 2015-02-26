#!/bin/sh
var1=`locate apertium-apy/servlet.py`
var2=${var1::-10}
echo $var2
cd $var2
./servlet.py /usr/share/apertium
