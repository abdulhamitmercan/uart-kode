from UARTASYNC1 import UARTFrame, recieveframe, RxTxFonk
from UARTmem import SetDataResponse,ReadDataResponse
import asyncio

# Command and message types

class CmdTypeData:
    SET_DATA = 0
    SET_DATA_RESPONSE = 1
    READ_DATA = 2
    READ_DATA_RESPONSE = 3


class MessageTypeData:
    MODE = 0
    RUN_CTRL = 1
    ETOTAL = 2
    ETOTAL_CHARGING_COMPLETE = 3
    CHARGING_TIME = 4
    PRMS = 5
    ERR_STATUS = 6
    CHARGE_FINISHED = 7
    CLEAR_CHARGE = 8
    END_TRANSACTION_SEND = 9
    CHARGING_STATUS = 10
    CONNECTOR_STATUS = 11
    CHARGING_TIME_HOURS = 12
    DEVICE_ID = 13
    MAX_POWER = 14
    
messageTypeData = MessageTypeData()
cmdTypeData = CmdTypeData()

#MAX_POWER =14#SET

class UartProtokol:
    def __init__(self, UART_HAL):
        self.recieve_message_err_status = None
        self.UART_HAL = UART_HAL
        
    def handleSET_DATA_RES(self):
        print("set data response")
        if recieveframe.get_msg_type() == messageTypeData.MODE:
            pass
        elif recieveframe.get_msg_type() == messageTypeData.RUN_CTRL:
            SetDataResponse.setRunControl(recieveframe.get_dataL())
            print("runcntrl")
            
        elif recieveframe.get_msg_type() == messageTypeData.CLEAR_CHARGE:
            SetDataResponse.setClearChargeSession(recieveframe.get_dataL())
            print("clear charge")
            
        elif recieveframe.get_msg_type() == messageTypeData.END_TRANSACTION_SEND:
            SetDataResponse.setEndTransaction(recieveframe.get_dataL())
            print("end transaction send")

    def handleREAD_DATA_RES(self):
        print("read data response")
        if recieveframe.get_msg_type() == messageTypeData.MODE:
            pass
        elif recieveframe.get_msg_type() == messageTypeData.RUN_CTRL:
            ReadDataResponse.setChargingStartStop(recieveframe.get_dataL())
            print("charging start stop")
            
        elif recieveframe.get_msg_type() == messageTypeData.ETOTAL_CHARGING_COMPLETE:
            ReadDataResponse.setEnergyTotalComplate(recieveframe.get_dataL())
            print("read energy") 
            
        elif recieveframe.get_msg_type() == messageTypeData.CHARGING_TIME:
            ReadDataResponse.setTimeSeconds(recieveframe.get_dataL())
            ReadDataResponse.setTimeMinutes(recieveframe.get_dataH())
            print("read time")
            
        elif recieveframe.get_msg_type() == messageTypeData.CHARGING_TIME_HOURS :
            ReadDataResponse.setTimeHours(recieveframe.get_dataL())
            print("read device time hours")  
            
        elif recieveframe.get_msg_type() == messageTypeData.PRMS:
            ReadDataResponse.setRmsPowerValue(recieveframe.get_dataL())
            print("read rms value of power")
            
        elif recieveframe.get_msg_type() == messageTypeData.ERR_STATUS:
            ReadDataResponse.setErrorType(recieveframe.get_dataL())
            print("type of error")
            
        elif recieveframe.get_msg_type() == messageTypeData.CHARGE_FINISHED:
            ReadDataResponse.setChargeFinished(recieveframe.get_dataL())
            print("charge finish")
            
        elif recieveframe.get_msg_type() == messageTypeData.CHARGING_STATUS:
            print("charge status")
            ReadDataResponse.setChargingStatus(recieveframe.get_dataL())
            
            
        elif recieveframe.get_msg_type() == messageTypeData.CONNECTOR_STATUS:
            ReadDataResponse.setConnectorStatus(recieveframe.get_dataL())
            print("conn status")
            
        elif recieveframe.get_msg_type() == messageTypeData.DEVICE_ID :
            ReadDataResponse.setDeviceId(recieveframe.get_dataL)
            print("read device id")
 

    async def reciveHandleUartFrame(self):
        while True:
            if(self.UART_HAL.rxSuccess == 1):
                if recieveframe.get_cmd_type() == cmdTypeData.SET_DATA_RESPONSE:
                    self.handleSET_DATA_RES()
                elif recieveframe.get_cmd_type() == cmdTypeData.READ_DATA_RESPONSE:
                    self.handleREAD_DATA_RES()
                    
                self.UART_HAL.rxSuccess = 0
                
                

            await asyncio.sleep(0.1)
