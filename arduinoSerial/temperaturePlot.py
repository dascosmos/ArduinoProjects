import serial
import matplotlib.pyplot as plt
import time

plt.ion()
fig = plt.figure()

i = 0
x = list()
y = list()
show = True

ser = serial.Serial('COM3', 9600)

ser.close()
ser.open()


def on_close(event):
    global show
    show = False


localtime = time.strftime("%a_%d_%b_%Y_%H_%M_%S", time.localtime())
print(localtime)
begin_time = time.time()
print('start time = ' + str(x))

with open('C:\\Users\\david\\PycharmProjects\\Arduino projects\\resources\\temp_data_' + localtime + '.csv', 'w') as file_t:
    file_t.write("time;temperature\n")
    while show:
        data = ser.readline()
        clean_data = data.decode().rstrip()
        curr_time = time.time() - begin_time
        print(str(curr_time) + " " + clean_data)

        file_t.write(str(curr_time) + ";" + clean_data+"\n")

        x.append(curr_time)
        y.append(data.decode())

        plt.scatter(curr_time, float(clean_data))

        plt.show()
        plt.pause(0.0001)
        cid = fig.canvas.mpl_connect('close_event', on_close)

        if curr_time >= 3600:
            plt.close()
            show = False

ser.close()
print('program finished')
