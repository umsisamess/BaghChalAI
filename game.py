
from importlib.util import set_loader
import random
from tiger import Tiger
from goat import Goat
from evaluation import Evaluation

from numpy import Inf

goatwins = 0
tigerwins = 0

class Game:
    def initi(self):
        self.no_of_goat_wins = 0
        self.no_of_tiger_wins = 0

    def __init__(self):
        self.current_turn = "Goat"
        self.winner = None
        self.goats_to_be_placed = 20
        self.goats_killed = 0
        self.tigers_trapped = 0
        self.no_of_moves_made = 0
        
        self.boardgrid = [['_' for _ in range(5)] for _ in range(5)]
        # Place tiger at corners
        self.boardgrid[0][0] = self.boardgrid[0][4] = self.boardgrid[4][0] = self.boardgrid[4][4] = 'T'

    # def is_draw(self):
    #     if self.repeat==3:
    #         return True

    def switch_turn(self):
        if self.current_turn == "Goat":
            self.current_turn = "Tiger"
        else:
            self.current_turn = "Goat"

    def make_a_move(self):
        if self.current_turn == "Goat":
            goat = Goat(self.boardgrid,self.goats_to_be_placed)
            goat.make_a_goat_move()
        else:
            tiger = Tiger(self.boardgrid,self.tigers_trapped,self.goats_killed)
            tiger.make_a_tiger_move()
            self.no_of_moves_made += 1

    def play(self):
        self.__init__()
        
        while self.is_game_over() == False:
            self.make_a_move()
            self.switch_turn()
        print(self.no_of_moves_made)
        if self.winner == "Goat":
            print("Goat has won the game")
            self.no_of_goat_wins += 1
        elif self.winner == "Tiger":
            print("Tiger has won the game")
            self.no_of_tiger_wins += 1
        else:
            print("The game ended in the draw")

        print("No of goat wins :: ",self.no_of_goat_wins)
        print("No of tiger wins :: ",self.no_of_tiger_wins)


    def is_goat_winner(self):
        tiger = Tiger(self.boardgrid,self.tigers_trapped,self.goats_killed)
        poss_movs = tiger.possible_tiger_movess()
        if len(poss_movs) == 0:
            return True
        return False

    def is_tiger_winner(self):
        if self.goats_killed>=5:
            return True
        goat = Goat(self.boardgrid,self.goats_to_be_placed)
        poss_movs = goat.possible_goat_movess()
        if len(poss_movs) == 0:
            return True
        return False

    def is_game_over(self):
        if self.is_tiger_winner():
            self.winner = "Tiger" 
            return True
        elif self.is_goat_winner():
            self.winner = "Goat"
            print(self.boardgrid)   
            return True
        elif self.no_of_moves_made==300:
            self.winner = None
            return True
        else:
            return False   

    


game = Game()
game.initi()
i = 10

while(i):
    game.play()
    i -= 1


        
    
