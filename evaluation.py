from numpy import Inf
from goat import Goat
from tiger import Tiger

class Evaluation:

    def __init__(self, goats_killed, tigers_trapped, boardgrid, winner,goats_to_be_placed,best_move,depth = 1):
        self.goats_killed = goats_killed
        self.tigers_trapped = tigers_trapped
        self.boardgrid = boardgrid
        self.winner = winner
        self.goats_to_be_placed = goats_to_be_placed
        self.best_move = best_move
        self.depth = depth

    def evaluation(self,depth=0):
        if self.winner == "Goat":
            return -Inf
        elif self.winner == "Tiger":
            return Inf
        else:
            return 4*self.goats_killed-5*self.tigers_trapped

    def make_move(self,move,player):
        if(player=="Goat"):
            if move[0]==-1:
                self.boardgrid[move[2]][move[3]] = 'G'
                self.goats_to_be_placed -= 1
            else:
                self.boardgrid[move[2]][move[3]] = 'G'
                self.boardgrid[move[0]][move[1]] = '_'
        else:
            if(abs(move[2]-move[0])==2):
                self.boardgrid[move[2]][move[3]] = 'T'
                self.boardgrid[move[0]][move[1]] = '_'
                self.boardgrid[(move[0]+move[2])//2][(move[1]+move[3])//2] = '_'
            else:
                self.boardgrid[move[2]][move[3]] = 'T'
                self.boardgrid[move[0]][move[1]] = '_'

    # def make_move(self, board):
    def revert_move(self,move,player):
        if player=="Goat":
            if move[0]==-1:
                self.boardgrid[move[2]][move[3]] = '_'
                self.goats_to_be_placed += 1
            else:
                self.boardgrid[move[2]][move[3]] = '_'
                self.boardgrid[move[0]][move[1]] = 'G'
        else:
            if abs(move[2]-move[0])==2:
                self.boardgrid[move[2]][move[3]] = '_'
                self.boardgrid[move[0]][move[1]] = 'T'
                self.boardgrid[(move[0]+move[2])//2][(move[1]+move[3])//2] = 'G'
            else:
                self.boardgrid[move[2]][move[3]] = '_'
                self.boardgrid[move[0]][move[1]] = 'T'


    def minimax(self, is_max=True, depth=0, alpha=-Inf, beta=Inf):
        score = self.evaluation(depth)

        if depth == self.depth or abs(score) == Inf:
            return score

        if not is_max:
            value = Inf

            goat = Goat(self.boardgrid,self.goats_to_be_placed)
            moves = goat.possible_goat_movess()
            for move in moves:
                self.make_move(move,"Goat")
                current_value = self.minimax(True, depth + 1, alpha, beta)
                beta = min(beta, current_value)

                if current_value == value and depth == 0:
                    self.best_move = move
                if current_value < value:

                    value = current_value
                    beta = min(beta, value)
                    if depth == 0:
                        self.best_move = move

                self.revert_move(move,"Goat")
                if alpha >= beta:
                    break
            return value

        else:
            value = -Inf
            tiger = Tiger(self.boardgrid,self.tigers_trapped,self.goats_killed)
            moves = tiger.possible_tiger_movess()
            for move in moves:
                self.make_move(move,"Tiger")
                current_value = self.minimax(False, depth + 1, alpha, beta)
                alpha = max(alpha, value)
                if current_value == value and depth == 0:
                    self.best_move = move
                if current_value > value:
                    value = current_value
                    alpha = max(alpha, value)
                    if depth == 0:
                        self.best_move = move
                
                self.revert_move(move,"Tiger")
                if alpha >= beta:
                    break
            return value