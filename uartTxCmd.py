import asyncio
from uart_PROTOCOL import UartProtokol
from UARTASYNC1 import RxTxFonk

async def main():
    rxtx_fonk = RxTxFonk()
    myUart = UartProtokol(rxtx_fonk)
    
    await asyncio.gather(
        rxtx_fonk.send_message(),
        rxtx_fonk.receive_message(),
        myUart.handleUartFrame()
    )

asyncio.run(main())




STOP_CHARGE = 2
START_CHARGE = 1

