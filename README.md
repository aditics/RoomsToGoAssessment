# Product Inventory Management System

## Package Requirements

###### Readline: 
```bash
pip install pyreadline
```

###### Tabulate:
```bash
pip install tabulate
```

###### Aync IO:
```bash
pip install asyncio
pip install aiofiles
```

## Run the application
```
python inventoryManagement.py
```

## Commands

###### Add a new product to the product catalog
```
> ADD PRODUCT "PRODUCT NAME" SKU
```

###### Create a new warehouse to stock products
```
> ADD WAREHOUSE WAREHOUSE# [STOCK_LIMIT]
```

###### Stock QTY nos. of product with SKU in WAREHOUSE#
```
> STOCK SKU WAREHOUSE# QTY
```

###### Unstock QTY nos. of product with SKU in WAREHOUSE#
```
> UNSTOCK SKU WAREHOUSE# QTY
```

###### List all products in the product catalog
```
> LIST PRODUCTS
```

###### List all warehouses
```
> LIST WAREHOUSES
```

###### List information about all the products in the WAREHOUSE#
```
> LIST WAREHOUSE WAREHOUSE#
```


## License
[MIT](https://choosealicense.com/licenses/mit/)