import pyfirmata
import time

board = pyfirmata.Arduino('COM4')
led1 = board.digital[12]

while True:
    led1.write(1)
    time.sleep(0.5)
    led1.write(0)
    time.sleep(0.5)
    led1.write(1)
    time.sleep(0.2)
    led1.write(0)
    time.sleep(0.2)
    led1.write(1)
    time.sleep(0.2)
    led1.write(0)
    time.sleep(0.2)
    led1.write(1)
    time.sleep(0.5)
    led1.write(0)
    time.sleep(0.5)
