from controller import Controller
import time
con = Controller()

# Dictionary representing the morse code chart
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
                    'C':'-.-.', 'D':'-..', 'E':'.',
                    'F':'..-.', 'G':'--.', 'H':'....',
                    'I':'..', 'J':'.---', 'K':'-.-',
                    'L':'.-..', 'M':'--', 'N':'-.',
                    'O':'---', 'P':'.--.', 'Q':'--.-',
                    'R':'.-.', 'S':'...', 'T':'-',
                    'U':'..-', 'V':'...-', 'W':'.--',
                    'X':'-..-', 'Y':'-.--', 'Z':'--..',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ',':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

morseshort = 0xFF0000
morselong  = 0x0000FF
morsespace = 0x000000
chardel    = 100
spacedel   = 500

text = "bad and naughty children get put in the pear wiggler to attone for their crimes".upper()

for c in text:
    if c == " ":
        con.send(morsespace, wait=spacedel)
    else:
        for m in MORSE_CODE_DICT[c]:
            if m == ".":
                con.send(morseshort, wait=chardel)
            elif m == "-":
                con.send(morselong, wait=chardel)
        con.send(morsespace, wait=50)