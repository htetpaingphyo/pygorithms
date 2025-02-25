# static method belongs to the class itself, not to any specific instance of the class
class ClassOne:
    @staticmethod
    def get_data():
        print("Hello, this is a static method")


ClassOne.get_data()


# class method also belongs to the class itself, but it receives the class (cls) as its first argument
class ClassTwo:
    x = 10
    y = 20

    @classmethod
    def modify_data(cls, x, y):
        cls.x = x
        cls.y = y

    def __str__(self):
        return f"x: {self.x}, y: {self.y}"


inst_one = ClassTwo()
ClassTwo.modify_data(100, 200)


# @property transforms a method into a "getter" for a class attribute
class ClassThree:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    @property
    def point(self):
        return f"x: {self._x}, y: {self._y}"

    @point.setter  # setter decorator comes with "@property"
    def point(self, value):
        self._x = value[0]
        self._y = value[1]


inst_two = ClassThree(40, 50)
print(inst_two.point)

inst_two.point = [50, 60]
print(inst_two.point)
