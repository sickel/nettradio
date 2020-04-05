BINDIR=/usr/local/bin 
WWWDIR=/var/www/html

install: installpi installbuttons
	addgroup www-data audio
	apt install mpg123 apache2 php
	
installpi: installwww installsh

installwww:
	cp www/* $(WWWDIR)

	
installsh:
	cp shell/* $(BINDIR)

installbuttons:
	cp hardware/buttons.py $(BINDIR)

installhw: installbuttons

