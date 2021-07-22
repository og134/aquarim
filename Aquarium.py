import animal
from math import sin, cos


class Aquarium:
    def __init__(self, height, length):
        self.Height = height
        self.length = length
        self.animals = {}  # dict of tha object and there place re presented as x * y


    """
    @property
    def animals(self):
        return self._animals
    @animals.setter
    def animals(self,animal,place):
        self._animals[animal] = place
    """

    def move(self):
        for animal in self.animals:
            self.animals[animal] = self.define_move(self.animals[animal], animal)

    def define_move(self, place, animal):
        x_animal, y_animal = place
        x_animal += animal.speed * sin(animal.angle)
        y_animal += animal.speed * cos(animal.angle)
        change_angle = False
        if x_animal > self.length:
            change_angle = True
            x_animal = 2 * self.length - x_animal
            """
             example :
             length = 9 , x_animal = 11 
             means at the end x animal needs to be 7 
             x_animal = self.length - (x_animal - self.length) and after bit of magic called math 
             x_animal = 2 * self.length - x_animal 
            """
        if y_animal > self.Height:
            change_angle = True
            y_animal = 2 * self.Height - y_animal
        if x_animal < 0:
            change_angle = True
            x_animal = abs(x_animal)
        if y_animal < 0:
            change_angle = True
            y_animal = abs(y_animal)
        if change_angle:
            animal.angle = 360 - animal.angle
        return [x_animal, y_animal]
