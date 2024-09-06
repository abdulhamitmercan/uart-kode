from UARTASYNC1 import UARTFrame, recieveframe, sendframe, RxTxFonk
from uart_PROTOCOL import UartProtokol, RxTxFonk
import asyncio







STOP_CHARGE = 2
START_CHARGE = 1
async def main():
    rxtx_fonk = RxTxFonk()
    myUart = UartProtokol(rxtx_fonk)    
    await asyncio.gather(rxtx_fonk.send_message(), rxtx_fonk.receive_message(), myUart.handleUartFrame())
    
asyncio.run(main())
