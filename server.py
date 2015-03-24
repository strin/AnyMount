from flask import *
import pdb
import webbrowser
import threading
import json

import cloud.dropbox as dropbox
import database.mountdb as mountdb

import sys
reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)
db = mountdb.ShelveDB('database.db')
db.load()

@app.route("/programmer")
def programmer():
    try:
        return render_template('programmer.html')
    except Exception as e:
        print "error:", e

def open_webbrowser():
    webbrowser.open('http://127.0.0.1:8080/programmer')

@app.route('/createmount', methods=['POST']) 
def mount_dir():
  try:
    path = request.form['dir'].decode('utf-8')

    names = request.form['names'].decode('utf-8')
    names = json.loads(names)

    links = request.form['links'].decode('utf-8')
    links = json.loads(links)
    links = dropbox.make_raw_links(links)

    mnt = mountdb.Mount(path, names, links, selected = False)
    db.mount(mnt)
    db.save()

    return jsonify(response='ok')
  except Exception as e:
    print "error:", e

if __name__ == "__main__":
    thread = threading.Thread(target = open_webbrowser)
    thread.start()
    app.run('127.0.0.1', port=8080)
