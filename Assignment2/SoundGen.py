import wave
import numpy as np

def sinPhase(f, framerate, time):
    nframes = time * framerate
    t = np.linspace(0, time, num=nframes)
    phase = 2 * np.pi * f * t
    return np.sin(phase)