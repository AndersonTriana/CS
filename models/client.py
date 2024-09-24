from base.base_model import BaseModelWithRequiredString

#Class
class Client(BaseModelWithRequiredString):

    #Constructor method
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    #Attributes
    _name: str
    _phone: int

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