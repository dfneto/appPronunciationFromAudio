# Import SpeechRecognition library
import speech_recognition as sr
import wave
import os
from pydub import AudioSegment
from pydub.playback import play

path = "/Users/david/DEV/app_pronunciation_files/"
os.system(f"ffmpeg -y -i {path}ramit_seth_talks_at_google.mp4 -ac 1  {path}ramit_seth_talks_at_google_mono.wav")
os.system(f"ffmpeg -y -i {path}ramit_seth_talks_at_google.wav -ss 00:05:00.000 -to 00:05:59.000 {path}ramit_seth_talks_at_google_59s.wav")


pedaco002_audio = AudioSegment.from_file(file=path + "pedaco002.wav")
play(pedaco002_audio)


good_morning = wave.open(f"{path}pedaco001.wav", "r")
frames = good_morning.getnframes()
framerate_gm = good_morning.getframerate()
duration_in_sec = frames / float(framerate_gm)


# extraindo o testo do arquivo quebrado
recognizer = sr.Recognizer()
# Read in audio file
pedaco001_audio_file = sr.AudioFile(f"{path}pedaco001.wav")
play(pedaco001_audio_file)

# Convert from AudioFile to AudioData
with pedaco001_audio_file as source:
    # Record the audio
    pedaco001_data = recognizer.record(source)
    # Check the type
    type(pedaco001_data)

# Transcribe speech using Goole web API
pedaco001_text = recognizer.recognize_google(audio_data=pedaco001_data, language="en-US")




lista = []
pedaco001 = {
    "audio": pedaco001_audio,
    "text": pedaco001_text
}
lista.append(pedaco001)
play(lista[0].get("audio"))




'''
abra o arquivo de áudio
calcule a duração dele
quebre ele em arquivos de 1s
extraia o texto deles
{
    pedaco001:{
        audio: audio_do_pedaco001,
        text: descricao_do_pedaco001
    }
}
'''
descricao_do_pedaco001: ...

