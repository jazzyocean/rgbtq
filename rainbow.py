from controller import Controller
from controller import cols_to_col
import math

con = Controller()


def make_color_gradient(frequency1, frequency2, frequency3,
                        phase1,     phase2,     phase3,
                        center=128, width=127, len=50, wait=75):
    for i in range(len):
        red = math.sin(frequency1*i + phase1) * width + center;
        green = math.sin(frequency2*i + phase2) * width + center;
        blue = math.sin(frequency3*i + phase3) * width + center;
        con.send(cols_to_col(red, green, blue), wait=wait)

make_color_gradient(.01, .01, .01, 0, 2, 4, len=500000, wait=(1/60)*1000)