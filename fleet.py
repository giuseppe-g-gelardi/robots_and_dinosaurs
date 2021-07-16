from robot import Robot
from weapon import Weapon

class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()


    def create_fleet(self):
        self.robot_list.append(Robot("Robby", 100, Weapon("Torch Hammer", 10)))
        self.robot_list.append(Robot("Bawby", 100, Weapon("Line Rifle", 10)))
        self.robot_list.append(Robot("Dhaby", 100, Weapon("Slap Rifle", 10)))
        # * used Weapons named from the game Destiny 2
        # TODO set up the ability to choose the different weapons in battle
