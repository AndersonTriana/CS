from base.base_model import BaseModelWithRequiredString
from models.client import Client
from models.product import Product
import streamlit as st

from datetime import datetime

#Class
class Sale(BaseModelWithRequiredString):

    #Constructor method
    def __init__(self, client:Client, date:datetime):
        self._client = client
        self._total_price = 0
        self._total_paid = 0
        self._products = {}
        self._date = date

    #Attributes
    _client: Client
    _total_price: int
    _total_paid: int
    _products: dict
    _date: datetime

    #Encapsulation:
    @property
    def client(self):
        return self._client
    
    @client.setter
    def client(self, client:Client):
        self._client = client

    @property
    def total_price(self):
        return self._total_price
    
    @total_price.setter
    def total_price(self, total_price:int):
        self._total_price = total_price

    @property
    def total_paid(self):
        return self._total_paid
    
    @total_paid.setter
    def total_paid(self, total_paid:int):
        self._total_paid = total_paid

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

    def add_product(self, product:Product, sold_quantity:int, unit_cost:int, value_paid:int):
        if product.name in self._products:
            self._products[product.name]["sold_quantity"] += sold_quantity
        else:
            self._products[product.name] = {
                'product': product,
                'sold_quantity': sold_quantity,
                'unit_cost': unit_cost,
                'value_paid': value_paid
                }
        
        self.calculate_total_price();
        self.calculate_total_paid();

    def remove_product(self, product_name:str):
        if product_name in self._products:
            del self._products[product_name]
        else:
            raise ValueError("The product doesn't exist in the sale")

    def calculate_total_price(self):
        total_price = 0
        for product in self._products:
            total_price += self._products[product]["unit_cost"] * self._products[product]["sold_quantity"]
            
        self._total_price = total_price
        
    def calculate_total_paid(self):
        total_paid = 0
        for product in self._products:
            total_paid += self._products[product]["value_paid"]
            
        self._total_paid = total_paid
