#coding:utf-8

class Fruit:
    price = 0

    def __init__(self):
        self.__color = "red"
        Fruit.price += 1

    def getcolor(self):
        print self.__color

    @classmethod
    def getPriceclassmethod(cls):
        print(cls.price)


    @staticmethod
    def getpricestaticmethod():
        print 'this is staticmethod.'




if __name__ == "__main__":

    apple = Fruit()
    apple.getcolor()

    apple.getPriceclassmethod()
    Fruit.getpricestaticmethod()


    Fruit.getpricestaticmethod()
    Fruit.getPriceclassmethod()

    banana = Fruit()










'''

class Car:
    class Door:
        def open(self):
            print('open door')

    class Wheel:
        def run(self):
            print('car run')


if __name__ == "__main__":
    car = Car()

    backDoor = Car.Door()

    frontDoor = car.Door()

    backDoor.open()
    frontDoor.open()

    wheel = car.Wheel()
    wheel.run()
'''
