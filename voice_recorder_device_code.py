import sounddevice
from scipy.io.wavfile import write


def savefile(sec):
    print("Start Recording...")
    # voice recording sample rates are 44.1 kHz and 48 kHz
    recording = sounddevice.rec((sec * 44100), samplerate=44100, channels=2)
    sounddevice.wait()
    write("demo.wav", 44100, recording)
    print("End Recording...")


savefile(10)
