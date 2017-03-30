#!/bin/bash

url=$1
pidfile=/tmp/radiopid


if [ -f $pidfile ];
then
   kill `cat $pidfile`
   rm $pidfile
fi

if [ $1 != "off" ]; then
   mpg123 $url &> /tmp/radiotitle &
   echo $! > $pidfile
fi

if [ $1 == "off"]; then
   rm /tmp/radiotitle
fi
