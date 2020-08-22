import pyfirmata
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

MY_ADDRESS = 'tite.kubo033@gmail.com'
PASSWORD = 'Natsu.123'

# funcion para enviar el mensaje
def send_message():
    s = smtplib.SMTP(host='smtp.gmail.com', port=587) #conexion a servidor smtp
    s.starttls() # iniciar protocolo de seguridad
    s.login(MY_ADDRESS, PASSWORD) # iniciac sesion en la cuenta


    msg = MIMEMultipart() # inicializar mensaje

    msg['From'] = MY_ADDRESS # quien es el remitente del mensaje
    msg['To'] = 'david.salazar033@outlook.com' # a quien va dirigido el mensaje
    msg['Subject'] = 'Alerta de movimiento' # Asunto del mensaje

    msg.attach(MIMEText("Este es un aviso que alguien se ha movido dentro del rango del sensor", 'plain')) # Cuerpo del mensaje

    s.send_message(msg) # enviar mensaje
    del msg # eliminar mensaje


board = pyfirmata.Arduino('COM3') # inicializar la board

# inicializar cada uno de los componentes de la board
it = pyfirmata.util.Iterator(board)
it.start()

pir = board.get_pin('d:7:i') # inicializar pin digital 7 como INPUT
led = board.get_pin('d:9:o') # inicializar pin digital 9 como OUTPUT

control_mensaje = 0 # variable que controlara que los mensajes no se envien cada vez que hay un ciclo

while True:
    data = pir.read() # leer informacion del sensor True o False
    print(data)
    if data: # preguntar si el sensor se activa
        led.write(1)  # prender el led
        if control_mensaje == 0: # si es la primera vez que el sensor capta algo, entonces enviar el mensaje. si no, no haga nada
            send_message() # enviar el mensaje
            control_mensaje += 1 # aumentar el contador en 1
    else: # si no hay movimiento
        led.write(0) # apagar el led
        control_mensaje = 0 # reiniciar el contador para cuando el sensor vuelva a activarse, pueda enviar una nueva alerta
