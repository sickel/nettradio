BINDIR=/usr/local/bin
WWWDIR=/var/www/html

install: installapt installpi installbuttons

installapt:
	apt install mpg123 apache2 libapache2-mod-wsgi-py3 python3-flask  
	addgroup www-data audio


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


linkweb: 
	ln -sT ~/nettradio /var/www/html/nettradio
