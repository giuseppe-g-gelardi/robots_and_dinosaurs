from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        print("inside the run_game method!")


    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")
        self.initiate_game = input("Would you like to start the game?: 'yes' or 'no' ")
        

    def battle(self):
        self.fleet.robot_list[0].attack(self.herd.dino_list[0])


    def dino_turn(self, dinosaur):
        pass


    def robot_turn(self, dinosaur):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robot_opponent_options(self):
        pass

    def display_winners(self):
        pass
            

