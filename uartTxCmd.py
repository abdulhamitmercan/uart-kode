import asyncio
from uart_PROTOCOL import UartProtokol, messageTypeData, cmdTypeData
from UARTASYNC1 import RxTxFonk, sendframe

class SetDataValue:
    # Sabit değerler 
    STOP_CHARGE = 2
    START_CHARGE = 1

   
    END_TRANSACTION = 1
    START_BUZZER = 8
    END_TRANSACTION_SEND = 9

    def __init__(self):
        self._max_charge_val = None
        self._baz_val = None
        self._transection_val = None
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
    
    def set_transection_val(self, value):
        self._transection_val = value

    def get_transection_val(self):
        return self._transection_val   

class UartHandler:
    def __init__(self, set_data):
        self.setdata = set_data



  
    def sendStartCharging(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.RUN_CTRL)
        sendframe.set_dataL(self.setdata.START_CHARGE)

    def sendMaxPower(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.MAX_POWER)
        sendframe.set_dataL(self.setdata.get_max_charge_val())

    def sendStopCharging(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.RUN_CTRL)
        sendframe.set_dataL(self.setdata.STOP_CHARGE)

    def sendReadEnergyIns(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.ETOTAL)

    def sendReadDeviceId(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.DEVICE_ID)

    def sendReadEnergyComplete(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.ETOTAL_CHARGING_COMPLETE)

    def sendReadChargingTime(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.CHARGING_TIME)

    def sendReadChargingTimeHour(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.CHARGING_TIME_HOURS)

    def sendReadPrms(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.PRMS)

    def sendReadErr(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.ERR_STATUS)

    def sendReadChargeFinished(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.CHARGE_FINISHED)

    def sendClearChargeSession(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.RUN_CTRL)
        sendframe.set_dataL(self.setdata.START_BUZZER)

    def sendEndTransaction(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(self.setdata.END_TRANSACTION_SEND)
        sendframe.set_dataL(self.setdata.END_TRANSACTION)

    def sendNotEndTransaction(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(self.setdata.END_TRANSACTION_SEND)
        sendframe.set_dataL(self.setdata.NOT_END_TRANSACTION)

    def sendReadConnectorStatus(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.CONNECTOR_STATUS)

    def sendReadChargingStatus(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)    
        sendframe.set_msg_type(messageTypeData.CHARGING_STATUS)    
    
    def sendSetBuzzer(self):    
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)    
        sendframe.set_msg_type(messageTypeData.CLEAR_CHARGE)    
        sendframe.set_dataL(self.setdata.get_baz_val())    
            
    async def handleSET_DATA(self):    
        
        self.sendMaxPower()
        await asyncio.sleep(0.3)
               
        self.sendSetBuzzer()
        await asyncio.sleep(0.3)
        
        self.sendClearChargeSession()
        await asyncio.sleep(0.3)
        
        if(messageTypeData.RUN_CTRL==1):
            
            self.sendStartCharging()    
            await asyncio.sleep(0.3)    
        else:
            self.sendStopCharging()
            await asyncio.sleep(0.3)
        
        if(self.setdata.get_transection_val() == self.setdata.END_TRANSACTION):
            self.sendEndTransaction()
            await asyncio.sleep(0.3)
        else:
            self.sendNotEndTransaction()
            await asyncio.sleep(0.3)
            


        

    async def handleREAD_DATA(self):
        self.sendReadEnergyIns()
        await asyncio.sleep(0.3)
        self.sendReadDeviceId()
        await asyncio.sleep(0.3)
        self.sendReadEnergyComplete()
        await asyncio.sleep(0.3)
        self.sendReadChargingTime()
        await asyncio.sleep(0.3)
        self.sendReadChargingTimeHour()
        await asyncio.sleep(0.3)
        self.sendReadPrms()
        await asyncio.sleep(0.3)
        self.sendReadErr()
        await asyncio.sleep(0.3)
        self.sendReadChargeFinished()
        await asyncio.sleep(0.3)
        self.sendReadConnectorStatus()
        await asyncio.sleep(0.3)
        self.sendReadChargingStatus()

    async def sendHandleUartFrame(self):
        while True:
            await self.handleREAD_DATA()
            await self.handleSET_DATA()

setdata = SetDataValue()
uart_handler = UartHandler(setdata)



 
                   
async def main():
    rxtx_fonk = RxTxFonk()
    myUart = UartProtokol(rxtx_fonk)
    
    await asyncio.gather(
        rxtx_fonk.send_message(),
        rxtx_fonk.receive_message(),
        myUart.reciveHandleUartFrame(),
        uart_handler.sendHandleUartFrame()
    )

asyncio.run(main())






