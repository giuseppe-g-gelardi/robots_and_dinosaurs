from dinosaur import Dinosaur

class Herd:
    def __init__(self):
        self.dino_list = []


    def create_herd(self):
        self.dino_list.append(Dinosaur("Bethany", 150, 25))
        self.dino_list.append(Dinosaur("Staphanie", 225, 20))
        self.dino_list.append(Dinosaur("Deathany", 222, 20))

