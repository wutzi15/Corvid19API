####Stolen code from https://flask.palletsprojects.com/en/1.1.x/patterns/fileuploads/

from flask import Flask, escape, request
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from flask import *
from handleUpload import handle_file
app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == "csv"

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            handle_file(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect('/success')

    return '''
    <!doctype html>
    <title>New Data</title>
    <h1>Upload new data</h1>
        Use csv format.
     <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''

@app.route('/success')
def upload_success():
     return render_template("success.html")

#url_for('upload_file', filename=filename)