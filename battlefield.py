from fleet import Fleet
from herd import Herd

class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd()


    def run_game(self):
        print("inside the run_game method!")
        self.display_welcome()


    def display_welcome(self):
        print("Welcome to Robots vs Dinosaurs!")
        self.initiate_game = input("Would you like to start the game?: 'yes' or 'no': ")
        if self.initiate_game == "yes":
            self.battle()
        if self.initiate_game == "no":
            self.run_game()
        

    def battle(self):
        print("BATTLE!!")
        self.battle_start = input("Who goes first? robots or dinosaurs?: ")
        if self.battle_start == "robots":
            print("ROBOTS ATTACK FIRST")
            self.dino_turn(self)
        if self.battle_start == "dinosaurs":
            print("DINOSAURS ATTACK FIRST!")
            self.robot_turn(self)


        # self.fleet.robot_list[0].attack(self.herd.dino_list[0])
        # self.herd.dino_list[0].attack(self.fleet.robot_list[0])
        # TODO link the different attacks + ability to choose for each respective character


    def dino_turn(self, dinosaur):
        # TODO find a way to alternate dino / robot turns
        pass


    def robot_turn(self, dinosaur):
        # TODO find a way to alternate dino / robot turns
        pass

    def show_dino_opponent_options(self):
        # TODO display robots are left
        pass

    def show_robot_opponent_options(self):
        # TODO display which dinos are left
        pass

    def display_winners(self):
        if len(self.fleet.robot_list) == 0:
            print("DINOSAURS WIN")
        if len(self.herd.dino_list) == 0:
            print("ROBOTS WIN!")           


