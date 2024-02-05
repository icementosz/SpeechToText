import librosa

import sounddevice as sd
from scipy.io.wavfile import write
import wavio as wv   
import numpy as np

from pythaiasr import asr


# Sampling frequency
freq = 44100

# Recording duration
duration = 5

# Start recorder with the given values of 
# duration and sample frequency
recording = sd.rec(int(duration * freq), samplerate=freq, channels=2)

# Record audio for the given number of seconds
print("เริ่มพูด")
sd.wait()
print("สิ้นสุดการพูด")

# This will convert the NumPy array to an audio
# file with the given sampling frequency
write("recording0.wav", freq, recording)


input_file, sr = librosa.load("recording0.wav", sr=16000)
print(asr(input_file))


#######ทำไม้่ได้
# from pythaitts import TTS

# tts = TTS("lunalist")

# input_text = "ภาษาไทย ง่าย มาก มาก"
# file = tts.tts(input_data, filename="cat.wav")
# IPython.display.Audio(file)