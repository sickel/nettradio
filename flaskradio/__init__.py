import os

from flask import Flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.radioscript = '/usr/local/bin/radio.sh'


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    filename = 'flaskradio/stationlist.txt'

    with open(filename,'r') as listfile:
        lines = listfile.readlines()
    app.stationlist = {}
    for line in lines:
        line = line.strip()
        (key,name,url) = line.split(',')
        app.stationlist[key] = {'name':name ,'url': url}


    @app.route('/radiotext')
    def radiotext():
        return 'OK'


    @app.route('/', methods=('GET', 'POST'))
    def radiopage():
        ch = None
        if request.method == 'POST':
           off = request.form.get('off')
           if not off is None:
               os.system(f'{app.radioscript} off')
           else: 
             ch = request.form.get('ch')
             if not ch is None:
                url = app.stationlist[ch]['url']
                os.system(f'{app.radioscript} {url}')
                off = request.form.get('off')
                if not off is None:
                    os.system('{app.radioscript} off')

        return render_template('Nettradio.html', channellist=app.stationlist, activech = ch)



    return app


