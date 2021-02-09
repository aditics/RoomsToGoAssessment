from datetime import datetime
from inventory import Inventory
from command import *
import readline
import sys
import asyncio
import aiofiles as aiof
from messages import *

if __name__ == "__main__":
    COUNTER = 0
    INV = Inventory()

    while True:
        try:
            rawInput = input(">")
            commands = rawInput.split(' ')

            #ADDING TO THE INVENTORY
            if commands[0] == ADD_COMMAND:
                addToInventory(INV, rawInput, commands)

            #LISTING FROM THE INVENTORY
            elif commands[0] == LIST_COMMAND:
                listFromInventory(INV, commands)

            #STOCK PRODUCT IN THE WAREHOUSE
            elif commands[0] == STOCK_COMMAND:
                stockProduct(INV, commands)

            #UNSTOCK PRODUCT FROM THE WAREHOUSE
            elif commands[0] == UNSTOCK_COMMAND:
                unstockProduct(INV, commands)

            else:
                print(COMMAND_NOT_FOUND_MESSAGE)

            COUNTER += 1
            if COUNTER > 0 and COUNTER % 2 == 0:
                loop = asyncio.get_event_loop()
                loop.run_until_complete(logCommandHistory(COUNTER - 2))

        except KeyboardInterrupt:
            print(KEYBOARD_INTERRUPT)
            sys.exit(0)
        except:
            logError(sys.exc_info()[0])
