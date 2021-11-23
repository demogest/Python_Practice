class Shape:
    def __init__(self, sh, name):
        self.__name = name
        self.__sh = sh

    def __repr__(self):
        return self.__name + ' is ' + self.__sh

    def getName(self):
        return self.__name

    def getShape(self):
        return self.__sh


class Circle(Shape):
    def __init__(self, name: str, radius: int, sh='Circle'):
        super().__init__(sh, name)
        self.__name = name
        self.__sh = sh
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def __repr__(self):
        return "{}'s radius is {}" \
            .format(self.__name, self.__radius)


class Cylinder(Shape):
    def __init__(self, name: str, height, radius, sh="Cylinder"):
        super().__init__(sh, name)
        self.__name = name
        self.__sh = sh
        self.__height = height
        self.__radius = radius

    def __repr__(self):
        return "{}'s radius is {}, height is {}" \
            .format(self.__name, self.__radius, self.__height)

    def getRadius(self):
        return self.__radius

    def getHeight(self):
        return self.__height

    def setRadius(self, radius):
        self.__radius = radius

    def setHeight(self, height):
        self.__height = height


a = Shape('none', 'a')
b = Circle('b', 5)
c = Cylinder('c', 10, 5)
print("{} is {}\n{}'s radius is {}\n{}'s radius is {}, height is {}"
      .format(a.getName(), a.getShape(), b.getName(), b.getRadius(), c.getName(), c.getRadius(), c.getHeight()))
b.setRadius(10)
c.setRadius(20)
c.setHeight(11)
print("{}\n{}\n{}".format(a, b, c))
