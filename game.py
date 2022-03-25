
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
        self.best_move = None
        
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

    def make_a_best_move(self):
        if self.current_turn == "Goat":
            self.make_a_best_goat_move()
            print(self.boardgrid)
        else:
            self.make_a_best_tiger_move()
            print(self.boardgrid)
            self.no_of_moves_made += 1

    def make_a_best_goat_move(self):
        eval = Evaluation(self.goats_killed,self.tigers_trapped,self.boardgrid,self.winner, self.goats_to_be_placed,self.best_move)
        # print(self.best_move)
        eval.minimax(False)
        self.make_move_goat(eval.best_move)

    def make_a_best_tiger_move(self):
        eval = Evaluation(self.goats_killed,self.tigers_trapped,self.boardgrid,self.winner, self.goats_to_be_placed,self.best_move)
        eval.minimax(True)
        self.make_move_tiger(eval.best_move)

    def make_move_goat(self,move_to_be_made):
        if len(move_to_be_made)==0:
            print('ok')
            return
        if move_to_be_made[0] == -1:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'G'
            self.goats_to_be_placed -= 1
        else:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'G'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'

    def make_move_tiger(self,move_to_be_made):
        if len(move_to_be_made)==0:
            return
        if abs(move_to_be_made[2]-move_to_be_made[0])==2 or abs(move_to_be_made[3]-move_to_be_made[1])==2:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'T'
            self.boardgrid[(move_to_be_made[2]+move_to_be_made[0])//2][(move_to_be_made[3]+move_to_be_made[1])//2] = '_'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'
            self.goats_killed += 1
        else:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'T'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'


    def make_a_goat_move(self):
        possible_moves = self.possible_goat_movess()
        move_to_be_made = self.select_random(possible_moves)
        if move_to_be_made[0] == -1:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'G'
            self.goats_to_be_placed -= 1
        else:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'G'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'
        


    def make_a_tiger_move(self):
        possible_moves = self.possible_tiger_movess()
        move_to_be_made = self.select_random(possible_moves)

        if abs(move_to_be_made[2]-move_to_be_made[0])==2 or abs(move_to_be_made[3]-move_to_be_made[1])==2:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'T'
            self.boardgrid[(move_to_be_made[2]+move_to_be_made[0])//2][(move_to_be_made[3]+move_to_be_made[1])//2] = '_'
            self.goats_killed += 1
        else:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'T'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'

    def play(self):
        self.__init__()
        
        while self.is_game_over() == False:
            self.make_a_move()
            # self.make_a_best_move()
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

    def select_random(self,pos_mo):
        n = len(pos_mo)
        return pos_mo[random.randint(0,n-1)]

    def is_game_over(self):
        if self.is_tiger_winner():
            self.winner = "Tiger" 
            return True
        elif self.is_goat_winner():
            self.winner = "Goat"
            # print(self.boardgrid)   
            return True
        elif self.no_of_moves_made==1000:
            self.winner = None
            return True
        else:
            return False   

    


game = Game()
game.initi()
i = 1000

while(i):
    game.play()
    i -= 1


        
    
