import serial
import asyncio 

# Seri portu açıyoruz ve baud rate olarak 9600 bps (bit per second) kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

def format_message(message):
    # Mesajı 6 byte'a ayarla, gerekirse kısalt veya boşlukla doldur
    formatted_message = message[:6].ljust(6)  # Mesajı 6 byte uzunluğa getir
    # Başına 'b', sonuna 'k' ekle ve 8 byte olacak şekilde encode et
    return f"b{formatted_message}k".encode() 

async def send_message(message):
    while True:
        formatted_message = format_message(message)  # Mesajı formata uygun hale getir
        print(f"Gönderilen mesaj: {formatted_message.decode('utf-8')}")
        await asyncio.sleep(2)
        ser.write(formatted_message)  # Seri porta yaz

async def receive_message():
    while True:
        if ser.in_waiting: 
            received_data = ser.read()      
            await asyncio.sleep(0.03) 
            data_left = ser.in_waiting 
            received_data += ser.read(data_left) 
            print(f"Alınan veri: {received_data.decode(errors='ignore')}")
        await asyncio.sleep(0.1)

async def main():
    await asyncio.gather(send_message("asburaci"), receive_message())  # Mesajınızı buraya yazabilirsiniz

asyncio.run(main())
