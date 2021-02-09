from datetime import datetime
from inventory import Inventory
import readline
import sys
import asyncio
import aiofiles as aiof
from messages import *

#LOGS COMMANDS ISSUED IN THE SYSTEM
async def  logCommandHistory(count):
    async with aiof.open(COMMAND_LOG_FILENAME, "a") as out:
        for i in range(count, readline.get_current_history_length()):
            message = datetime.now().strftime("%B %d, %Y %H:%M:%S") + " " + readline.get_history_item(i)
            await out.write("\n" + message)
        await out.flush()
        await out.close()

#LOGS UNEXPECTED ERRORS ENCOUNTERED IN THE SYSTEM
def logError(errorMessage):
    f = open(ERROR_LOG_FILENAME, "a")
    f.write("\n" + str(errorMessage))
    print(EXCEPTION_MESSAGE)
    f.close()

#ADDS PRODUCTS/WAREHOUSE TO THE INVENTORY
def addToInventory(INV, rawInput, commands):
    try:
        if commands[1] == PRODUCT_COMMAND:
            arguments = rawInput.split("\"")
            INV.addProduct(arguments[1].strip(), arguments[2].strip())

        elif commands[1] == WAREHOUSE_COMMAND:
            if len(commands) > 3:
                INV.addWarehouse(commands[2].strip(), int(commands[3].strip()))
            else:
                INV.addWarehouse(commands[2].strip())
        else:
            print(COMMAND_NOT_FOUND_MESSAGE)
            print(ADD_PRODUCT_MESSAGE)
            print(ADD_PRODUCT_MESSAGE)
    except:
        print(ADD_PRODUCT_MESSAGE)
        print(ADD_PRODUCT_MESSAGE)

#LISTS PRODUCTS/WAREHOUSES FROM THE INVENTORY
def listFromInventory(INV, commands):
    try:
        if commands[1] == PRODUCTS_COMMAND:
            INV.listAllProducts()

        elif commands[1] == WAREHOUSES_COMMAND:
            INV.listAllWarehouses()

        elif commands[1] == WAREHOUSE_COMMAND:
            INV.listAllWarehousesById(commands[2])
        else:
            print(COMMAND_NOT_FOUND_MESSAGE)
            print(LIST_PRODUCT_MESSAGE)
            print(LIST_WAREHOUSES_MESSAGE)
            print(LIST_WAREHOUSE_ID_MESSAGE)
    except:
        print(LIST_PRODUCT_MESSAGE)
        print(LIST_WAREHOUSES_MESSAGE)
        print(LIST_WAREHOUSE_ID_MESSAGE)

#STOCKS A PRODUCT IN THE WAREHOUSE
def stockProduct(INV, commands):
    if len(commands) == 4:
        INV.stockProductInWarehouse(commands[1].strip(), commands[2].strip(), commands[3].strip())
    else:
        print(STOCK_MESSAGE)

#UNSTOCKS A PRODUCTS FROM THE WAREHOUSE
def unstockProduct(INV, commands):
    if len(commands) == 4:
        INV.unstockProductInWarehouse(commands[1].strip(), commands[2].strip(), commands[3].strip())
    else:
        print(UNSTOCK_MESSAGE)
