from UARTASYNC1 import UARTFrame, recieveframe, sendframe, RxTxFonk
import asyncio

# Command and message types
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
END_TRANSACTION__SEND = 9
CHARGING_STATUS = 10 
CONNECTOR_STATUS = 11


class UartProtokol:
    def __init__(self, uartProtocol):
        self.recieve_message_err_status = None
        self.rxSuccess = 0
        self.uartProtocol = uartProtocol
        
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

    async def handleUartFrame(self):
        while True:
            if(self.uartProtocol.rxSuccess == 1):
                if recieveframe.get_cmd_type() == SET_DATA_RESPONSE:
                    self.handleSET_DATA_RES()
                elif recieveframe.get_cmd_type() == READ_DATA_RESPONSE:
                    self.handleREAD_DATA_RES()
                    
                self.uartProtocol.rxSuccess = 0
                
                

            await asyncio.sleep(0.1)


async def main():
    rxtx_fonk = RxTxFonk()
    myUart = UartProtokol(rxtx_fonk)    
    await asyncio.gather(rxtx_fonk.send_message(), rxtx_fonk.receive_message(), myUart.handleUartFrame())
    
asyncio.run(main())
