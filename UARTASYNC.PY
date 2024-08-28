import serial
import asyncio 

# Seri portu açıyoruz ve baud rate olarak 9600 bps (bit per second) kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

def format_message(message):
    # Mesajı 6 byte'a ayarla, gerekirse kısalt veya boşlukla doldur
    formatted_message = message[:6].ljust(6)
    # Başına 'b', sonuna 'k' ekle
    formatted_message = f"b{formatted_message}k"  # Tek bir 'b' karakteri ekliyoruz
    return formatted_message.encode()  # 8 byte'lık mesajı encode et

async def send_message(message):
    while True:
        formatted_message = format_message(message)
        print(f"gonderilen mesaj: {formatted_message}")
        await asyncio.sleep(2)
        ser.write(formatted_message)

async def receive_message():
    while True:
        if ser.in_waiting: 
            received_data = ser.read()      
            await asyncio.sleep(0.03) 
            data_left = ser.in_waiting 
            received_data += ser.read(data_left) 
            print(f"alinan veri: {received_data.decode(errors='ignore')}")
        await asyncio.sleep(0.1)

async def main():
    await asyncio.gather(send_message("buraci"), receive_message())

asyncio.run(main())
