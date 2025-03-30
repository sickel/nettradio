import sys
sys.path.insert(0,'/var/www/html/nettradio')
from flaskradio import create_app
application = create_app()
