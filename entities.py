
import math

class Product:
    def __init__(self, name=None, sku=None):
        self.productName = name
        self.SKU = sku

class Warehouse:
    def __init__(self, warehouseid=None, stocklimit=math.inf):
        self.warehouseId = warehouseid
        self.stockLimit = stocklimit

class Stock:
    def __init__(self, sku, warehouseid, quantity):
        self.SKU = sku
        self.warehouseId = warehouseid
        self.quantity = quantity
