from machine import Pin
import time
import network
import dht
import ujson
from umqtt.simple import MQTTClient
import random
from machine import Timer

print("Starting the IOT - Eka Arya Gading")

MQTT_CLIENT_ID = "ekaaryagading"
MQTT_BROKER    = "broker.emqx.io"
MQTT_USER      = ""
MQTT_PASSWORD  = ""
MQTT_TOPIC_DATA_SENSOR   = "Barudak_Depok_Baik_Hati_dan_Rajin_Menabung/ekaaryagading/data_sensor"
MQTT_TOPIC_AKTUASI_LED   = "Barudak_Depok_Baik_Hati_dan_Rajin_Menabung/ekaaryagading/aktuasi_led"



def connect_wifi():
    print("Menghubungkan Ke WiFi...", end="")
    sta_if = network.WLAN(network.STA_IF)
    sta_if.active(True)
    sta_if.connect('Wokwi-GUEST', '')
    while not sta_if.isconnected():
        print(".", end="")
        time.sleep(1)
    print(" Terhubung Ke WiFi!")


def callbackGet_message(topic, msg):
    try:
        message = msg.decode("UTF-8").strip()
    except AttributeError:
        print("Format pesan yang salah!. Harus Bytes!")
        return

    if message == "ON":
        print("Menghidupkan lampu")
        led.on()
    elif message == "OFF":
        print("Mematikan lampu")
        led.off()
    else:
        print(f"{message} Tidak Mempengaruhi Apa Apa Woi!")


led = Pin(18, Pin.OUT)
sensor = dht.DHT22(Pin(5))

def main():
    print("Memulai Sistem..")
    connect_wifi()

    print("koneksi ke MQTT server... ", end="")
    client = MQTTClient(MQTT_CLIENT_ID, MQTT_BROKER, user=MQTT_USER, password=MQTT_PASSWORD)
    client.set_callback(callbackGet_message)
    client.connect()
    client.subscribe(MQTT_TOPIC_AKTUASI_LED)
    print("Terhubung!")

    prev_weather = ""
    while True:
        print("Mengukur kondisi cuaca")
        sensor.measure()

        data = {
            "temp": sensor.temperature(),
            "humidity": sensor.humidity()
        }

        msg = ujson.dumps(data)

        if msg != prev_weather:
            client.publish(MQTT_TOPIC_DATA_SENSOR, msg)
            print(f"Data dikirim: {msg}")
            prev_weather = msg
        else:
            print("Tidak ada perubahan data ....")
        
        client.check_msg()
        time.sleep(4)


main()