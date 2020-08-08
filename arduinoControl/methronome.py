import pyfirmata
import time



board = pyfirmata.Arduino('COM3')
 
led1 = board.digital[12]

bpm = 120                 #bpm reuired
bps = bpm/60              #bpm converted to bps
freq = 1/bps              #real frequency of the bpm
led_freq = freq/2         #frequency for the led to mach real freq when led is on

print("BPM "+str(bpm))
print("frequency "+str(freq))
print("LED frequency "+str(led_freq))

print("=========START METRONOME=========")
cont = 0
t1 = time.perf_counter()
while True:
    led1.write(1)
    time.sleep(led_freq)
    led1.write(0)
    time.sleep(led_freq)
    cont += 1
    t2 = time.perf_counter()
    
    if cont % 60 == 0:
        print("total Bits "+str(cont))
        print("elapsed time "+str(t2 - t1))
