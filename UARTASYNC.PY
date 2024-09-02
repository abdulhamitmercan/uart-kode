import serial
import asyncio
from dataclasses import dataclass

# Komut ve mesaj türleri
SET_DATA = 0
SET_DATA_RESPONSE = 1
READ_DATA = 2
READ_DATA_RESPONSE = 3

MODE = 0
RUN_CTRL = 1
ETOTAL = 2
ETOTAL_CHARGING_COMPLETE = 3
CHARGING_TIME = 4
PRMS = 5
ERR_STATUS = 6

@dataclass
class UARTFrame:
    header: int = 0x62  # Sabit değer
    cmd_type: int = 0x00
    msg_type: int = 0x00
    dataH: int = 0x00
    dataL: int = 0x00
    eof: int = 0x6B  # Sabit değer

    def __post_init__(self):
        # Her değeri 1 byte (0xFF) sınırına kısıtla
        self.cmd_type &= 0xFF
        self.msg_type &= 0xFF
        self.dataH &= 0xFF
        self.dataL &= 0xFF

    @property
    def rsv1(self):
        return 0x00  # Sabit değer

    @property
    def rsv0(self):
        return 0x00  # Sabit değer

    def get_cmd_type(self):
        return self.cmd_type

    def get_msg_type(self):
        return self.msg_type

    def get_dataH(self):
        return self.dataH

    def get_dataL(self):
        return self.dataL

    def set_cmd_type(self, value):
        self.cmd_type = value & 0xFF

    def set_msg_type(self, value):
        self.msg_type = value & 0xFF

    def set_dataH(self, value):
        self.dataH = value & 0xFF

    def set_dataL(self, value):
        self.dataL = value & 0xFF

sendframe = UARTFrame()
recieveframe = UARTFrame()
# Seri portu açıyoruz ve baud rate olarak 9600 bps (bit per second) kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

def uartformat_to_rawdata_send_message(): 
    # Bayt listesini set ve get metodlarıyla oluşturuyoruz
    byte_list = [
        sendframe.header,
        sendframe.get_cmd_type(),
        sendframe.get_msg_type(),
        sendframe.rsv1,
        sendframe.rsv0,
        sendframe.get_dataH(),
        sendframe.get_dataL(),
        sendframe.eof,
    ]

    return bytearray(byte_list)  # bytearray ile döndür

def rawdata_to_uartformat_recieve_message(recieved_message):
    if len(recieved_message) != 8:
        print("Geçersiz mesaj uzunluğu:", len(recieved_message))
        return None

    byte_list = [0] * 8
    for index, byte in enumerate(recieved_message):
        byte_list[index] = byte

    if byte_list[0] == 0x62 and byte_list[7] == 0x6B:
        recieveframe.set_cmd_type(byte_list[1])
        recieveframe.set_msg_type(byte_list[2])
        recieveframe.set_dataH(byte_list[5])
        recieveframe.set_dataL(byte_list[6])
        byte_list2 = [0] * 8
        for index, byte in enumerate(recieved_message):
            byte_list2[index] = byte
        return byte_list2
    else:
        print("Hatalı mesaj alındı")
        return byte_list

async def send_message():
    while True:
        formatted_message = uartformat_to_rawdata_send_message()  # Mesajı formata uygun hale getir
        print(f"gönderilen veri: {formatted_message}")
        
        """print("gönderilen veri bayt bayt:")
        for index, byte in enumerate(formatted_message):
                print(f"Bayt {index}: {byte:02X}")  # Her baytı hexadecimal olarak yazdır"""
                
        await asyncio.sleep(2)
        ser.write(formatted_message)  # Seri porta yaz

async def receive_message():
    while True:
        if ser.in_waiting >= 8:  # En az 8 bayt bekleyin
            received_data = ser.read()  
            await asyncio.sleep(0.03)
            data_left = ser.in_waiting
            received_data += ser.read(data_left)
            solved_message = rawdata_to_uartformat_recieve_message(received_data)
            
            if solved_message:
                print("alınan veri:")
                for index, byte in enumerate(solved_message):
                    print(f"Bayt {index}: {byte:02X}")  # Her baytı hexadecimal olarak yazdır
            else:
                print("Geçersiz veri alındı.")
            print(recieveframe.get_msg_type())
        await asyncio.sleep(0.1)




# Frame değerlerini set ediyoruz
sendframe.set_cmd_type(SET_DATA)
sendframe.set_msg_type(RUN_CTRL)
sendframe.set_dataH(0x04)
sendframe.set_dataL(0x05)

async def main():
    await asyncio.gather(send_message(), receive_message())

asyncio.run(main())