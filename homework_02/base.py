from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption):
        self.weight = weight
        self.started = False
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption

    def start(self):
        if self.fuel > 0 or self.started is True:
            self.started = True
        else:
            raise LowFuelError

    def move(self, distance):
        if self.fuel - distance * self.fuel_consumption >= 0:
            self.fuel = self.fuel - distance * self.fuel_consumption
        else:
            raise NotEnoughFuel
