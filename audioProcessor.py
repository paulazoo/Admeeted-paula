#first part of audioProcessor.py

#set up "bot" in the Google Hangout... record the audio

#process what the data means? how much silence? quiet (low dB?)

import sounddevice as sd
from scipy.io.wavfile import write, read
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import Audio
from numpy.fft import fft, ifft


#the following records audio from your microphone and saves it as a .WAV file
fs = 44100  # Sample rate
seconds = 3  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording)

Fs, data = read("output.wav")
data = data[:,0]
plt.figure()
plt.plot(data)
plt.show()
