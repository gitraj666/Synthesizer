__author__ = 'PRITHVIRAJ'

import tkinter as tk
root = tk.Tk()

white_key_width = 30
white_key_height = 110
black_key_width = white_key_width * 0.5
black_key_height = white_key_height * 0.6
num_octaves = 5
first_octave = 2
x_offset = 3
y_offset = 20
canvas = tk.Canvas(width=white_key_width*num_octaves*7+2, height=white_key_height+10+y_offset, borderwidth=0)
# white keys:
for key_nr, key in enumerate("CDEFGAB"*num_octaves):
    octave = first_octave+key_nr//7
    x = key_nr * white_key_width
    key_rect = canvas.create_rectangle(x+x_offset, y_offset, x+white_key_width+x_offset, white_key_height+y_offset, fill="white", outline="gray50", width=1, activewidth=2)
    canvas.create_text(x+white_key_width/2+2, 1, text=key, anchor=tk.N, fill="gray")


# black keys:
for key_nr, key in enumerate((["C#", "D#", None, "F#", "G#", "A#", None]*num_octaves)[:-1]):
    if key:
        octave = first_octave + key_nr // 7
        x = key_nr * white_key_width + white_key_width*0.75
        key_rect = canvas.create_rectangle(x+x_offset, y_offset, x+black_key_width+x_offset, black_key_height+y_offset, fill="black", outline="gray50", width=1, activewidth=2)

canvas.pack()



root.mainloop()
