
# nettradio

Very simple network radio. Made for listening to NRK (nrk.no) on a raspberry. Can be set to work with any station
that have available mp3-streams for their channels.


Copy the shell script to /usr/local/bin and the php file to anywhere it can be picked up by your web server. Feel
free to rename the php-file.

To use it:

Make sure the the user that the web server runs as can play audio

On debian
sudo addgroup www-data audio

Make sure that the directory the script is stored in is writeable by the web server user (yes I know this is a safety issue)

mpg123 must be installed and in path

make sure that no other user has created the files /tmp/radiopid and /tmp/radiotitle

To use hardware buttons and display, use buttons.py and texttest.py. 
For conncections of buttons, see https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/robot/buttons_and_switches/ 

The buttons should be connected so the port is low when the button is open. They are connected to GPIO9 (next channel), GPIO10 (previous channel) and GPIO11 (off).


For display, see https://www.algissalys.com/how-to/nokia-5110-lcd-on-raspberry-pi

The channels are listed in stationlist.txt, each line in the file should consist of three items, separated by , (comma): Unique id,Name (shown in the web interface), url to mp3 stream


==Installation==

On a pi without any buttons or display:

sudo make installpi

On a pi with buttons:

sudo make install


Software for display still needs to be installed manually as I am presently not testing it - 


https://asdkazmi.medium.com/deploying-flask-app-with-wsgi-and-apache-server-on-ubuntu-20-04-396607e0e40f

