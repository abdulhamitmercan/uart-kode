import asyncio
from uart_PROTOCOL import UartProtokol, messageTypeData, cmdTypeData
from UARTASYNC1 import RxTxFonk, sendframe
from UARTmem import setDataval

class SetDataValue:
    # Sabit değerler 
    STOP_CHARGE = 2
    START_CHARGE = 1

   
    END_TRANSACTION = 1
    NOT_END_TRANSACTION = 0
    START_BUZZER = 8
    END_TRANSACTION_SEND = 9



class UartHandler:


  
    def sendStartCharging(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.RUN_CTRL)
        sendframe.set_dataL(SetDataValue.START_CHARGE)

    def sendMaxPower(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.MAX_POWER)
        sendframe.set_dataL(setDataval.get_max_charge_val())

    def sendStopCharging(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(messageTypeData.RUN_CTRL)
        sendframe.set_dataL(SetDataValue.STOP_CHARGE)

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
        sendframe.set_dataL(SetDataValue.START_BUZZER)

    def sendEndTransaction(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(SetDataValue.END_TRANSACTION_SEND)
        sendframe.set_dataL(SetDataValue.END_TRANSACTION)

    def sendNotEndTransaction(self):
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)
        sendframe.set_msg_type(SetDataValue.END_TRANSACTION_SEND)
        sendframe.set_dataL(SetDataValue.NOT_END_TRANSACTION)

    def sendReadConnectorStatus(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)
        sendframe.set_msg_type(messageTypeData.CONNECTOR_STATUS)

    def sendReadChargingStatus(self):
        sendframe.set_cmd_type(cmdTypeData.READ_DATA)    
        sendframe.set_msg_type(messageTypeData.CHARGING_STATUS)    
    
    def sendSetBuzzer(self):    
        sendframe.set_cmd_type(cmdTypeData.SET_DATA)    
        sendframe.set_msg_type(messageTypeData.CLEAR_CHARGE)    
        sendframe.set_dataL(setDataval.get_baz_val())    
            
    async def handleSET_DATA(self):    
        
        self.sendMaxPower()  
        await asyncio.sleep(0.3)
               
        self.sendSetBuzzer()
        await asyncio.sleep(0.3)
        
        self.sendClearChargeSession()
        await asyncio.sleep(0.3)
        
        if(sendframe.dataL== self.setdata.START_CHARGE ):
            
            self.sendStartCharging()    
            await asyncio.sleep(0.3)    
        else:
            self.sendStopCharging()
            await asyncio.sleep(0.3)
        
        if(setDataval.get_transection_val() == self.setdata.END_TRANSACTION):
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



             
async def main():
    rxtx_fonk = RxTxFonk()
    
    
    myUart = UartProtokol(rxtx_fonk)
    uart_handler = UartHandler()
    await asyncio.gather(
        rxtx_fonk.send_message(),
        rxtx_fonk.receive_message(),
        myUart.reciveHandleUartFrame(),
        uart_handler.sendHandleUartFrame()
    )

asyncio.run(main())






