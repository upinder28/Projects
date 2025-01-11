import tkinter as tk
from tkinter import Text, Label, Button, OptionMenu, StringVar
import speech_recognition as sr
from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play
from googletrans import Translator as GoogleTranslator
import os
import threading as td

# Initialize the recognizer
r = sr.Recognizer()

main = tk.Tk()
main.title("Voiceprint Translator")
main.geometry("940x570")
main.config(bg="#C7F8FF")
main.resizable(0, 0)

lt = ["English", "Hindi", "Tamil", "Gujarati", "Marathi"]
v1 = StringVar(main)
v1.set(lt[0])
v2 = StringVar(main)
v2.set(lt[1])

Label(main, text="Translate Language via Voice Commands", font=("", 18, "bold"), bg="#C7F8FF", fg="black").place(x=240, y=20)

flag = False

can_input = tk.Canvas(main, width=400, height=450, bg="#17C3B2", relief="solid", bd=1, highlightthickness=0)
can_input.place(x=30, y=80)
Label(main, text="Input Box:", font=("", 12, "bold"), bg="#17C3B2", fg="black").place(x=44, y=70)

can_output = tk.Canvas(main, width=400, height=450, bg="#17C3B2", relief="solid", bd=1, highlightthickness=0)
can_output.place(x=490, y=80)
Label(main, text="Output Box:", font=("", 12, "bold"), bg="#17C3B2", fg="black").place(x=780, y=60)

txtbx = Text(main, width=40, height=7, font=("", 12, "bold"), relief="solid", bd=0, highlightthickness=0)
txtbx.place(x=50, y=100)

txtbx2 = Text(main, width=40, height=7, font=("", 12, "bold"), relief="solid", bd=0, highlightthickness=0)
txtbx2.place(x=510, y=100)

def speak():
    global txtbx2
    tx = txtbx2.get("1.0", "end")
    code = ["en", "hi", "ta", "gu", "mr"]
    language = code[lt.index(v2.get())]
    myobj = gTTS(text=tx, lang=language, slow=False)
    try:
        os.remove("temp.mp3")
    except:
        pass
    myobj.save("temp.mp3")
    song = AudioSegment.from_mp3("temp.mp3")
    play(song)

def translate():
    global txtbx, txtbx2
    txtbx2.delete("1.0", "end")
    tx = txtbx.get("1.0", "end-1c")  # Adjusted to exclude the newline character at the end
    code = ["en", "hi", "ta", "gu", "mr"]
    lang = code[lt.index(v2.get())]
    translator = GoogleTranslator()
    translated = translator.translate(tx, src='auto', dest=lang).text
    txtbx2.insert("end", translated)

def detect():
    global flag, txtbx
    while True:
        if flag:
            print("breaked")
            break
        try:
            with sr.Microphone() as source2:
                r.adjust_for_ambient_noise(source2, duration=0.2)
                audio2 = r.listen(source2)
                MyText = r.recognize_google(audio2)
                MyText = MyText.lower()
                txtbx.insert("end", MyText)
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            break
        except sr.UnknownValueError:
            print("Unknown error occurred")
            break

def start():
    global flag, b1
    flag = False
    b1["text"] = "Stop Speaking"
    b1["command"] = stop
    td.Thread(target=detect).start()

def stop():
    global flag, b1
    b1["text"] = "Give Voice Input"
    b1["command"] = start
    flag = True

b1 = Button(main, text="Give Voice Input", font=("", 12, "bold"), width=35, height=1, bg="#FEF9EF", fg="black", command=start, relief="solid", bd=4, highlightthickness=0)
b1.place(x=50, y=250)

Button(main, text="Speak Text", font=("", 12, "bold"), width=35, height=1, bg="#FEF9EF", fg="black", command=speak, relief="solid", bd=4, highlightthickness=0).place(x=510, y=250)

Button(main, text="Translate", font=("", 15, "bold"), width=71, height=3, bg="#FEF9EF", fg="black", command=translate, relief="solid", bd=3, highlightthickness=0).place(x=30, y=446)

Label(main, text="Select Language:", font=("", 12, "bold"), bg="#17C3B2", fg="black").place(x=50, y=300)
Label(main, text="Select Language:", font=("", 12, "bold"), bg="#17C3B2", fg="black").place(x=510, y=300)

o1 = OptionMenu(main, v1, *lt)
o1.config(font=("", 12, "bold"), width=36, bg="#FEF9EF", fg="black", relief="solid", bd=1, highlightthickness=0)
o1.place(x=50, y=340)

o2 = OptionMenu(main, v2, *lt)
o2.config(font=("", 12, "bold"), width=36, bg="#FEF9EF", fg="black", relief="solid", bd=1, highlightthickness=0)
o2.place(x=510, y=340)

main.mainloop()
