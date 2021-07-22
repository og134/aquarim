import Aquarium
import animal

if __name__ == '__main__':
    aquarium = Aquarium.Aquarium(10, 10)
    """
    create animals 
    """
    crab = animal.Crab(1, 1, 45, "mr", 3)
    fish = animal.Fish(2, 1, 2, 45, "dagi")
    plankton = animal.Plankton(1, 3, 70, "shelly")
    """
    enter animals to the aquarium 
    """
    aquarium.animals[crab] = [1, 2]
    aquarium.animals[fish] = [3, 4]
    aquarium.animals[plankton] = [7, 8]
    print(aquarium.animals)
    aquarium.move()
    aquarium.move()
    for animal in aquarium.animals:
        print(animal.angle)
