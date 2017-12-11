import wave
import numpy as np
import waveProc as wProc

def cosPhase(f, framerate, time, modulation):
    nframes = time * framerate
    t = np.linspace(0, time, num=nframes)
    
    phase = 2 * np.pi * f * t
    ans = np.sin(phase) * np.cos( 2 * np.pi * modulation * t)
    return ans

print("歌曲清單：")
print("[1] Twinckle Twinckle little star")
print("[2] 周杰倫 - 我不配")

f0 = open(wProc.songList(input()))
modulation = int(input("請輸入 f，f = 100, 500, 800："))
##f0 = open("twinckle.txt")
##f0 = open("Not Good Enough For You.txt")
sheet = f0.read()
f = wave.open(r"Mod.wav", "wb")

f.setnchannels(1)
f.setsampwidth(2)
f.setframerate(wProc.framerate)

for i in range(0, len(sheet)):
    if sheet[i] == "-":
        continue
    nowDuration = wProc.time
    if i < len(sheet)-1 and sheet[i+1] == "-" :
        nowDuration = wProc.time * 2
    
    wave_data = cosPhase(wProc.note2(sheet[i]),  wProc.framerate, nowDuration, modulation)
    wave_data = wave_data * 10000 / 2
    wave_data = wave_data.astype(np.short)
    
    wave_data2 = cosPhase(wProc.note4(sheet[i]),  wProc.framerate, nowDuration, modulation)
    wave_data2 = wave_data2 * 10000 / 2
    wave_data2 = wave_data2.astype(np.short)
    
    ADD = wave_data + wave_data2
    
    f.writeframes(ADD.tostring())
    
    if i < len(sheet)-1 and sheet[i+1] == sheet[i]:
        f.writeframes(wProc.zeroPhase().tostring())


f.close()
f0.close()