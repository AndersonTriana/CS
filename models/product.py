from base.base_model import BaseModelWithRequiredString

#Class
class Product(BaseModelWithRequiredString):

    #Constructor method
    def __init__(self, name, suggested_price=0, stock=0):
        self._name = name
        self._suggested_price = suggested_price
        self._stock = stock

    #Attributes
    _name: str
    _suggested_price: float
    _stock: float

    #Encapsulation:
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = self.validate_req_str_value(property_name="name", value=value)

    @property
    def suggested_price(self):
        return self._suggested_price
    
    @suggested_price.setter
    def suggested_price(self, value: float):
        self._suggested_price = value

    @property
    def stock(self):
        return self._stock
    
    @stock.setter
    def stock(self, value: float):
        self._stock = value