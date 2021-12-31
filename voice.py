from controller import Controller
from controller import cols_to_col
import sounddevice as sd
import numpy as np

con = Controller()

def print_sound(indata, outdata, frames, t, status):
    volume_norm = np.linalg.norm(indata) ** 3
    volume_norm /= 40
    volume_norm = min(volume_norm, 1)
    if volume_norm > .1:
        con.send(0xb19cd9, dim=volume_norm, wait=50)
    else:
        con.send(0, dim=0, wait=50)

with sd.Stream(callback=print_sound):
    sd.sleep(75000)
