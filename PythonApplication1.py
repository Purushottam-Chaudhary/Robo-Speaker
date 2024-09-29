import pyttsx3
import tkinter as tk

def speak(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)
    engine.say(text)
    engine.runAndWait()

def on_button_click():
    text = entry.get()
    if text:
        speak(text)

# Create GUI
root = tk.Tk()
root.title("RoboSpeaker")

# Create an input field
entry = tk.Entry(root, width=50)
entry.pack(pady=20)

# Create a button to trigger speech
button = tk.Button(root, text="Speak", command=on_button_click)
button.pack(pady=10)

root.mainloop()
