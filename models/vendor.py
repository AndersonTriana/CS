from base.base_model import BaseModelWithRequiredString

#Class
class Vendor(BaseModelWithRequiredString):

    #Constructor method
    def __init__(self, name, phone, website):
        self.name = name
        self.phone = phone
        self.website = website

    #Attributes
    _name: str
    _phone: int
    _website: str

    #Encapsulation:
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value: str):
        self._name = self.validate_req_str_value(property_name="name", value=value)

    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value: int):
        self._phone = value

    @property
    def website(self):
        return self._website
    
    @website.setter
    def website(self, value: str):
        self._website = value