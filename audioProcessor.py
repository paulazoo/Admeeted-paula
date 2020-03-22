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

fs = 44100  # sample rate, 44.1 kHz
seconds = 3  # duration of recording, 3 seconds

my_recording = sd.rec(seconds * fs, samplerate=fs, channels=2)
sd.wait()  # wait until recording is finished

write('output.wav', fs, my_recording)

#read and plot the following data
Fs, data = read("output.wav")
data = data[:,0]

plt.figure()
plt.plot(data)
plt.show()