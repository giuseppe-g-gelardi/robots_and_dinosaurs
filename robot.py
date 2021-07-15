

class Robot:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon
        self.power = 6


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power



