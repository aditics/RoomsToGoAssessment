global ADD_COMMAND
global LIST_COMMAND
global STOCK_COMMAND
global UNSTOCK_COMMAND
global PRODUCT_COMMAND
global WAREHOUSE_COMMAND
global PRODUCTS_COMMAND
global WAREHOUSES_COMMAND

global KEYBOARD_INTERRUPT
global COMMAND_NOT_FOUND_MESSAGE
global ADD_PRODUCT_MESSAGE
global ADD_WAREHOUSE_MESSAGE
global LIST_PRODUCT_MESSAGE
global LIST_WAREHOUSES_MESSAGE
global LIST_WAREHOUSE_ID_MESSAGE
global STOCK_MESSAGE
global UNSTOCK_MESSAGE
global COMMAND_LOG_FILENAME
global ERROR_LOG_FILENAME
global EXCEPTION_MESSAGE

global SKU_ERROR_MESSAGE
global WAREHOUSE_ERROR_MESSAGE
global PRODUCT_INVALID_ERROR_MESSAGE
global WAREHOUSE_INVALID_ERROR_MESSAGE
global PRODUCT_NOT_FOUND
global TABLE_TITLE_ITEM_NAME
global TABLE_TITLE_SKU
global TABLE_TITLE_QUANTITY

ADD_COMMAND = "ADD"
LIST_COMMAND = "LIST"
STOCK_COMMAND = "STOCK"
UNSTOCK_COMMAND = "UNSTOCK"
PRODUCT_COMMAND = "PRODUCT"
WAREHOUSE_COMMAND = "WAREHOUSE"
PRODUCTS_COMMAND = "PRODUCTS"
WAREHOUSES_COMMAND = "WAREHOUSES"

KEYBOARD_INTERRUPT = "Interrupted"
COMMAND_NOT_FOUND_MESSAGE = "COMMAND NOT FOUND!"
ADD_PRODUCT_MESSAGE = "To add a product type: ADD PRODUCT \"PRODUCT NAME\" SKU \n e.g. ADD PRODUCT \"BED\" 5ce956fa-a71e-4bfb-b6ae-5eeaa5eb0a70"
ADD_WAREHOUSE_MESSAGE = "To add a warehouse type: ADD WAREHOUSE WAREHOUSE# [STOCK_LIMIT] \n e.g. ADD WAREHOUSE 45"
LIST_PRODUCT_MESSAGE = "To print all products type: LIST PRODUCTS"
LIST_WAREHOUSES_MESSAGE = "To print all warehouses type: LIST WAREHOUSES"
LIST_WAREHOUSE_ID_MESSAGE = "To print all product details of a warehouse type: LIST WAREHOUSE WAREHOUSE# \n e.g. LIST WAREHOUSE 970"
STOCK_MESSAGE = "To stock a product type: STOCK SKU WAREHOUSE# QTY \n e.g. STOCK 385308505-0767-453f-89af-d11c809ebb3b 970 1000"
UNSTOCK_MESSAGE = "To unstock a product type: UNSTOCK SKU WAREHOUSE# QTY \n e.g. UNSTOCK 385308505-0767-453f-89af-d11c809ebb3b 970 800"
COMMAND_LOG_FILENAME = "INVENTORY COMMAND LOG.txt"
ERROR_LOG_FILENAME = "ERROR.txt"
EXCEPTION_MESSAGE = "An unexpected error has been encountered. Please refer the ERROR.TXT file."

SKU_ERROR_MESSAGE = "ERROR ADDING PRODUCT PRODUCT with SKU {} ALREADY EXISTS"
WAREHOUSE_ERROR_MESSAGE = "ERROR ADDING WAREHOUSE WAREHOUSE with WAREHOUSE# {} ALREADY EXISTS"
PRODUCT_INVALID_ERROR_MESSAGE = "Product {} does not exist."
WAREHOUSE_INVALID_ERROR_MESSAGE = "Warehouse {} does not exist."
PRODUCT_NOT_FOUND = "Product {0} is not stocked in Warehouse {1}"
TABLE_TITLE_ITEM_NAME = "ITEM NAME"
TABLE_TITLE_SKU = "SKU"
TABLE_TITLE_QUANTITY = "QTY"
