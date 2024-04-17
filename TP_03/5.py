import os

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        # Primero el chasis
        body = self.__builder.getBody()
        car.setBody(body)

        # Luego el motor
        engine = self.__builder.getEngine()
        car.setEngine(engine)

        # Finalmente (4) ruedas
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        # Retorna el vehiculo completo
        return car

    def getAirplane(self):
        airplane = Airplane()

        body = self.__builder.getBody()
        airplane.setBody(body)

        engine = self.__builder.getEngine()
        airplane.setEngine(engine)

        i = 0
        while i < 8:
            wheel = self.__builder.getWheel()
            airplane.attachWheel(wheel)
            i += 1

        i = 0
        while i < 2:
            turbine = self.__builder.getTurbine()
            airplane.setTurbine(turbine)
            i += 1

        undercarriage = self.__builder.getUndercarriage()
        airplane.setUndercarriage(undercarriage)

        i = 0
        while i < 2:
            wing = self.__builder.getWing()
            airplane.setWing(wing)
            i += 1

        return airplane

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def specification(self):
        print ("chasis: %s" % (self.__body.shape))
        print ("planta motora: %d" % (self.__engine.horsepower))
        print ("ruedas: %d\'" % (self.__wheels[0].size))

class Airplane:
    def __init__(self):
        self.__body = None
        self.__engine = None
        self.__undercarriage = None
        self.__turbines = list()
        self.__wings = list()
        self.__wheels = list()

    def setBody(self, body):
        self.__body = body

    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def setEngine(self, engine):
        self.__engine = engine

    def setUndercarriage(self, undercarriage):
        self.__undercarriage =  undercarriage

    def setTurbine(self, turbine):
        self.__turbines.append(turbine)

    def setWing(self, wing):
        self.__wings.append(wing)

    def specification(self):
        print('')
        print ("chasis: %s" % (self.__body.shape))
        print ("planta motora: %d" % (self.__engine.horsepower))
        print ("ruedas: %d\'" % (self.__wheels[0].size))
        print(f'tiene {len(self.__turbines)} turbinas')
        print(f'tiene {len(self.__wings)} alas')
        print(f'¿tiene tren de aterrizaje?: {self.__undercarriage is not None}')

class Builder:
    def getWheel(self): pass
    def getEngine(self): pass
    def getBody(self): pass
    def setUndercarriage(self): pass
    def setTurbine(self): pass
    def setWing(self): pass

class JeepBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

class AirplaneBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 50
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 4000
        return engine

    def getBody(self):
        body = Body()
        body.shape = "body airplane"
        return body

    def getUndercarriage(self):
        undercarriage = Undercarriage()
        return undercarriage

    def getTurbine(self):
        turbine = Turbine()
        return turbine

    def getWing(self):
        wing = Wing()
        return wing

class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None

class Undercarriage():
    size = None

class Turbine():
    horsepower = None

class Wing():
    size = None

def main():
    jeepBuilder = JeepBuilder()
    director = Director()
    director.setBuilder(jeepBuilder)

    jeep = director.getCar()
    jeep.specification()

    airplaneBuilder = AirplaneBuilder()
    director.setBuilder(airplaneBuilder)

    airplane = director.getAirplane()
    airplane.specification()

if __name__ == "__main__":
    os.system("clear")
    print("Ejemplo de un patrón de tipo builder aplicado a la construcción de un vehículo\n")

    main()
