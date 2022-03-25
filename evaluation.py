from numpy import Inf
from goat import Goat
from tiger import Tiger

class Evaluation:

    def __init__(self, goats_killed, tigers_trapped, boardgrid, winner,goats_to_be_placed):
        self.goats_killed = goats_killed
        self.tigers_trapped = tigers_trapped
        self.boardgrid = boardgrid
        self.winner = winner
        self.goats_to_be_placed = goats_to_be_placed
        self.best_move = None

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

    def minimax(self, is_max=True, depth=0, alpha=-Inf, beta=Inf):
        score = self.evaluation(depth)

        if depth == self.depth or abs(score) == Inf:
            return score

        if not is_max:
            value = Inf

            goat = Goat(self.boardgrid,self.goats_to_be_placed)
            for move in goat.possible_goat_movess():
                goat.make_move_goat(move)
                current_value = self.minimax(True, depth + 1, alpha, beta)
                beta = min(beta, current_value)

                if current_value == value and depth == 0:
                    self.best_move = move
                if current_value < value:

                    value = current_value
                    beta = min(beta, value)
                    if depth == 0:
                        self.best_move = move

                self.boardgrid = board
                if alpha >= beta:
                    break
            return value

        else:
            value = -Inf
            tiger = Tiger(self.boardgrid,self.tigers_trapped,self.goats_killed)
            for move in tiger.possible_tiger_movess():
                board = self.boardgrid
                tiger.make_move_tiger(move)
                current_value = self.minimax(False, depth + 1, alpha, beta)
                alpha = max(alpha, value)
                if current_value == value and depth == 0:
                    self.best_move = move
                if current_value > value:
                    value = current_value
                    alpha = max(alpha, value)
                    if depth == 0:
                        self.best_move = move
                self.boardgrid = board

                if alpha >= beta:
                    break
            return value