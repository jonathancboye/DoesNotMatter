import os

def createVehicle(make, model):
    return lambda speed: (make, model, speed)

def printVehicle(vehicle):
    print(carTupleToString(vehicle))

def carTupleToString(vehicle):
    result = ""
    result += f'Make: {vehicle[0]}'
    result += '\n'
    result += f'Model: {vehicle[1]}'
    result += '\n'
    result += f'Speed: {vehicle[2]}'
    result += '\n'
    return result

vehicle = createVehicle("Toyota", "Camry", "20mph")
printVehicle(vehicle)