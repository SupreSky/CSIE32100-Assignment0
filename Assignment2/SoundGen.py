import wave
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
    f.writeframes(X.tostring())

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

print("歌曲清單：")
print("[1] Twinckle Twinckle little star")
print("[2] 周杰倫 - 我不配")

f0 = open(songList(input()))
##f0 = open("twinckle.txt")
##f0 = open("Not Good Enough For You.txt")
sheet = f0.read()
f = wave.open(r"Song.wav", "wb")

f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(framerate)

for i in range(0, len(sheet)):
    if sheet[i] == "-":
        continue
    nowDuration = time
    if i < len(sheet)-1 and sheet[i+1] == "-" :
        nowDuration = time * 2
        
    
    sinus_f_sweep = sinPhase(note2(sheet[i]),  framerate, nowDuration)
    wave_data = sinus_f_sweep * 10000 / 2
    wave_data = wave_data.astype(np.short)
    
    sinus_f_sweep2 = sinPhase(note4(sheet[i]),  framerate, nowDuration)
    wave_data2 = sinus_f_sweep2 * 10000 / 2
    wave_data2 = wave_data2.astype(np.short)
    
    ADD = wave_data + wave_data2
    
    f.writeframes(ADD.tostring())
    
    if i < len(sheet)-1 and sheet[i+1] == sheet[i]:
        zeroPhase()


f.close()
f0.close()