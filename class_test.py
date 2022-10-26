class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def __str__(self):
        return f"Nome veicolo: {self.name}, mileage: {self.mileage}, capacita': {self.capacity}"


class Bus(Vehicle):
    pass


class Mario(Vehicle):
    pass


vehicle = Vehicle('Fabrizio', 0, "infinito")
print(vehicle)

matas = Vehicle("Riccardo", "Bullo", "no")
print(matas)
