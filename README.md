# nettradio
Very simple network radio. Made for listening to NRK (nrk.no) on a raspberry. Can be set to work with any station
that have available mp3-streams for their channels.

To use it:

Make sure the the user that the web server runs as can play audio

On debian
sudo addgroup www-data audio

Make sure that the directory the script is stored in is writeable by the web server user (yes I know this is a safety issue)



