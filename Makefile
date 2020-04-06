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
	cp hardware/runbuttons.py $(BINDIR)/runbuttons
	cp buttons.service  /etc/systemd/system
	systemctl daemon-reload

startbuttons:
	systemctl enable buttons
	systemctl start buttons


installhw: installbuttons

