from flask import Flask
from flask import request
from flask import render_template, send_from_directory
from uuid import uuid4

import base64
import json
import openai
import os

app = Flask(__name__)

#OPENAI_KEY = # Must complete this part
#OPENAI_API_URL = # Must complete this part

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/resources/<path:path>', methods=['GET'])
def resources(path):
    return send_from_directory('resources', path)

@app.route('/transcribe', methods=['POST'])
def post_audio_file():
    # You must complete the full implementation for this
    return None

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
