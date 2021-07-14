

#unique product code, description and unit price.

class Product:
    def __init__(self, productCode, description, unitPrice):
        self._productCode = productCode
        self._description = description
        self._unitPrice = unitPrice

    #getter
    @property
    def productCode(self): return self._productCode

    @property
    def description(self): return self._description

    @property
    def unitPrice(self): return self._unitPrice

    #setter
    @productCode.setter
    def productCode(self, productCode):
        self._productCode = productCode

    @description.setter
    def description(self, description):
        self._description = description

    @unitPrice.setter
    def unitPrice(self, unitPrice):
        self._unitPrice = unitPrice

    #methods
    def __str__(self):
        return f'{self._productCode}, {self._description}, {self._unitPrice}'


p1 = Product(1, 'test', 20)

print(p1.__str__())