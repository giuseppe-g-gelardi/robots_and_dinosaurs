class Dinosaur:
    def __init__(self, name: str, attack_power: int, health: int):
        self.name = name
        self.attack_power = attack_power
        self.health = health


    def attack(self, robot):
        robot.health -= self.attack_power
