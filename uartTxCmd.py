import asyncio
from uart_PROTOCOL import UartProtokol,messageTypeData,cmdTypeData
from UARTASYNC1 import RxTxFonk,sendframe

class SetDataValue:
    # Sabit değerler
    STOP_CHARGE = 2
    START_CHARGE = 1

    NOT_END_TRANSACTION = 0
    END_TRANSACTION = 1
    START_BUZZER = 8
   

    END_TRANSACTION__SEND = 9

    def __init__(self):
       
        self._max_charge_val = None
        self._baz_val = None

    # max_charge_val 
    def set_max_charge_val(self, value):
        self._max_charge_val = value

    def get_max_charge_val(self):
        return self._max_charge_val

    # baz_val   
    def set_baz_val(self, value):
        self._baz_val = value

    def get_baz_val(self):
        return self._baz_val
    
    
setdata = SetDataValue() 

def sendStartCharging():
    
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(messageTypeData.RUN_CTRL)
    sendframe.set_dataL(setdata.START_CHARGE)
    
def sendMaxPower():
    
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(messageTypeData.MAX_POWER)
    sendframe.set_dataL(setdata.get_max_charge_val())
         
def sendStopCharging():
    
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(messageTypeData.RUN_CTRL)
    sendframe.set_dataL(setdata.STOP_CHARGE)

def sendReadEnergyIns():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.ETOTAL)
    
def sendReadDeviceId():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.DEVICE_ID)
    
def sendReadEnergyComplete():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.ETOTAL_CHARGING_COMPLETE)
      
def sendReadChargingTime():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.CHARGING_TIME)
    
def sendReadChargingTimeHour():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.CHARGING_TIME_HOURS)  
     
def sendReadPrms():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.PRMS)      

def sendReadErr():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.ERR_STATUS)
    
def sendReadChargeFinished():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.CHARGE_FINISHED)

def sendClearChargeSession():
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(messageTypeData.RUN_CTRL)  ### 
    sendframe.set_dataL(setdata.START_BUZZER)
    
def sendEndTransaction():
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(setdata.END_TRANSACTION__SEND)  
    sendframe.set_dataL(setdata.END_TRANSACTION)  

def sendNotEndTransactio():
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(setdata.END_TRANSACTION__SEND)  
    sendframe.set_dataL(setdata.NOT_END_TRANSACTION)
    
def sendReadConnectorStatus():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.CONNECTOR_STATUS)   
       
def  sendReadChargingStatus():
    sendframe.set_cmd_type(cmdTypeData.READ_DATA)
    sendframe.set_msg_type(messageTypeData.CHARGING_STATUS)  

def  sendSetBuzzer():  
    sendframe.set_cmd_type(cmdTypeData.SET_DATA)
    sendframe.set_msg_type(messageTypeData.CLEAR_CHARGE)  
    sendframe.set_dataL(setdata.get_baz_val())  
 
 
 
                   
async def main():
    rxtx_fonk = RxTxFonk()
    myUart = UartProtokol(rxtx_fonk)
    
    await asyncio.gather(
        rxtx_fonk.send_message(),
        rxtx_fonk.receive_message(),
        myUart.reciveHandleUartFrame()
    )

asyncio.run(main())






