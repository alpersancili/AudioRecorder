import sounddevice
import tkinter
from scipy.io.wavfile import write

voice_file = "C:/Users/alper/OneDrive/Masaüstü/voice.wav"

def record():
    sr = 44100
    seconds = 5
    record_voice = sounddevice.rec(sr * seconds, samplerate=sr, channels=2)
    sounddevice.wait()
    write(voice_file, sr, record_voice)

window = tkinter.Tk()
window.title("VOICE RECORDER")
window.minsize(width=400, height=400)

btn = tkinter.Button(text="Record", command=record, bg="green")
btn.config(height=3, width=10)
btn.place(x=170, y=150)

window.mainloop()