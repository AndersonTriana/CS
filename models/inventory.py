import models.product as Product
from base.base_model import BaseModelWithRequiredString

#Class
class Inventory(BaseModelWithRequiredString):

    #Constructor method
    def __init__(self):
        self._products = {}

    #Attributes
    _products: dict

    #Encapsulation:
    @property
    def products(self):
        return self._products

    def add_product(self, product:Product, stock:int):
        if product.name in self._products:
            self._products[product.name]["stock"] += stock
        else:
            self._products[product.name] = {'product': product, 'stock': stock}

    def remove_product(self, product_name:str):
        if product_name in self._products:
            del self._products[product_name]
        else:
            raise ValueError("The product doesn't exist in Inventory")

    def get_product_stock(self, product_name:str):
        if product_name in self._products:
            return self._products[product_name]["stock"]
        else:
            raise ValueError("The product doesn't exist in Inventory")

    def update_stock(self, product_name:str, new_stock:int):
        if product_name in self._products:
            self._products[product_name]["stock"] = new_stock
        else:
            raise ValueError("The product doesn't exist in Inventory")
