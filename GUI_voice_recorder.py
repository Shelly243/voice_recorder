import sounddevice
from scipy.io.wavfile import write
from tkinter import *
from tkinter.messagebox import showinfo, showwarning
from tkinter.filedialog import askdirectory

add = ""  # address


def file_path():
    global add
    add = askdirectory()


def save_file():
    global add
    try:
        time = int(sec.get())
        addr = add + "/" + "demo.wav"
        showinfo(title="Start", message="Recording Started")
        recording = sounddevice.rec((time * 44100), samplerate=44100, channels=2)
        sounddevice.wait()
        write("demo.wav", 44100, recording)
        showinfo(title="End", message="Recording Ended")
    except:
        showwarning(title="Time", message="Wrong Format of Time")


def main_window():
    global sec
    win = Tk()
    win.geometry("300x250")
    win.resizable(False, False)
    win.title("My Voice Recorder")
    win.config(bg="lightgray")

    label1 = Label(
        win,
        text="Recording Duration (seconds):",
        font=("Arial", 14),
        bg="lightgray",
        fg="black",
    )
    label1.place(x=10, y=50, height=30, width=280)

    sec = Entry(win, font=("Arial", 20))
    sec.place(x=10, y=90, height=50, width=280)

    start = Button(
        win,
        text="Start Recording",
        font=("Arial", 12),
        command=save_file,
        bg="lightgreen",
    )
    start.place(x=50, y=150, height=50, width=200)

    win.mainloop()


main_window()
