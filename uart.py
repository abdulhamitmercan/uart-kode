import serial
from time import sleep
"""
ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)  # timeout eklemek veri okuma süresini belirler

while True:
    if ser.in_waiting > 0:  # Seri portta veri varsa
        received_data = ser.read(ser.in_waiting)  # Tüm veriyi oku
        print(received_data.decode('utf-8', errors='ignore'))  # Veriyi çöz ve yazdır
        ser.write(received_data)  # Veriyi tekrar gönder
    sleep(0.1)  # Döngü hızını ayarla
"""


ser = serial.Serial("/dev/ttyS0", 9600, timeout=1)  # timeout eklemek veri okuma süresini belirler

while True:
    received_data = ser.read()
    if ser.in_waiting > 0:  # Seri portta veri varsa
        received_data = ser.read()  # Tüm veriyi oku
        print(received_data.decode('utf-8', errors='ignore'))  # Veriyi çöz ve yazdır
    sleep(0.001)  # Döngü hızını ayarla