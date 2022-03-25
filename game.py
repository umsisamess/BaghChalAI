
from importlib.util import set_loader
import random

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

    # def board_init(self):
    #     self.boardgrid = [['_' for _ in range(5)] for _ in range(5)]
    #     # Place tiger at corners
    #     self.boardgrid[0][0] = self.boardgrid[0][4] = self.boardgrid[4][0] = self.boardgrid[4][4] = 'T'

    def possible_goat_movess(self):
        self.possible_goat_moves = []
        if self.goats_to_be_placed > 0:
            for i in range(5):
                for j in range(5):
                    if self.boardgrid[i][j]=='_':
                        self.possible_goat_moves.append([-1,-1,i,j])
        else:
            for i in range(5):
                for j in range(5):
                    if self.boardgrid[i][j]=='G':
                        if i-1>=0:
                            if(self.boardgrid[i-1][j] == '_'):
                                self.possible_goat_moves.append([i,j,i-1,j])
                        if i+1<5:
                            if(self.boardgrid[i+1][j] == '_'):
                                self.possible_goat_moves.append([i,j,i+1,j])
                        if j-1>=0:
                            if(self.boardgrid[i][j-1] == '_'):
                                self.possible_goat_moves.append([i,j,i,j-1])
                        if j+1<5:
                            if(self.boardgrid[i][j+1] == '_'):
                                self.possible_goat_moves.append([i,j,i,j+1])

                        if i-1>=0 and j-1>=0 and i%2==j%2:
                            if(self.boardgrid[i-1][j-1] == '_'):
                                self.possible_goat_moves.append([i,j,i-1,j-1])
                        if i-1>=0 and j+1<5 and i%2==j%2:
                            if(self.boardgrid[i-1][j+1] == '_'):
                                self.possible_goat_moves.append([i,j,i-1,j+1])
                        if i+1<5 and j-1>=0 and i%2==j%2:
                            if(self.boardgrid[i+1][j-1] == '_'):
                                self.possible_goat_moves.append([i,j,i+1,j-1])
                        if i+1<5 and j+1<5 and i%2==j%2:
                            if(self.boardgrid[i-1][j-1] == '_'):
                                self.possible_goat_moves.append([i,j,i+1,j+1])
        return self.possible_goat_moves


    def possible_tiger_movess(self):
        possible_tiger_moves = []
        for i in range(5):
            for j in range(5):
                if self.boardgrid[i][j]=='T':
                    if i-1>=0:
                        if(self.boardgrid[i-1][j] == '_'):
                            possible_tiger_moves.append([i,j,i-1,j])
                    if i+1<5:
                        if(self.boardgrid[i+1][j] == '_'):
                            possible_tiger_moves.append([i,j,i+1,j])
                    if j-1>=0:
                        if(self.boardgrid[i][j-1] == '_'):
                            possible_tiger_moves.append([i,j,i,j-1])
                    if j+1<5:
                        if(self.boardgrid[i][j+1] == '_'):
                            possible_tiger_moves.append([i,j,i,j+1])

                    if i-1>=0 and j-1>=0 and i%2==j%2:
                        if(self.boardgrid[i-1][j-1] == '_'):
                            possible_tiger_moves.append([i,j,i-1,j-1])
                    if i-1>=0 and j+1<5 and i%2==j%2:
                        if(self.boardgrid[i-1][j+1] == '_'):
                            possible_tiger_moves.append([i,j,i-1,j+1])
                    if i+1<5 and j-1>=0 and i%2==j%2:
                        if(self.boardgrid[i+1][j-1] == '_'):
                            possible_tiger_moves.append([i,j,i+1,j-1])
                    if i+1<5 and j+1<5 and i%2==j%2:
                        if(self.boardgrid[i+1][j+1] == '_'):
                            possible_tiger_moves.append([i,j,i+1,j+1])

                    if i-2>=0:
                        if(self.boardgrid[i-2][j] == '_' and self.boardgrid[i-1][j]=='G'):
                            possible_tiger_moves.append([i,j,i-2,j])
                    if i+2<5:
                        if(self.boardgrid[i+2][j] == '_' and self.boardgrid[i+1][j]=='G'):
                            possible_tiger_moves.append([i,j,i+2,j])
                    if j-2>=0:
                        if(self.boardgrid[i][j-2] == '_' and self.boardgrid[i][j-1]=='G'):
                            possible_tiger_moves.append([i,j,i,j-2])
                    if j+2<5:
                        if(self.boardgrid[i][j+2] == '_' and self.boardgrid[i][j+1]=='G'):
                            possible_tiger_moves.append([i,j,i,j+2])

                    if i-2>=0 and j-2>=0 and i%2==j%2:
                        if(self.boardgrid[i-2][j-2] == '_' and self.boardgrid[i-1][j-1]=='G'):
                            possible_tiger_moves.append([i,j,i-2,j-2])
                    if i-2>=0 and j+2<5 and i%2==j%2:
                        if(self.boardgrid[i-2][j+2] == '_' and self.boardgrid[i-1][j+1]=='G'):
                            possible_tiger_moves.append([i,j,i-2,j+2])
                    if i+2<5 and j-2>=0 and i%2==j%2:
                        if(self.boardgrid[i+2][j-2] == '_' and self.boardgrid[i+1][j-1]=='G'):
                            possible_tiger_moves.append([i,j,i+2,j-2])
                    if i+2<5 and j+2<5 and i%2==j%2:
                        if(self.boardgrid[i+2][j+2] == '_' and self.boardgrid[i+1][j+1]=='G'):
                            possible_tiger_moves.append([i,j,i+2,j+2])       
        return possible_tiger_moves

    def switch_turn(self):
        if self.current_turn == "Goat":
            self.current_turn = "Tiger"
        else:
            self.current_turn = "Goat"

    def make_a_move(self):
        if self.current_turn == "Goat":
            self.make_a_goat_move()
        else:
            self.make_a_tiger_move()
            self.no_of_moves_made += 1

    def select_random(self,pos_mo):
        n = len(pos_mo)
        return pos_mo[random.randint(0,n-1)]

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
            # self.update_the_position()
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

            
    def is_tiger_winner(self):
        if self.goats_killed>=5:
            return True
        poss_movs = self.possible_goat_movess()
        if len(poss_movs) == 0:
            return True
        return False

    def is_goat_winner(self):
        poss_movs = self.possible_tiger_movess()
        if len(poss_movs) == 0:
            return True
        return False

    def is_game_over(self):
        if self.is_tiger_winner():
            self.winner = "Tiger"
            return True
        elif self.is_goat_winner():
            self.winner = "Goat"
            return True
        elif self.no_of_moves_made==300:
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


        
    
