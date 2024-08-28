import serial
import asyncio 


# Seri portu açıyoruz ve baud rate olarak 9600 bps (bit per second) kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

async def send_message(message):
    while True:
        print("gonderilen mesaj:"+{message})
        await asyncio.sleep(2)
        ser.write(message.encode()) 
        
async def recieve_message():
    while True:
        if ser.in_waiting: 
            
            received_data = ser.read()      
            await asyncio.sleep(0.03) 
            data_left = ser.inWaiting() 
            received_data += ser.read(data_left) 
            print(f"alinan veri :{received_data.decode(errors='ignore')}" ) 
        await asyncio.sleep(0.1)
        
async def main():
    results = await asyncio.gather(send_message("abdulhamit"),recieve_message())


 

asyncio.run(main())