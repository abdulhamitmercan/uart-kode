'''
UART communication on Raspberry Pi using Pyhton
http://www.electronicwings.com
'''
import serial
from time import sleep

ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)

while True:
    if ser.in_waiting > 0:
        received_data = ser.read(ser.in_waiting)  # Veriyi oku
        print(received_data.decode('utf-8', errors='ignore'))  # Veriyi yazdır
        ser.write(received_data)  # Veriyi tekrar gönder
    sleep(0.1)  # Döngü hızını ayarla
