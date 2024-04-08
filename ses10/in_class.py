class Person:

    gender = 'Male'  # class variable

    def __init__(self):
        self.name = 'Anders'  # public instance variable
        self._variable = 12  # an agreement that it is to be a private variable
        self._age = 14
        self.gender = 'male'  # public variable changed to a property

    @property
    def gender(self):
        """Gender variable"""
        return self._gender

    @gender.setter
    def gender(self, gender):
        if gender in ['male', 'female']:
            self._gender = gender

    def set_age(self, age):
        if age < 0:
            print('Error')
        else:
            self._age = age

    def get_age(self):
        return self.age

# Ex 1: Car object


class Car:
    def __init__(self, make=None, model=None, bhp=None, mph=None):
        self.make = make
        self.model = model
        self.bhp = bhp
        self.mph = mph

    @property
    def make(self):
        return self._make

    @make.setter
    def make(self, make):
        if make in ['bmw', 'volvo']:
            self._make = make

    @property
    def model(self):
        return self._model

    @model.setter
    def model(self, model):
        if isinstance(model, str):
            self._model = model

    @property
    def bhp(self):
        return self._bhp

    @bhp.setter
    def bhp(self, bhp):
        if bhp > 0:
            self._bhp = bhp
        else:
            raise ValueError('must be a positive number')

    @property
    def mph(self):
        return self._mph

    @mph.setter
    def mph(self, mph):
        if mph > 0:
            self._mph = mph
        else:
            raise ValueError('must be a positive number')

# Ex 2. Don´t break the public interface


class Square:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, height):
        if height > 0:
            self._height = height
        else:
            raise ValueError('Must be a positive number')

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, width):
        if width > 0:
            self._width = width
        else:
            raise ValueError('Must be a positive number')


# Ex: Create an imutable object
class Card:
    def __init__(self, value, suit):
        self._value = value
        self._suit = suit

    @property
    def value(self):
        return self._value

    @property
    def suit(self):
        return self._suit

    def __repr__(self) -> str:
        return f'{self.value} of {self.suit}'


#Ex: Number object (logic)
class Number:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if self._value is not None and value < self._value:
            raise ValueError('Value must be greater than previous value')
        self._value = value
