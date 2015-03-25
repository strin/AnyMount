from flask import *
import pdb
import webbrowser
import threading
import json
import os, sys

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
        return render_template('programmer.html', mounts=db.mounts)
    except Exception as e:
        print "error:", e

@app.route("/user")
def user():
    try:
        return render_template('user.html', mounts=db.mounts)
    except Exception as e:
        print "error:", e

def open_webbrowser():
    webbrowser.open('http://127.0.0.1:8080/programmer')

@app.route('/create_mount', methods=['POST']) 
def create_mount():
  try:
    path = request.form['dir'].decode('utf-8')
    path = json.loads(path)
    path = dropbox.strip_path(path)

    names = request.form['names'].decode('utf-8')
    names = json.loads(names)

    links = request.form['links'].decode('utf-8')
    links = json.loads(links)
    links = dropbox.make_raw_links(links)

    mnt = mountdb.Mount(path, names, links, selected = False)
    db.mount(mnt)
    db.save()

    return jsonify(status='ok')
  except Exception as e:
    print "error:", e

@app.route('/delete_mount', methods=['POST']) 
def delete_mount():
  try:
    remove_id = int(request.form['id'])
    db.unmount(remove_id)
    db.save()

    return jsonify(status='ok')
  except Exception as e:
    print "error:", e

@app.route('/check_mount', methods=['POST']) 
def check_mount():
  try:
    check_id = int(request.form['id'])
    checked = json.loads(request.form['checked'])
    db.check(check_id, checked)
    db.save()

    return jsonify(status='ok')
  except Exception as e:
    print 'error:', e

@app.route('/download', methods=['POST', 'GET']) 
def download():
  try:
    for mount in db.mounts:
      if mount.selected == True:
        path = dropbox.strip_path(mount.path)
        dropbox.download(mount.names, mount.links, path)
  except Exception as e:
    print 'error:', e

if __name__ == "__main__":
    thread = threading.Thread(target = open_webbrowser)
    # thread.start()
    app.run('127.0.0.1', port=8080)
