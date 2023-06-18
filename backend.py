from flask import Flask
from flask import request
from flask import render_template, send_from_directory
import base64
import openai
app = Flask(__name__)

OPENAI_KEY = "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"
OPENAI_API_URL = "https://api.openai.com/v1"
openai.api_key = OPENAI_KEY
openai.api_base = OPENAI_API_URL

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/resources/<path:path>', methods=['GET'])
def resources(path):
    return send_from_directory('resources', path)

@app.route('/transcribe', methods=['POST'])
def post_audio_file():
    file = request.json['data']
    print(file)
 
    decoded_bytes = base64.b64decode(file)

    #convertBase64(file)
    with open('music.webm', 'wb') as wav_file:
        wav_file.write(decoded_bytes)

    audio_file = open('music.webm', "rb")
  
    transcript = openai.Audio.transcribe('whisper-1',audio_file)
    
    return transcript



if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
