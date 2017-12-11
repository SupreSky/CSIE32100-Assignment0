import wave
import numpy as np

def sinPhase(f, framerate, time):
    nframes = time * framerate
    t = np.linspace(0, time, num=nframes)
    phase = 2 * np.pi * f * t
    return np.sin(phase)

def note2(num):
    if int(num) == 1:
        freq = 65
    elif int(num) == 2:
        freq = 73
    elif int(num) == 3:
        freq = 82
    elif int(num) == 4:
        freq = 87
    elif int(num) == 5:
        freq = 98
    elif int(num) == 6:
        freq = 110
    elif int(num) == 7:
        freq = 124
    else:
        freq = 10**9
        print ("ERROR!!")
    return freq

def note4(num):
    if int(num) == 1:
        freq = 262
    elif int(num) == 2:
        freq = 294
    elif int(num) == 3:
        freq = 330
    elif int(num) == 4:
        freq = 349
    elif int(num) == 5:
        freq = 393
    elif int(num) == 6:
        freq = 440
    elif int(num) == 7:
        freq = 494
    else:
        freq = 10**9
        print ("ERROR!!")
    return freq