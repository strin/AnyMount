from flask import *
import pdb
import webbrowser
import threading

app = Flask(__name__)

@app.route("/programmer")
def programmer():
    try:
        return render_template('programmer.html')
    except Exception as e:
        print "error:", e

def open_webbrowser():
    webbrowser.open('http://127.0.0.1:8080/programmer')

if __name__ == "__main__":
    thread = threading.Thread(target = open_webbrowser)
    thread.start()
    app.run('0.0.0.0', port=8080)
