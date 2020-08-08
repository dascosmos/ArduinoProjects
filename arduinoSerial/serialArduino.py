import serial

serial = serial.Serial('COM3', baudrate=9600, timeout=1)

while 1:
    data = serial.readline().decode('ascii')
    print(data)
