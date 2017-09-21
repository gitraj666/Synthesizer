__author__ = 'PRITHVIRAJ'
import math
import pyaudio
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
root = tk.Tk()


#Variables :
f1 = tk.Frame()
f2 = tk.Frame()
PyAudio = pyaudio.PyAudio
waveform_select = tk.StringVar()
waveform_select.set("sine")
waveform_select2 = tk.StringVar()
waveform_select2.set("sine")
default_sinefreq = tk.DoubleVar()
default_sinefreq.set(5)
input_freq = tk.DoubleVar()
input_freq.set(440.0)
input_phase = tk.DoubleVar()
input_phase.set(0.0)
samplerate = 8000
amplitude = 1

def plot_sine1(f,amplitude):
    Fs = 8000
    #f = 5
    sample = 8000
    x = np.arange(sample)
    y = (np.sin(2 * np.pi * f * x / Fs))*amplitude
    plt.plot(x, y)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.show()


def plot_sawtooth(n=5,xmin=0,xmax=10,ymin=-2,ymax=2,offset=0.5):
    x=np.sort(np.concatenate([np.arange(xmin, xmax)-1E-6,np.arange(xmin, xmax)+1E-6]))
    y=np.array(x+n+offset,dtype=int)%2
    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid()
    plt.show()

def plot_square(n=5,xmin=0,xmax=10,ymin=-2,ymax=2,offset=1):

    x=np.sort(np.concatenate([np.arange(xmin, xmax)-1E-6,np.arange(xmin, xmax)+1E-6]))
    #You can use np.linspace(xmin,xmax,Nx) if you want the intermediate points

    y=np.array(x+n+offset,dtype=int)%2


    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid()
    plt.show()

def waveform_selected1(*args):
    waveform__select = waveform_select.get()
    return(waveform__select)

def waveform_selected2():
    waveform__select2 = waveform_select2.get()
    return(waveform__select2)

def play_sine1():
    p = pyaudio.PyAudio()

    volume = 1.0     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 2.0   # in seconds, may be float
    f = 440.0        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively) 
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

def play_sawtooth():
    p = pyaudio.PyAudio()

    volume = 1.0     # range [0.0, 1.0]
    fs = 44100       # sampling rate, Hz, must be integer
    duration = 2.0   # in seconds, may be float
    f = 440.0        # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (np.sin(2*np.pi*np.arange(fs*duration)*f/fs)).astype(np.float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=fs,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()

def play_osc1():
    waveform_selected = waveform_selected1()
    if(waveform_selected == "sine"):
        play_sine1()



def play_osc2():
    pass

def plot_osc1():
    waveform_selected = waveform_selected1()
    freq = float(input_freq.get())
    amplitude = amp_osc1.get()
    if(waveform_selected == "sine"):
        plot_sine1(freq,amplitude)

    if(waveform_selected == "sawtooth"):
        plot_sawtooth()

    if(waveform_selected=="square"):
        plot_square()

def plot_osc2():
    pass

#Oscillator 1:
row = 0
waveforms = ["sine", "triangle", "pulse", "sawtooth", "square"]
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
amp_osc1 = tk.Scale(f1, from_=0, to=50, orient=tk.HORIZONTAL)
amp_osc1.grid(row=row,column=1)
row +=1
tk.Label(f1, text="phase").grid(row=row, column=0, sticky=tk.E)
phase_osc1 = tk.Scale(f1, from_=0, to=50, orient=tk.HORIZONTAL)
phase_osc1.grid(row=row,column=1)
row += 1
button_plotosc1 = tk.Button(f1,text="PLOT",command=plot_osc1)
button_plotosc1.grid(row=row,column=0)
button_plotosc1 = tk.Button(f1,text="PLAY",command=play_osc1)
button_plotosc1.grid(row=row,column=1)

#Oscillator 2:
row = 0
waveforms2 = ["sine", "triangle", "pulse", "sawtooth", "square"]
tk.Label(f2, text="waveform").grid(row=row, column=2, sticky=tk.E)
waveform2 = tk.OptionMenu(f2, waveform_select2, *waveforms2, command=waveform_selected2)
waveform2["width"] = 10
waveform2.grid(row=row, column=3)
row+=1
tk.Label(f2, text="frequency").grid(row=row, column=2, sticky=tk.E)
e1 = tk.Entry(f2)
e1.insert(10,str(default_sinefreq))
e1.grid(row=row,column=3)
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


f1.pack(side=tk.LEFT)
f2.pack(side=tk.RIGHT)
root.mainloop()


