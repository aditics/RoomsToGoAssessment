import math
from entities import Product
from entities import Warehouse
from entities import Stock
from tabulate import tabulate
from messages import *

class Inventory:

    #INITIALISES DICTIONARIES OF PRODUCTS, WAREHOUSES AND STOCKS
    def __init__(self):
        self.WAREHOUSES = {}
        self.PRODUCTS = {}
        self.STOCKS = {}

    #DETERMINES WHETHER A PRODUCT SKU ALREADY EXISTS IN THE INVENTORY
    def isValidProduct(self,productName, SKU):
        if self.PRODUCTS:
            if (SKU in self.PRODUCTS):
                print(SKU_ERROR_MESSAGE.format(SKU))
                return False
        return True

    #ADDS A PRODUCT TO THE INVENTORY
    def addProduct(self,productName, SKU):
        if self.isValidProduct(productName, SKU):
            self.PRODUCTS[SKU] = Product(productName, SKU)

    #PRINTS ALL PRODUCTS IN THE INVENTORY
    def listAllProducts(self):
        print(PRODUCTS_COMMAND)
        for sku in self.PRODUCTS:
            product  = self.PRODUCTS[sku]
            print(product.productName + ' ' + product.SKU)

    #DETERMINES WHETHER A WAREHOUSE# ALREADY EXISTS IN THE INVENTORY
    def isValidWareHouse(self,warehouseid, stocklimit):
        if self.WAREHOUSES:
            if warehouseid in self.WAREHOUSES:
                print(WAREHOUSE_ERROR_MESSAGE.format(warehouseid))
                return False
        return True

    #ADDS A WAREHOUSE TO THE INVENTORY
    def addWarehouse(self,warehouseid, stocklimit = math.inf):
        if self.isValidWareHouse(warehouseid, stocklimit):
            self.WAREHOUSES[warehouseid] = Warehouse(warehouseid, stocklimit)

    #PRINTS ALL THE WAREHOUSES IN THE INVENTORY
    def listAllWarehouses(self):
        print(WAREHOUSES_COMMAND)
        for warehouseid in self.WAREHOUSES:
            warehouse = self.WAREHOUSES[warehouseid]
            print(warehouse.warehouseId)

    #PRINTS ALL THE PRODUCTS STOCKED IN THE GIVEN WAREHOUSE#
    def listAllWarehousesById(self, warehouseid):
        if warehouseid in self.WAREHOUSES and self.STOCKS:
            stocks = [s for (_, wid), s in self.STOCKS.items() if wid == warehouseid]
            table = []
            for stock in stocks:
                product = self.PRODUCTS[stock.SKU]
                table.append([product.productName, product.SKU, stock.quantity])

            print (tabulate(table, headers=[TABLE_TITLE_ITEM_NAME, TABLE_TITLE_SKU, TABLE_TITLE_QUANTITY]))
        else:
            print(WAREHOUSE_INVALID_ERROR_MESSAGE.format(warehouseid))

    #DETERMINES WHETHER THE GIVEN SKU AND WAREHOUSE# ARE VALID
    def isValidStock(self, SKU, warehouseid):
        if SKU not in self.PRODUCTS:
            print(PRODUCT_INVALID_ERROR_MESSAGE.format(SKU))
            return False
        if warehouseid not in self.WAREHOUSES:
            print(WAREHOUSE_INVALID_ERROR_MESSAGE.format(warehouseid))
            return False
        return True

    #STOCKS THE GIVEN QUANTITY OF A PRODUCT IN THE WAREHOUSE
    def stockProductInWarehouse(self, SKU, warehouseid, quantity):
        if self.isValidStock(SKU, warehouseid):
            warehouse = self.WAREHOUSES[warehouseid]

            if (SKU, warehouseid) in self.STOCKS:
                stockQuantity = stock.quantity + int(quantity)
                self.STOCKS[(SKU, warehouseid)].quantity = stockQuantity if stockQuantity < warehouse.stockLimit else warehouse.stockLimit
            else:
                stockQuantity = min(warehouse.stockLimit, int(quantity))
                self.STOCKS[(SKU, warehouseid)] = Stock(SKU, warehouseid, min(warehouse.stockLimit, stockQuantity))

    #UNSTOCKS THE GIVEN QUANTITY OF A PRODUCT FROM THE WAREHOUSE
    def unstockProductInWarehouse(self, SKU, warehouseid, quantity):
        if self.isValidStock(SKU, warehouseid) and (SKU, warehouseid) in self.STOCKS:
            stockRemaining = self.STOCKS[(SKU, warehouseid)].quantity - int(quantity)
            self.STOCKS[(SKU, warehouseid)].quantity = stockRemaining if stockRemaining >= 0 else 0
        else:
            print(PRODUCT_NOT_FOUND.format(SKU, warehouseid))

    #PRINTS ALL STOCKS
    def listStocks(self):
        for s in self.STOCKS:
            print(self.STOCKS[s].SKU + " " + self.STOCKS[s].warehouseId + " " + str(self.STOCKS[s].quantity))
