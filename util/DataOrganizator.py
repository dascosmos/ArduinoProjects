

with open ('C:\\Users\\david\\Documents\\Arduino\\temp_data_Sat_27_Jun_2020_19_11_48.csv', 'r') as read_file:
    with open ("/resources/final_data_Sat_27_Jun_2020_19_11_48.csv", 'w') as write_file:
        for x, line in enumerate(read_file.readlines()):
            if x == 0:
                write_file.write(line.rstrip())
            else:
                if line is not '\n':
                    split_line = line.split(";")
                    time = round(float(split_line[0]), 2)
                    temp = split_line[1]
                    write_file.write(str(time)+";"+str(temp))


