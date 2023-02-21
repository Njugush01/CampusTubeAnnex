from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/music')
def music():
    return render_template('music.html')

@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'No file uploaded'

    file = request.files['file']
    file.save(file.filename)
    return 'File uploaded successfully'
