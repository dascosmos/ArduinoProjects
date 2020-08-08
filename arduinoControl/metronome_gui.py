import pyfirmata
import time
import tkinter as tk
import threading


board = ''
led1 = ''
running = True

def initialize():
    global board
    board = pyfirmata.Arduino('COM3')
    global led1
    led1 = board.digital[12]

def operate():
    bpm = 120
    bps = 1/((bpm/60)*2)

    while running:
        led1.write(1)
        time.sleep(bps)
        led1.write(0)
        time.sleep(bps)




def startCallBack(flag):
    global running
    x = threading.Thread(target=operate)
    if flag:
        print('begin operation')

        running = True
        x.start()
    else:
        running = False



top = tk.Tk()
top.title("Metronome")
top.grid()
top.geometry('500x500')

initialize()
start = tk.Button(top, text="Start", command=startCallBack(True))
stop = tk.Button(top, text="Stop", command=startCallBack(False))

start.grid()
stop.grid()

top.mainloop()
