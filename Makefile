BINDIR=/usr/local/bin
WWWDIR=/var/www/html

install: installapt installpi installbuttons

installapt:
	apt install mpg123 apache2 libapache2-mod-wsgi-py3 python3-flask  
	addgroup www-data audio


installpi: installwww installsh

installwwwphp:
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

installsite:

	cp /etc/apache2/sites-available/000-default.conf 000-default.backup
	cp 000-default.conf /etc/apache2/sites-available/


linkweb: 
	ln -sT /home/pi/devel/nettradio /var/www/html/nettradio
