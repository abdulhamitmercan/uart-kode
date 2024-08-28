import serial
import asyncio

# Seri portu açıyoruz ve baud rate olarak 9600 bps kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

async def send_message(message):
    while True:
        print(f"gonderilen mesaj: {message}")
        ser.write(message.encode())  # Mesajı byte olarak gönderiyoruz
        await asyncio.sleep(1)  # 1 saniye bekletiyoruz

async def recieve_message():
    while True:
        if ser.in_waiting:  # Veri bekleniyorsa
            received_data = ser.read()      
            await asyncio.sleep(0.03)
            data_left = ser.in_waiting
            received_data += ser.read(data_left)
            print(f"alinan veri: {received_data.decode(errors='ignore')}")  # Alınan veriyi stringe çeviriyoruz
        await asyncio.sleep(0.1)  # Döngüyü rahatlatmak için küçük bir bekleme

async def main():
    await asyncio.gather(
        send_message("abdulhamit"),  # Gönderilen mesaj
        recieve_message()            # Alınan mesaj
    )

asyncio.run(main())
