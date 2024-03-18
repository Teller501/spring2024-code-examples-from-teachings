class Car:
    def __init__(self, make: str, model: str, year: int) -> None:
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f'Make: {self.make}, Model: {self.model}, Year: {self.year}'


class ElectricCar(Car):
    def __init__(self, make: str, model: str, year: int, battery_size: int) -> None:
        super().__init__(make, model, year)
        self._battery_size = battery_size

    def get_description(self):
        return super().get_description() + f", Battery size: {str(self.battery_size)} kWh"

    @property
    def battery_size(self):
        return self._battery_size

    @battery_size.setter
    def battery_size(self, value: int):
        if value < 0:
            raise ValueError("Battery size must be a positive integer")
        self._battery_size = value


audi = Car("Audi", "Q8", 2018)
tesla = ElectricCar("Tesla", "Model X", 2020, 28)

print(audi.get_description())
print(tesla.get_description())
