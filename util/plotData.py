import serial
import matplotlib.pyplot as plt
import time


x = list()
y = list()


with open('C:\\Users\\david\\PycharmProjects\\Arduino projects\\resources\\final_data_Sat_27_Jun_2020_19_11_48.csv', 'r') as read:
    for i, line in enumerate(read.readlines()):
        if i > 0:
            values = line.split(";")
            x.append(float(values[0]))
            y.append(float(values[1]))

plt.scatter(x, y)
plt.xlabel("time (s)")
plt.ylabel("temperature (C)")
plt.title("Newton's law of cooling")
plt.grid()
plt.show()