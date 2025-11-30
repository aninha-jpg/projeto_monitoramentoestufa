#Nome: Ana Luiza de Lima da Rocha.
#Curso: Análise e desenvolvimento de sistemas.

# Import das Bibliotecas
import network
import machine
import urequests
import dht
import time

#configs
NOMEWIFI = "LUCAS"
PASSWORD = "lima010609"
THINGSPEAKE_API_KEY = "OTUA4L2DFLJXGKMD"

#Conexão ao wifi.

station = network.WLAN(network.STA_IF)
station.active(True)
station.connect(NOMEWIFI, PASSWORD)

while not station.isconnected():
    print("Conectando ao Wifi...")
    time.sleep(2)
    
    print("Conectado com sucesso!")
    
#Sensor DHT11 e Relé.
    
sensor = dht.DHT11(machine.Pin(4))
rele = machine.Pin(2, machine.Pin.OUT)

while True:
    try:
        sensor.measure()
        temperatura = sensor.temperature()
        umidade = sensor.humidity()
        print ("Temperatura = {} Umidade = {}.".format(temperatura, umidade))
#Lógica relé
    
        if temperatura > 31 or umidade > 70:
            rele.value(1)
            print("Relé Ligado.")
        
        else:
            rele.value(0)
            print("Relé desligado.")
            
# Enviar dados para o ThingSpeak

        url = "https://api.thingspeak.com/update?api_key={}&field1={}&field2={}".format(
            THINGSPEAKE_API_KEY, temperatura, umidade
            )

        response = urequests.get(url)
        print("Resposta do ThingSpeak:", response.text)
        response.close()
        
    except Exception as e:
        print("Erro:", e)
            

    time.sleep(15)