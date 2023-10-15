import os
import pygame
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class MusicPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Music Player")

        self.playlist = []
        self.current_track = 0
        self.paused = False

        pygame.mixer.init()

        # Create GUI elements
        self.load_button = tk.Button(root, text="Load Songs", command=self.load_songs)
        self.play_button = tk.Button(root, text="Play", command=self.play_music)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_music)
        self.stop_button = tk.Button(root, text="Stop", command=self.stop_music)
        self.next_button = tk.Button(root, text="Next", command=self.next_track)
        self.prev_button = tk.Button(root, text="Previous", command=self.prev_track)

        self.playlistbox = ttk.Treeview(root, columns=("Name", "Path"), show="headings")
        self.playlistbox.heading("Name", text="Name")
        self.playlistbox.heading("Path", text="Path")
        self.playlistbox.column("Name", width=200)
        self.playlistbox.column("Path", width=400)

        self.current_label = tk.Label(root, text="Currently Playing: ", font=("Helvetica", 14, "bold"))
        self.current_track_label = tk.Label(root, text="", font=("Helvetica", 12, "italic"))

        # Layout
        self.load_button.grid(row=0, column=0, columnspan=6, pady=10)
        self.playlistbox.grid(row=1, column=0, columnspan=6, padx=10, pady=10, sticky="nsew")
        self.play_button.grid(row=2, column=0, padx=5, pady=10)
        self.pause_button.grid(row=2, column=1, padx=5, pady=10)
        self.stop_button.grid(row=2, column=2, padx=5, pady=10)
        self.prev_button.grid(row=2, column=3, padx=5, pady=10)
        self.next_button.grid(row=2, column=4, padx=5, pady=10)
        self.current_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.current_track_label.grid(row=3, column=1, columnspan=5, padx=10, pady=5, sticky="w")

        root.grid_rowconfigure(1, weight=1)
        root.grid_columnconfigure(0, weight=1)

    def load_songs(self):
        directory = filedialog.askdirectory()
        if directory:
            self.playlistbox.delete(*self.playlistbox.get_children())
            self.playlist = [os.path.join(directory, song) for song in os.listdir(directory) if song.endswith('.mp3')]
            for song in self.playlist:
                self.playlistbox.insert("", "end", values=(os.path.basename(song), song))

    def play_music(self):
        if not self.paused:
            selected_item = self.playlistbox.selection()
            if selected_item:
                self.current_track = self.playlist.index(self.playlistbox.item(selected_item)["values"][1])
                pygame.mixer.music.load(self.playlist[self.current_track])
                pygame.mixer.music.play()
                self.current_track_label.config(text=os.path.basename(self.playlist[self.current_track]))
        else:
            pygame.mixer.music.unpause()
        self.paused = False

    def pause_music(self):
        pygame.mixer.music.pause()
        self.paused = True

    def stop_music(self):
        pygame.mixer.music.stop()
        self.current_track_label.config(text="")

    def next_track(self):
        if self.playlist:
            self.stop_music()
            self.current_track = (self.current_track + 1) % len(self.playlist)
            self.play_music()

    def prev_track(self):
        if self.playlist:
            self.stop_music()
            self.current_track = (self.current_track - 1) % len(self.playlist)
            self.play_music()

if __name__ == '__main__':
    root = tk.Tk()
    player = MusicPlayer(root)
    root.geometry("600x400")  # Initial window size
    root.mainloop()
