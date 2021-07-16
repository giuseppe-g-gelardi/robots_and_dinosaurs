class Dinosaur:
    def __init__(self, name: str, attack_power: int, health: int):
        self.name = name
        self.attack_power = attack_power
        self.health = health


    def attack(self, robot, attack_list):
        robot.health -= self.attack_power
        # self.attack_list = ("Chomp", "Tail slap", "Stomp" )
        # TODO connect attack list and set up the ability to select which attack to use
