from flask import Flask
from flask import request
from flask import render_template, send_from_directory
from uuid import uuid4
import wave
import base64
import json
import openai
import os
import pydub
import pygame
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
    
    # Decodificar el archivo Base64
    decoded_bytes = base64.b64decode(file)

    # Escribir los bytes decodificados en un archivo WAV
    wav_file = wave.open('music.ogg', 'wb') 
    wav_file.setnchannels(2)  # Número de canales (estéreo)
    wav_file.setsampwidth(2)  # Tamaño de muestra en bytes (16 bits)
    wav_file.setframerate(44100)  # Frecuencia de muestreo en Hz
    wav_file.writeframes(decoded_bytes)
    wav_file.close()

    # Reabrir el archivo WAV para realizar la transcripción
    audio_file = open('file2.ogg', "rb")
    # Realiza la transcripción utilizando el archivo WAV temporal
    transcript = openai.Audio.transcribe('whisper-1', audio_file)
    
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
