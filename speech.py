import pyttsx3
import playsound
import threading
from time import sleep
from threading import Thread

beat_to_play = r"C:\Users\DELL\Desktop\J-Component\New folder (4)\beat.mp3"

slowdown_rate = 5
intro = 10


def play_mp3(path):
     playsound.playsound(path)

def cb(name):
    print(name)

engine = pyttsx3.init()
engine.connect('started-utterance', cb)

def letters(input):
    valids = []
    for character in input:
        if character.isalpha() or character == "," or character == "'" or character == " ":
            valids.append(character)
    return ''.join(valids)

lyrics = open("neural_rap.txt").read().split("\n")
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - slowdown_rate)
voices = engine.getProperty('voices')
engine.setProperty('voice','english-us')

wholesong = ""
for i in lyrics:
    wholesong = wholesong + i + " ... "
    

def sing(line):
    engine.say(line,name=line)
    a = engine.runAndWait()

def beat():
    play_mp3(beat_to_play)


Thread(target=beat).start()
sleep(intro)
lines = wholesong.split(" ... ")
for i in lines:
    sing(i)