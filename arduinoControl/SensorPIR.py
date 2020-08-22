import pyfirmata
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'tite.kubo033@gmail.com'
PASSWORD = 'Natsu.123'

def send_message():
    s = smtplib.SMTP(host='smtp.gmail.com', port=587)
    s.starttls()
    s.login(MY_ADDRESS, PASSWORD)


    msg = MIMEMultipart()

    msg['From'] = MY_ADDRESS
    msg['To'] = 'david.salazar033@outlook.com'
    msg['Subject'] = 'Alerta de movimiento'

    msg.attach(MIMEText("Este es un aviso que alguien se ha movido dentro del rango del sensor", 'plain'))

    s.send_message(msg)
    del msg


board = pyfirmata.Arduino('COM3')

it = pyfirmata.util.Iterator(board)
it.start()
pir = board.get_pin('d:7:i')
led = board.get_pin('d:9:o')

control_mensaje = 0

while True:
    data = pir.read()
    print(data)
    if data == 1:
        led.write(1)
        if control_mensaje == 0:
            send_message()
            control_mensaje += 1
    else:
        led.write(0)
        control_mensaje = 0
