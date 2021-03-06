import tkinter as tk
import pygame as pg
import os

HEIGHT = 650
WIDTH = 1100
ALBUM_DIR = "/home/leon/DevelopmentDir/MP3Player/files/songs"
IMG_DIR = "/home/leon/DevelopmentDir/MP3Player/files/images"
sample = ALBUM_DIR + '/music1.mp3'

root = tk.Tk()
root.title("MP3 Player")
pg.init()
pg.mixer.init()


def play():
    if not pg.mixer.music.get_busy():
        pg.mixer.music.load(sample)
        pg.mixer.music.play()
    else:
        pg.mixer.music.unpause()


def stop():
    pg.mixer.music.stop()


def pause():
    pg.mixer.music.pause()


os.chdir(ALBUM_DIR)
songs = os.listdir()
songString = 'Current directory: ' + ALBUM_DIR + ': \n\n\n'
for song in songs:
    songString += song + '\n'

print(songString)

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bg_img = tk.PhotoImage(file=IMG_DIR + "/background.png")
bg_label = tk.Label(canvas, image=bg_img)
bg_label.place(relx=0, rely=0, relwidth=1, relheight=1)

songFrame = tk.Frame(root, bg='#373737')
songFrame.place(relx=0.1, rely=0.05, relwidth=0.8, relheight=0.2)
playIcon = tk.PhotoImage(file=IMG_DIR + '/play.png') #PLAY
playIcon = playIcon.subsample(5)
playButton = tk.Button(songFrame, image=playIcon, command=play)
playButton.place(relx=0, rely=0, relwidth=0.2, relheight=1)
stopIcon = tk.PhotoImage(file=IMG_DIR + '/stop.png') #STOP
stopIcon = stopIcon.subsample(5)
stopButton = tk.Button(songFrame, image=stopIcon, command=stop)
stopButton.place(relx=0.2, rely=0, relwidth=0.2, relheight=1)
pauseIcon = tk.PhotoImage(file=IMG_DIR + '/pause.png') #PAUSE
pauseIcon = pauseIcon.subsample(5)
pauseButton = tk.Button(songFrame, image=pauseIcon, command=pause)
pauseButton.place(relx=0.4, rely=0, relwidth=0.2, relheight=1)
timerLabel = tk.Label(songFrame, text='placeholder')
timerLabel.place(relx= 0.6, rely=0, relwidth=0.4, relheight=1)


songListFrame = tk.Frame(root, bg='#373737')
songListFrame.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)
songListLabel = tk.Label(songListFrame, text=songString)
songListLabel.place(relx=0, rely=0.1, relwidth=1, relheight=1)

root.mainloop()
