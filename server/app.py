#!/bin/python3
import os
from flask import Flask, send_from_directory, request, url_for, redirect
from werkzeug.utils import secure_filename
from wd import WatchDog
import shutil

app = Flask(__name__)
PUSH_TO_DROID = '/home/aiman/Desktop/push-to-droid'
UPLOAD_FOLDER = '/home/aiman/Desktop/get-from-droid'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
UPDATES_AVAILABLE=False


@app.route("/")
def index():
    return "<p>Server is up and running.</p>"

@app.route("/check-updates")
def check_updates():
    return str(UPDATES_AVAILABLE)

@app.route("/download-file")
def download_file():
    
    """
    Actually sends zipped dir
    """
    global UPDATES_AVAILABLE
    UPDATES_AVAILABLE = False

    path = shutil.make_archive("packet", "zip", PUSH_TO_DROID)
    return send_from_directory(os.path.split(path)[0], os.path.split(path)[1])


@app.route('/upload-file', methods=['GET', 'POST'])
def upload_file():

    if request.method == 'POST':

        file = request.files['upload']
        
        if file.filename == '':         
            return "empty file"

        if file and file.filename:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return "ok"

    return "error uploading file", 400

def set_updates_available():
    global UPDATES_AVAILABLE
    UPDATES_AVAILABLE = True

if __name__ == '__main__':

    def on_anything(e):
        # # ignore hidden and tmp files
        # if (e.src_path[0] ==  ".")  or ("swp" in e.src_path):
        #     return 
        set_updates_available()

    wd = WatchDog.get(PUSH_TO_DROID, on_created=on_anything, on_modified=on_anything)
    wd.start()

    app.run(port=8000 ).start()