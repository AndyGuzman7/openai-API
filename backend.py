from flask import Flask
from flask import request
from flask import render_template, send_from_directory
from uuid import uuid4
import base64
import openai
import pygame
app = Flask(__name__)

#OPENAI_KEY = "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"
#OPENAI_API_URL = "https://api.openai.com/v1"
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

def convertBase64(base64_encoded_sound_data):
    

    pygame.mixer.init(frequency=8000, size=8, channels=1, allowedchanges=0)
    sound_data = base64.b64decode(base64_encoded_sound_data)
    sound = pygame.mixer.Sound(sound_data)
    ch = sound.play(loops=50)
    while ch.get_busy():
        pygame.time.wait(100)

if __name__ == '__main__':
    app.run('0.0.0.0', 8000)
