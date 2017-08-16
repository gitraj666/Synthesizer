__author__ = 'PRITHVIRAJ'

from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
root = Tk()


def plot():
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


button1 = Button(root, text="SINE", command=plot)
button2 = Button(root, text="SAWTOOTH", command=SquareWave)
button1.pack()
button2.pack()


root.mainloop()


