BINDIR=/usr/local/bin 
WWWDIR=/var/www/html

installwww:
        cp www/* $(WWWDIR)

installsh:
        cp shell/* $(BINDIR)

installbuttons:
        cp hardware/buttons.py $(BINDIR)

installhw: installbuttons

