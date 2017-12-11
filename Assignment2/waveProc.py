import numpy as np

time = 0.275 # second
framerate = 44000 # Hz

def sinPhase(f, framerate, time):
    nframes = time * framerate
    t = np.linspace(0, time, num=nframes)
    phase = 2 * np.pi * f * t
    return np.sin(phase)

def zeroPhase():
    X = sinPhase(1, framerate, 0.025)
    X = X * 10000 / 2
    X = X.astype(np.short)
    return X

def note2(num):
    num = int(num)
    if num == 1:
        freq = 65
    elif num == 2:
        freq = 73
    elif num == 3:
        freq = 82
    elif num == 4:
        freq = 87
    elif num == 5:
        freq = 98
    elif num == 6:
        freq = 110
    elif num == 7:
        freq = 124
    else:
        freq = 10**9
        print ("ERROR!!")
    return freq

def note4(num):
    num = int(num)
    if num == 1:
        freq = 262
    elif num == 2:
        freq = 294
    elif num == 3:
        freq = 330
    elif num == 4:
        freq = 349
    elif num == 5:
        freq = 393
    elif num == 6:
        freq = 440
    elif num == 7:
        freq = 494
    else:
        freq = 10**9
        print ("ERROR!!")
    return freq

def songList(num):
    num = int(num)
    if num == 1:
        songFile = "twinckle.txt"
    elif num == 2:
        songFile = "Not Good Enough For You.txt"
    else:
        print("songList ERROR!!")
    return songFile