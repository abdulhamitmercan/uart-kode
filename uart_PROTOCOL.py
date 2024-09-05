from UARTASYNC1 import UARTFrame, send_message, receive_message,recieveframe,sendframe,RxTxFonk 
import asyncio
from dataclasses import dataclass


#Komut ve mesaj türleri
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
CHARGE_FINISHED = 7
CLEAR_CHARGE = 8
END_TRANSACTION__SEND =9
CHARGING_STATUS = 10 
CONNECTOR_STATUS =11


class UartProtokol:
    def handleSET_DATA_RES(self):
        print("set data response")
        
        if recieveframe.get_msg_type() == MODE:
            pass
        elif recieveframe.get_msg_type() == RUN_CTRL:
            print("runcntrl")
        elif recieveframe.get_msg_type() == CLEAR_CHARGE:
            print("clear charge")
        elif recieveframe.get_msg_type() == END_TRANSACTION__SEND:
            print("end transaction send")
###---------------------------------------------------------------------------###
    def handleREAD_DATA_RES(self):
        print("read data response")
        
        if recieveframe.get_msg_type() == MODE:
            pass
        elif recieveframe.get_msg_type() == RUN_CTRL:
            print("charging start stop")      
        elif recieveframe.get_msg_type() == ETOTAL_CHARGING_COMPLETE:
            print("read energy")       
        elif recieveframe.get_msg_type() == CHARGING_TIME:
            print("read time")       
        elif recieveframe.get_msg_type() == PRMS:
            print("read rms value of power")      
        elif recieveframe.get_msg_type() == ERR_STATUS:
            print("type of error")
        elif recieveframe.get_msg_type() == CHARGE_FINISHED:
            print("charge finish")        
        elif recieveframe.get_msg_type() == CHARGING_STATUS:
            print("charge status") 
        elif recieveframe.get_msg_type() == CONNECTOR_STATUS:
            print("conn status")

###--------------------------------------------------------------------------###
async def handleUartFrame(self):
    recieveframe.cmd_type = READ_DATA_RESPONSE
    recieveframe.dataH = 0
    recieveframe.dataL = 1
    recieveframe.msg_type = PRMS
    recieveframe.header = 'b'
    recieveframe.eof = 'k'
    while True:
        if recieveframe.get_cmd_type() == SET_DATA_RESPONSE:
            self.handleSET_DATA_RES()
            
        elif recieveframe.get_cmd_type() == READ_DATA_RESPONSE:
            self.handleREAD_DATA_RES()
            
        await asyncio.sleep(0.1)


async def main():   
    myUart = UartProtokol()     
    task1 = asyncio.create_task(myUart.handleUartFrame())


asyncio.run(main())