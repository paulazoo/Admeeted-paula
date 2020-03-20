#first part of audioProcessor.py

#set up "bot" in the Google Hangout... record the audio

#process what the data means? how much silence? quiet (low dB?)

import sounddevice as sd
from scipy.io.wavfile import write

#the following records audio from your microphone and saves it as a .WAV file
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)

