import serial
import time
import matplotlib.pyplot as plt
import numpy as np
from drawnow import *


# Crear listas para guardar los valores de la humedad y temperatura
tempC = []
humidity = []

#Comunicarse con arduino
arduino = serial.Serial('COM4', 115200)

# definir la grafica para que sea dinamica y se actualice
plt.ion()

# funcion que va a crear la grafica y la va a mostrar
def makeFig():
    plt.ylim(20, 50) # limitar el tamaño del eje y
    plt.title('Humidity and temperature') # poner titulo al grafico
    plt.grid(True) # poner grilla al grafico
    plt.ylabel('Temperature') #nombrar el eje y
    plt.plot(tempC, 'b^-', label='Degree C') # graficar temperatura
    plt.legend(loc='upper right') # definir la ubicacion de la leyenda
    plt2 = plt.twinx() # crear un segundo grafico
    plt.ylim(30, 100) # definir el tamaño del eje y del segundo grafico
    plt2.plot(humidity, 'g*-', label='Humidity') # graficar humedad
    plt2.set_ylabel('Humidity') # nombrar el eje y de la humedad
    plt2.ticklabel_format(useOffset=False) # evitar que el grafico se muestre desde el primer valor
    plt2.legend(loc = 'upper left') # definir la posicion de la leyenda


count = 0

#Loop que va a mostrar la grafica infinitamente
while True:

    arduinoString = arduino.readline() # leer los datos del arduino
    dataArray = arduinoString.decode().split(',') # separar los datos de humedad y temperatura
    temp = float(dataArray[0]) # obtener solo los datos de temperatura
    hum = float(dataArray[1]) # obtener solo los datos de humedad

    # imprimir los datos en consola
    print(temp, hum)

    #guardar los datos en las listas creadas arriba
    tempC.append(temp)
    humidity.append(hum)

    #dibujar el grafico y mostrarlo en pantalla
    drawnow(makeFig)

    #definir la tasa en la que la grafica va a mostrar los datos
    plt.pause(.00001)
    count = count + 1

    # condicion para mostrar solo los primeros 20 datos de la lista
    if(count > 20):
        tempC.pop(0)
        humidity.pop(0)
        

