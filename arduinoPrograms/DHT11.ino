#include <dht.h>

dht DHT;

//definir pin que trae la informacion del sensor
#define DHT11_PIN 8

//alistar los componentes del arduino
void setup(){
  Serial.begin(115200); // abrir puerto para que python pueda extraer la informacion
  pinMode(6, OUTPUT); // alistar el pin 6 como output (se prenda o se apague)
  pinMode(3, OUTPUT); // alistar el pin 3 como output (se prenda o se apague)
}

// ejecutar lo que vamos a hacer con el sensor
void loop(){
  int chk = DHT.read11(DHT11_PIN); // traer la informacion del sensor
  float temp = DHT.temperature; // leer los datos de la temperatura
  float hum = DHT.humidity; // leer los datos de la humedad

  // si la temperatura es mayor a 25 encienda el led en el pin 6. Si no, apaguelo
  if(temp > 25){
    digitalWrite(6, HIGH);
  }else{
    digitalWrite(6, LOW);
  }

  // si la humedad es mayor a 60& encienda el led en el pin 3. Si no, apaguelo
  if(hum > 60){
    digitalWrite(3, HIGH);
  }else{
    digitalWrite(3, LOW);
  }

  Serial.print(temp); // enviar informacion de temperatura
  Serial.print(","); // dar formato para separar los valores de temperatura y humedad
  Serial.print(hum); // envio la informacion de la humedad
  Serial.print("\n"); // crear nueva linea despuues de armar la informacion
  delay(1000); // despues de realizar todo el proceso anteror, espere 1 segundo y vuelva a iniciar
}
