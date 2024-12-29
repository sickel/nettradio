#!/bin/bash
path=/usr/bin:/bin
url=$1
pidfile=~/radiopid


if [ -f $pidfile ];
then
   kill `cat $pidfile`
   rm $pidfile
fi

if [ $url != "off" ]; then
   mpg123 -o alsa  $url 2> ~/radiotitle &
   echo $! > $pidfile
fi
