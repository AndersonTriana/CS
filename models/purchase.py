from base.base_model import BaseModelWithRequiredString
from models.vendor import Vendor
from models.product import Product
import streamlit as st

from datetime import datetime

#Class
class Purchase(BaseModelWithRequiredString):

    #Constructor method
    def __init__(self, vendor:Vendor, date:datetime):
        self._vendor = vendor
        self._total_price = 0
        self._products = {}
        self._date = date

    #Attributes
    _vendor: Vendor
    _total_price: int
    _products: dict
    _date: datetime

    #Encapsulation:
    @property
    def vendor(self):
        return self._vendor
    
    @vendor.setter
    def vendor(self, vendor:Vendor):
        self._vendor = vendor

    @property
    def total_price(self):
        return self._total_price
    
    @total_price.setter
    def total_price(self, total_price:int):
        self._total_price = total_price

    @property
    def value_paid(self):
        return self._total_price
    
    @value_paid.setter
    def value_paid(self, value_paid:int):
        self._total_price = value_paid

    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, date:datetime):
        self._date = date

    def add_product(self, product:Product, purchased_quantity:int, unit_cost:int):
        if product.name in self._products:
            self._products[product.name]["purchased_quantity"] += purchased_quantity
        else:
            self._products[product.name] = {
                'product': product,
                'purchased_quantity': purchased_quantity,
                'unit_cost': unit_cost
                }

    def remove_product(self, product_name:str):
        if product_name in self._products:
            del self._products[product_name]
        else:
            raise ValueError("The product doesn't exist in the purchase")

    def calculate_total_price(self):
        total_price = 0
        for product in self._products:
            total_price += self._products[product]["unit_cost"] * self._products[product]["purchased_quantity"]
            
        self._total_price = total_price
