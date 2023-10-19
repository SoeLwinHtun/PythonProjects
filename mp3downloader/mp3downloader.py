import os
import tkinter as tk
from tkinter import filedialog
from pytube import YouTube
import requests
from threading import Thread

#simple youtube downloader that will download youtube videos in mp3 format, it is good to notice that pytube can't download the videos that are age restricted.

def download_video():
    url = url_entry.get()
    destination = destination_entry.get()

    if not destination:
        destination = '.'

    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()

    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    success_label.config(text=yt.title + " has been successfully downloaded.")
    url_entry.delete(0, tk.END)  # Clear the URL entry field
    destination_entry.delete(0, tk.END)  # Clear the destination entry field

def browse_directory():
    folder = filedialog.askdirectory()
    destination_entry.delete(0, tk.END)
    destination_entry.insert(0, folder)

def download_with_progress():
    url = url_entry.get()
    destination = destination_entry.get()

    if not destination:
        destination = '.'

    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    total_size = video.filesize

    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

    success_label.config(text=yt.title + " has been successfully downloaded.")
    url_entry.delete(0, tk.END)  # Clear the URL entry field
    destination_entry.delete(0, tk.END)  # Clear the destination entry field

window = tk.Tk()
window.title("YouTube to MP3 Downloader")

url_label = tk.Label(window, text="Enter the URL of the video you want to download:")
url_label.pack()

url_entry = tk.Entry(window, width=40)
url_entry.pack()

destination_label = tk.Label(window, text="Enter the destination (leave blank for the current directory):")
destination_label.pack()

destination_entry = tk.Entry(window, width=40)
destination_entry.pack()

browse_button = tk.Button(window, text="Browse", command=browse_directory)
browse_button.pack()

download_button = tk.Button(window, text="Download", command=download_with_progress)
download_button.pack()

success_label = tk.Label(window, text="", fg="green")
success_label.pack()

window.mainloop()
