import random
from math import sin, cos


class Animal:
    def __init__(self, size, speed, angle, name):
        self.size = size  # size - len & height
        self.speed = speed  # speed - scalar of speed
        self.angle = angle  # angle - direction of movement
        self.name = name
        self.eat = []

    """check what happened if Two Animals come together
        if there is a eat return survivor and what happened 
        if there is no eat than determine randomly who is allowed to move and return order  
    """

    def encounter(self, animal):
        if animal in self.eat:
            print("{} ate {}".format(self.name, animal.name))
            return [self, "ate"]
        if self in animal.eat:
            print("{} ate {}".format(animal.name, self.name))
            return [self, "eaten"]
        if self.random:
            return [self, "move"]
        return [animal, "move"]

    @classmethod
    def random(cls):
        return random.random() > random.random()


class Fish(Animal):
    def __init__(self, fliper, size, speed, angle, name):
        self.fin = fliper
        self.eat = [Plankton]
        super().__init__(size, speed, angle, name)


class Plankton(Animal):
    def __init__(self, size, speed, angle, name):
        super().__init__(size, speed, angle, name)


class Crab(Animal):
    def __init__(self, size, speed, angle, name, strength):
        self.strength = strength
        self.eat = [Plankton, Crab, Fish]
        super().__init__(size, speed, angle, name)
