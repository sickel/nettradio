import os

from flask import Flask

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.radioscript = '/usr/local/bin/radio.sh'


    try:
        os.makedirs(app.instance_path)
        print(app.instance_path)
    except OSError:
        pass

    filename = '/var/www/html/nettradio/stationlist.txt'

    with open(filename,'r') as listfile:
        lines = listfile.readlines()
    app.stationlist = {}
    app.stationidx = []
    for line in lines:
        line = line.strip()
        (key,name,url) = line.split(',')
        app.stationlist[key] = {'name':name ,'url': url}
        app.stationidx.append(key)


    @app.route('/radiotext')
    def radiotext():
        return 'OK'


    @app.route('/', methods=('GET', 'POST'))
    def radiopage():
        chcachefile = '/var/www/chcache'
        ch = None
        browses = {'prev': -1, 'next': 1}
        print(request.form.get)
        if request.method == 'POST':
           off = request.form.get('off')
           if not off is None:
               os.system(f'{app.radioscript} off')
           else: 
             ch = request.form.get('ch')
             if ch is None:
                try:
                    with open(chcachefile) as chcache:
                        ch = chcache.read().rstrip('\n').strip()
                except:
                    ch = app.stationidx[0]
             if not ch is None:
                if not request.form.get('browse') is None:
                    browse = browses[request.form.get('browse')]
                    chidx = app.stationidx.index(ch)
                    chidx += browse
                    if chidx >= len(app.stationidx):
                        chidx = 0
                    ch = app.stationidx[chidx]
                with open(chcachefile,'w') as chcache:
                    chcache.write(ch)
                url = app.stationlist[ch]['url']
                os.system(f'{app.radioscript} {url}')
                    

        return render_template('Nettradio.html', channellist=app.stationlist, activech = ch)



    return app


