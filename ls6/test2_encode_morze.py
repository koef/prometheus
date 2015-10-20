#!/usr/bin/env python

def encode_morze(text):
    morse_code = {
        "A": "^_^^^",           # ".-"
        "B": "^^^_^_^_^",       # "-..."
        "C": "^^^_^_^^^_^",     # "-.-."
        "D": "^^^_^_^",         # "-.."
        "E": "^",               # "."
        "F": "^_^_^^^_^",       # "..-."
        "G": "^^^_^^^_^",       # "--."
        "H": "^_^_^_^",         # "...."
        "I": "^_^",             # ".."
        "J": "^_^^^_^^^_^^^",   # ".---"
        "K": "^^^_^_^^^",       # "-.-"
        "L": "^_^^^_^_^",       # ".-.."
        "M": "^^^_^^^",         # "--"
        "N": "^^^_^",           # "-."
        "O": "^^^_^^^_^^^",     # "---"
        "P": "^_^^^_^^^_^",     # ".--."
        "Q": "^^^_^^^_^_^^^",   # "--.-"
        "R": "^_^^^_^",         # ".-."
        "S": "^_^_^",           # "..."
        "T": "^^^",             # "-"
        "U": "^_^_^^^",         # "..-"
        "V": "^_^_^_^^^",       # "...-"
        "W": "^_^^^_^^^",       # ".--"
        "X": "^^^_^_^_^^^",     # "-..-"
        "Y": "^^^_^_^^^_^^^",   # "-.--"
        "Z": "^^^_^^^_^_^"      # "--.."
    }

    signal = ""

    for ch in text.upper():
        if ch == " ":
            signal += "____"
        elif ch in morse_code.keys():
            signal += morse_code.get(ch, "") + "___"

    return signal.strip("_")

print encode_morze("errr rre")