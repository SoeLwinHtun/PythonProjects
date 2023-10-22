from newspaper import Article
import nltk
from gtts import gTTS
import os
import tkinter as tk


#simple pytho program to convert online article into mp3 file

def convert_to_mp3():
    #load the article
    url = url_entry.get()
    savename = savename_entry.get()
    article = Article(url)
    article.download()
    article.parse()
    nltk.download('punkt')
    article.nlp()

    #extract the text
    articleText = article.text

    language = 'en'

    #create text to speech engine object
    engineObj = gTTS(text = articleText, lang = language, slow = False)

    #file name 
    filename = savename + '.mp3'

    #display message while downloading and converting file
    message_label.config(text="Downloading the mp3 file, please wait...", fg="blue")

    engineObj.save(filename)

    #display message after saving file
    message_label.config(text="File saved successfully!", fg="green")

#GUI window
window = tk.Tk()
window.title("Article to MP3 Converter")
window.geometry("400x200")

#URL input field
url_label = tk.Label(window, text="Article url:")
url_label.pack(pady=10)
url_entry = tk.Entry(window)
url_entry.pack()

#File name input field
savename_label = tk.Label(window, text="Filename:")
savename_label.pack(pady=10)
savename_entry = tk.Entry(window)
savename_entry.pack()

#Convert button
convert_button = tk.Button(window, text="Convert", command=convert_to_mp3)
convert_button.pack(pady=10)

#Message label
message_label = tk.Label(window, text="Article to mp3 converter")
message_label.pack(pady=10)

window.mainloop()
