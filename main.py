
from tkinter import *
from tkinter import Tk, font

import requests

root = Tk()
root.geometry("2880x1620")
root.title("AI CHATBOT")
background_color="#c9b497"
root.configure(background=background_color)
questionVar = StringVar()

def ask():
    print("Generating Answer")
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=AIzaSyAsX29Tx_fYsklapse_jwRe2msFpaiD7e8"
    question = questionVar.get()
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": question}
                ]
            }
        ]
    }
    response = requests.post(url, json=payload)
    data = response.json()

    answer = data['candidates'][0]['content']['parts'][0]['text']
    
    textBox.delete("1.0", END)
    textBox.insert(END, answer)


textBox = Text(root, height=30, width=160, font=('Microsoft YaHei Light', 14, "bold"))
textBox.pack()

questionLabel = Label(text="Enter your question:", font=('Microsoft YaHei Light', 14, "bold"))
questionLabel.pack()

questionEntry = Entry(root, textvariable=questionVar, font=('Microsoft YaHei Light', 14, "bold"), background='grey')
questionEntry.pack()

askButton = Button( text="Generate Response", command=ask, font=("Microsoft YaHei Light", 14, "bold"))
askButton.pack()





root.mainloop()

