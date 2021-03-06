__author__ = 'PRITHVIRAJ'
import math
import pyaudio
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from tkinter import *
root = tk.Tk()
#root.state('zoomed')


#Variables :
f1 = tk.Frame()
f2 = tk.Frame()
f3 = tk.Frame()
f4 = tk.Frame()
PyAudio = pyaudio.PyAudio
waveform_select = tk.StringVar()
waveform_select.set("sine")
waveform_select2 = tk.StringVar()
waveform_select2.set("sine")
default_sinefreq = tk.DoubleVar()
default_sinefreq.set(5)
input_freq = tk.DoubleVar()
input_freq.set(440.0)
phase = 0
samplerate = 8000
amplitude = 1
v = tk.IntVar()


def plot_sine1(f,amplitude,phase):
    Fs = 8000
    #f = 5
    phase = phase*1000
    sample = 8000
    x = (np.arange(sample))+phase
    y = ((np.sin(2 * np.pi * f * (x) / Fs))*amplitude)
    plt.plot(x,y)
    plt.ylabel('voltage(V)')
    plt.xlabel('sample(n)')
    plt.show()


def plot_triangle(freq,amplitude,phase):
    n=5
    xmin=0+phase
    xmax=10+phase
    ymin=-2-amplitude
    ymax=2+amplitude
    offset=0.5
    x=(np.sort(np.concatenate([np.arange(xmin, xmax)-1E-6,np.arange(xmin, xmax)+1E-6])))
    y=(np.array(x+n+offset,dtype=int)%2)*amplitude
    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid()
    plt.show()

def plot_square(freq,amplitude,phase):

    n=5
    xmin=0+phase
    xmax=10+phase
    ymin=-2-amplitude
    ymax=2+amplitude
    offset=1
    x=np.sort(np.concatenate([np.arange(xmin, xmax)-1E-6,np.arange(xmin, xmax)+1E-6]))

    y=((np.array(x+n+offset,dtype=int)%2)*amplitude)

    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid()
    plt.show()

def plot_noise1(f,amplitude,phase):
    Fs = 8000
    #f = 5
    phase = phase*1000
    sample = 8000
    x = (np.arange(sample))+phase
    y = (float(amplitude) * random.uniform(-1, 1) for _ in count(0))
    plt.plot(x,y)
    plt.ylabel('voltage(V)')
    plt.xlabel('sample(n)')
    plt.show()


def waveform_selected1(*args):
    waveform__select = waveform_select.get()
    return(waveform__select)

def waveform_selected2():
    waveform__select2 = waveform_select2.get()
    return(waveform__select2)

def play_sine1(freq,amplitude,duration = 2.0):
    p = pyaudio.PyAudio()

    volume = 1.0     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    #duration = 2.0   # in seconds, may be float
    #freq = 300.0        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = ((np.sin(2*np.pi*np.arange(fs*duration)*freq/fs))*amplitude).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples)
    print(samples)
    stream.stop_stream()
    stream.close()

    p.terminate()

def play_sawtooth1(freq,amplitude,phase):
    p = pyaudio.PyAudio()

    volume = 1.0     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 2.0   # in seconds, may be float
    #freq = 300.0        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = ((signal.sawtooth(2*np.pi*np.arange(fs*duration)*freq/fs))*amplitude).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)
    print(samples)
    stream.stop_stream()
    stream.close()

    p.terminate()

def play_square1(freq,amplitude,phase):
    p = pyaudio.PyAudio()

    volume = 1.0     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 2.0   # in seconds, may be float
    #freq = 300.0        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = ((signal.square(2*np.pi*np.arange(fs*duration)*freq/fs))*amplitude).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)
    print(samples)
    stream.stop_stream()
    stream.close()

    p.terminate()

def play_osc1():
    waveform_selected = waveform_selected1()
    freq = float(input_freq.get())
    phase = (phase_osc1.get())
    amplitude = amp_osc1.get()
    if(waveform_selected == "sine"):
        play_sine1(freq,amplitude)

    if(waveform_selected== "sawtooth"):
        play_sawtooth1(freq,amplitude)

    if(waveform_selected== "square"):
        play_square1(freq,amplitude)


def play_osc1_arpg():
    waveform_selected = waveform_selected1()
    freq = float(input_freq.get())
    phase = (phase_osc1.get())
    amplitude = amp_osc1.get()
    if(waveform_selected == "sine"):
        play_sine1(freq,amplitude,0.5)

    if(waveform_selected== "sawtooth"):
        play_sawtooth1(freq,amplitude,0.5)

    if(waveform_selected== "square"):
        play_square1(freq,amplitude,0.5)


def play_osc2():
    waveform_selected = waveform_selected1()
    freq = float(input_freq.get())
    phase = (phase_osc1.get())
    amplitude = amp_osc1.get()
    if(waveform_selected == "sine"):
        play_sine1(freq,amplitude)

    if(waveform_selected== "sawtooth"):
        play_sawtooth1(freq,amplitude)

    if(waveform_selected== "square"):
        play_square1(freq,amplitude)

def plot_osc1():
    waveform_selected = waveform_selected1()
    freq = float(input_freq.get())
    phase = (phase_osc1.get())
    amplitude = amp_osc1.get()
    if(waveform_selected == "sine"):
        plot_sine1(freq,amplitude,phase)

    if(waveform_selected == "triangle"):
        plot_triangle(freq,amplitude,phase)

    if(waveform_selected=="square"):
        plot_square(freq,amplitude,phase)

    if(waveform_select=="noise"):
        plot_noise1(freq,amplitude,phase)

def plot_osc2():
    waveform_selected = waveform_selected1()
    freq = float(input_freq.get())
    phase = (phase_osc1.get())
    amplitude = amp_osc1.get()
    if(waveform_selected == "sine"):
        plot_sine1(freq,amplitude,phase)

    if(waveform_selected == "triangle"):
        plot_triangle(freq,amplitude,phase)

    if(waveform_selected=="square"):
        plot_square(freq,amplitude,phase)




def change_parameters(note,octave,keypressed=0):
    if(note=="C" and octave==4 or keypressed=="a"):
        input_freq.set(261.6255653005986)
        amp_osc1.set(1)

    if(note=="D" and octave==4 or keypressed=="s"):
        input_freq.set(293.6647679174076)
        amp_osc1.set(1)

    if(note=="E" and octave==4 or keypressed=="d"):
        input_freq.set(329.6275569128699)
        amp_osc1.set(1)

    if(note=="F" and octave==4 or keypressed=="f"):
        input_freq.set(349.2282314330039)
        amp_osc1.set(1)

    if(note=="G" and octave==4 or keypressed=="g"):
        input_freq.set(391.99543598174927)
        amp_osc1.set(1)

    if(note=="A" and octave==4 or keypressed=="h"):
        input_freq.set(440.0)
        amp_osc1.set(1)

    if(note=="B" and octave==4 or keypressed=="j"):
        input_freq.set(493.8833012561241)
        amp_osc1.set(1)

    if(note=="C" and octave==5 or keypressed=="k"):
        input_freq.set(523.2511306011972)
        amp_osc1.set(1)


    play_osc1()

def change_parameters_arpg(note,octave,keypressed=0):
    if(note=="C" and octave==4 or keypressed=="a"):
        input_freq.set(261.6255653005986)
        amp_osc1.set(1)

    if(note=="D" and octave==4 or keypressed=="s"):
        input_freq.set(293.6647679174076)
        amp_osc1.set(1)

    if(note=="E" and octave==4 or keypressed=="d"):
        input_freq.set(329.6275569128699)
        amp_osc1.set(1)

    if(note=="F" and octave==4 or keypressed=="f"):
        input_freq.set(349.2282314330039)
        amp_osc1.set(1)

    if(note=="G" and octave==4 or keypressed=="g"):
        input_freq.set(391.99543598174927)
        amp_osc1.set(1)

    if(note=="A" and octave==4 or keypressed=="h"):
        input_freq.set(440.0)
        amp_osc1.set(1)

    if(note=="B" and octave==4 or keypressed=="j"):
        input_freq.set(493.8833012561241)
        amp_osc1.set(1)

    if(note=="C" and octave==5 or keypressed=="k"):
        input_freq.set(523.2511306011972)
        amp_osc1.set(1)


    play_osc1_arpg()



def stop_sound():
    pass

def keys():
        white_key_width = 30
        white_key_height = 110
        black_key_width = white_key_width * 0.5
        black_key_height = white_key_height * 0.6
        num_octaves = 5
        first_octave = 2
        x_offset = 3
        y_offset = 20
        canvas = tk.Canvas( width=white_key_width*num_octaves*7+2, height=white_key_height+10+y_offset, borderwidth=0)
        # white keys:
        for key_nr, key in enumerate("CDEFGAB"*num_octaves):
            octave = first_octave+key_nr//7
            def key_pressed(event, note=key, octave=octave):
                force = min(white_key_height, event.y*1.08)/white_key_height   # @todo control output volume, unused for now...
                change_parameters(note,octave)
                print(note,octave)
            def key_released(event, note=key, octave=octave):
                stop_sound()
            x = key_nr * white_key_width
            key_rect = canvas.create_rectangle(x+x_offset, y_offset, x+white_key_width+x_offset, white_key_height+y_offset, fill="white", outline="gray50", width=1, activewidth=2)
            canvas.tag_bind(key_rect, "<ButtonPress-1>", key_pressed)
            canvas.tag_bind(key_rect, "<ButtonRelease-1>", key_released)
            canvas.create_text(x+white_key_width/2+2, 1, text=key, anchor=tk.N, fill="gray")
            if 10 <= key_nr <= 21:
                keychar = "qwertyuiop[]"[key_nr-10]
                canvas.create_text(x+white_key_width/2+2, white_key_height+3, text=keychar, anchor=tk.N, fill="maroon")
                pass
        # black keys:
        for key_nr, key in enumerate((["C#", "D#", None, "F#", "G#", "A#", None]*num_octaves)[:-1]):
            if key:
                octave = first_octave + key_nr // 7
                def key_pressed(event, note=key, octave=octave):
                    force = min(black_key_height, event.y * 1.1) / black_key_height   # @todo control output volume, unused for now...
                    pass
                def key_released(event, note=key, octave=octave):
                    pass
                x = key_nr * white_key_width + white_key_width*0.75
                key_rect = canvas.create_rectangle(x+x_offset, y_offset, x+black_key_width+x_offset, black_key_height+y_offset, fill="black", outline="gray50", width=1, activewidth=2)
                canvas.tag_bind(key_rect, "<ButtonPress-1>", key_pressed)
                canvas.tag_bind(key_rect, "<ButtonRelease-1>", key_released)
        canvas.pack(padx=10,side="bottom")


def keyboard():
    def keyup(e):
        print ('up', e.char)
    def keydown(e):
        pressed = e.char
        change_parameters(0,0,pressed)


    f3.bind("<KeyPress>", keydown)
    f3.bind("<KeyRelease>", keyup)
    f3.pack()
    f3.focus_set()


def checkBoxState():
    checked = var1.get()
    if(checked ==1):
        print(checked)
        e1.config(state=DISABLED)
        e2.config(state=DISABLED)
        keyboard()

def effects():
    print(v.get())
    if v.get()==1:
        arpeggio()

def arpeggio():
    for i in range(3):
        change_parameters_arpg("C",4)
        change_parameters_arpg("E",4)
        change_parameters_arpg("G",4)


#Oscillator 1:
row = 0
tk.Label(f1,text="  Oscillator 1 :").grid(row=row,column=0,sticky=tk.E)
row += 2
waveforms = ["sine", "triangle", "pulse", "sawtooth", "square","noise"]
tk.Label(f1, text="waveform").grid(row=row, column=0, sticky=tk.E)
waveform = tk.OptionMenu(f1, waveform_select, *waveforms, command=waveform_selected1)
waveform["width"] = 10
waveform.grid(row=row, column=1)
row+=1
tk.Label(f1, text="frequency").grid(row=row, column=0, sticky=tk.E)
e1 = tk.Entry(f1,width=10,textvariable=input_freq)
e1.insert(10,str(default_sinefreq))
e1.grid(row=row,column=1)
row +=1
tk.Label(f1, text="amp").grid(row=row, column=0, sticky=tk.E)
amp_osc1 = tk.Scale(f1, from_=0, to=1, orient=tk.HORIZONTAL)
amp_osc1.grid(row=row,column=1)
row +=1
tk.Label(f1, text="phase").grid(row=row, column=0, sticky=tk.E)
phase_osc1 = tk.Scale(f1, from_=0, to=5, orient=tk.HORIZONTAL)
phase_osc1.grid(row=row,column=1)
row += 1
button_plotosc1 = tk.Button(f1,text="PLOT",command=plot_osc1)
button_plotosc1.grid(row=row,column=0)
button_plotosc1 = tk.Button(f1,text="PLAY",command=play_osc1)
button_plotosc1.grid(row=row,column=1)

#checkbox for keyboard
row +=1
var1 = IntVar()
Checkbutton(f1, text="KEYBOARD", variable=var1,command=checkBoxState).grid(row=row,column=0, sticky=tk.E)


#Oscillator 2:
row = 0
tk.Label(f2,text="  Oscillator 2 :").grid(row=row,column=2,sticky=tk.E)
row += 2
waveforms2 = ["sine", "triangle", "pulse", "sawtooth", "square","noise"]
tk.Label(f2, text="waveform").grid(row=row, column=2, sticky=tk.E)
waveform2 = tk.OptionMenu(f2, waveform_select2, *waveforms2, command=waveform_selected2)
waveform2["width"] = 10
waveform2.grid(row=row, column=3)
row+=1
tk.Label(f2, text="frequency").grid(row=row, column=2, sticky=tk.E)
e2 = tk.Entry(f2)
e2.insert(10,str(default_sinefreq))
e2.grid(row=row,column=3)
row +=1
tk.Label(f2, text="amp").grid(row=row, column=2, sticky=tk.E)
amp_osc2 = tk.Scale(f2, from_=0, to=50, orient=tk.HORIZONTAL)
amp_osc2.grid(row=row,column=3)
row +=1
tk.Label(f2, text="phase").grid(row=row, column=2, sticky=tk.E)
phase_osc2 = tk.Scale(f2, from_=0, to=50, orient=tk.HORIZONTAL)
phase_osc2.grid(row=row,column=3)
row += 1
button_plotosc2 = tk.Button(f2,text="PLOT",command=play_osc2)
button_plotosc2.grid(row=row,column=2)
button_plotosc2 = tk.Button(f2,text="PLAY",command=play_osc2)
button_plotosc2.grid(row=row,column=3)


#Options for effects
row = 0
tk.Label(f4,text="  Effects :").grid(row=row,column=0,sticky=tk.E)
row += 1
radio = tk.Radiobutton(f4,text="Chords",variable=v,value=1,command=effects)
radio.grid(row=row,column=0,sticky=tk.E)
row += 1
radio = tk.Radiobutton(f4,text="Arpeggio 3",variable=v,value=2,command=effects)
radio.grid(row=row,column=0,sticky=tk.E)



keys()
f1.pack(side=tk.LEFT)
f2.pack(padx=15,side=tk.LEFT)
f4.pack(side=tk.LEFT)

root.mainloop()


