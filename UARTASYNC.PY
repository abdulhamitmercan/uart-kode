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

frame = UARTFrame()

# Seri portu açıyoruz ve baud rate olarak 9600 bps (bit per second) kullanıyoruz
ser = serial.Serial("/dev/ttyS0", 9600)

def format_message():
    # Bayt listesini set ve get metodlarıyla oluşturuyoruz
    byte_list = [
        frame.header,
        frame.get_cmd_type(),
        frame.get_msg_type(),
        frame.rsv1,
        frame.rsv0,
        frame.get_dataH(),
        frame.get_dataL(),
        frame.eof,
    ]

    return bytearray(byte_list)  # bytearray ile döndür

async def send_message():
    while True:
        formatted_message = format_message()  # Mesajı formata uygun hale getir
        print(f"Alınan veri: {formatted_message.decode(errors='ignore')}")
        await asyncio.sleep(2)
        ser.write(formatted_message)  # Seri porta yaz

async def receive_message():
    while True:
        if ser.in_waiting: 
            received_data = ser.read()      
            await asyncio.sleep(0.03) 
            data_left = ser.in_waiting 
            received_data += ser.read(data_left) 
            print(f"Alınan veri: {received_data.decode(2)}")
        await asyncio.sleep(0.1)

# Frame değerlerini set ediyoruz
frame.set_cmd_type(SET_DATA)
frame.set_msg_type(RUN_CTRL)
frame.set_dataH(0x04)
frame.set_dataL(0x05)

async def main():
    await asyncio.gather(send_message(), receive_message())

asyncio.run(main())