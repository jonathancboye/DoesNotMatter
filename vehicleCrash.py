from functools import reduce
from os import linesep

def vehicleFactory(make):
    return lambda model, year: createVehicle(make, model, year)

def createVehicle(make, model, year):
    return {
        "Make": make,
        "Model": model,
        "Year": year
    }

def printVehicle(vehicle):
    print(vehicleToString(vehicle))


def vehicleToString(vehicle):
    stringPairs = [
        pairToString(k, v) for k, v in vehicle.items()
    ]
    return reduce(concat, stringPairs, '')


def pairToString(key, value):
    return key + ": " + value + linesep

def concat(first, second): return first + second

toyotaFactory = vehicleFactory("Toyota")
camry = toyotaFactory("Camry", "1990")
prius = toyotaFactory("Prius", "2000")

printVehicle(camry)
printVehicle(prius)

