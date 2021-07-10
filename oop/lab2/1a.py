from datetime import datetime

class Flight:
    def __init__(self, flightNo, destination, departureDate):
        self._flightNo = flightNo
        self._destination = destination
        self._departureDate = departureDate

    @property
    def flightNo(self):
        return self._flightNo

    @property
    def destination(self):
        return self._destination

    @property
    def departureDate(self):
        return self._departureDate

    @flightNo.setter
    def flightNo(self, flightNo):
        self._flightNo = flightNo

    @departureDate.setter
    def departureDate(self, departureDate):
        self._departureDate = departureDate

    def __str__(self):
        return '{} {} {:%#d %b %Y %H:%M}'.format(self._flightNo, self._destination, self.departureDate)

class Passenger:
    def __init__(self, name, flight=None): #set as none first 
        self._name = name
        self._flight = flight

    #getter
    @property
    def name(self): return self._name

    #methods
    def changeFlight(self, flight):
        self._flight = flight

    def __str__(self):
        return f'Name: {self._name} Flight: {self._flight}'

flight = Flight('SQ1', 'LA', datetime(2019, 3, 30, 4, 15)) #yyyy, d, mm, - hh, mm
p1 = Passenger('p1', flight)
p2 = Passenger('p2', flight)
print(p1.__str__()) #same as just print(p1)
print(p2)
flight.departureDate = datetime(2019, 3, 29, 15, 25)
print(p1)
print(p2)
print(flight)