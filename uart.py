import serial
from time import sleep

# Seri portu açıyoruz ve baud rate olarak 9600 bps (bit per second) kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

while True:
    # Seri porttan 1 byte veri okuyoruz
    received_data = ser.read()
    #abdul
    
    # 30 milisaniye bekliyoruz. Bu, verinin gelmesini beklemek için kullanılır.
    # Özellikle seri porttan gelen verilerin tam olarak alınabilmesi için bu süre zarfında
    # veri akışını gözlemleyebiliriz. Bu, veri kaybını önlemek için önemlidir.
    sleep(0.03)

    # Seri portta hala okunacak veri olup olmadığını kontrol ediyoruz.
    data_left = ser.inWaiting()

    # Eğer veri varsa, kalan veriyi okuyoruz ve önceki okunan veriye ekliyoruz.
    # `ser.inWaiting()` işlevi, portta bekleyen byte sayısını döner.
    # `ser.read(data_left)` ile kalan byte'ları okuruz ve bu veriyi `received_data`'ya ekleriz.
    received_data += ser.read(data_left)

    # Alınan tüm veriyi ekrana yazdırıyoruz.
    print(received_data)

    # Alınan veriyi tekrar aynı seri port üzerinden gönderiyoruz.
    # Bu işlem, verinin aynı şekilde geri gönderilmesini sağlar.
    ser.write(received_data)
