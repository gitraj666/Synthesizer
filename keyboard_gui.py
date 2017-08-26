__author__ = 'PRITHVIRAJ'
root = tk.Tk()
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt



#Variables :
waveform_select = tk.StringVar()
waveform_select.set("sine")
default_sinefreq = 50
f = tk.Frame()


def plot_osc1():
    #f = int(input("ENTER no of samples: "))
    Fs = 8000
    f = 5
    sample = 8000
    x = np.arange(sample)
    y = np.sin(2 * np.pi * f * x / Fs)
    plt.plot(x, y)
    plt.xlabel('voltage(V)')
    plt.ylabel('sample(n)')
    plt.show()

def SquareWave(n=5,xmin=0,xmax=10,ymin=-2,Nx=1000,ymax=2,offset=0.5):
    x=np.sort(np.concatenate([np.arange(xmin, xmax)-1E-6,np.arange(xmin, xmax)+1E-6]))
    y=np.array(x+n+offset,dtype=int)%2
    plt.plot(x, y)
    plt.axis([xmin, xmax, ymin, ymax])
    plt.grid()
    plt.show()

def waveform_selected():
    pass

def play_osc1():
    pass


row = 0
waveforms = ["sine", "triangle", "pulse", "sawtooth", "square"]
tk.Label(f, text="waveform").grid(row=row, column=0, sticky=tk.E)
waveform = tk.OptionMenu(f, waveform_select, *waveforms, command=waveform_selected)
waveform["width"] = 10
waveform.grid(row=row, column=1)
row+=1
tk.Label(f, text="frequency").grid(row=row, column=0, sticky=tk.E)
e1 = tk.Entry(f)
e1.insert(10,str(default_sinefreq))
e1.grid(row=row,column=1)
row +=1
tk.Label(f, text="amp").grid(row=row, column=0, sticky=tk.E)
amp_osc1 = tk.Scale(f, from_=0, to=50, orient=tk.HORIZONTAL)
amp_osc1.grid(row=row,column=1)
row +=1
tk.Label(f, text="phase").grid(row=row, column=0, sticky=tk.E)
phase_osc1 = tk.Scale(f, from_=0, to=50, orient=tk.HORIZONTAL)
phase_osc1.grid(row=row,column=1)
row += 1
button_plotosc1 = tk.Button(f,text="PLOT",command=plot_osc1)
button_plotosc1.grid(row=row,column=0)
button_plotosc1 = tk.Button(f,text="PLAY",command=play_osc1)
button_plotosc1.grid(row=row,column=1)


f.pack(side=tk.TOP)
root.mainloop()


