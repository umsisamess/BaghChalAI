import random

class Goat:
    def __init__(self,boardgrid,goats_to_be_placed):
        self.boardgrid = boardgrid
        self.goats_to_be_placed = goats_to_be_placed

    def make_a_goat_move(self):
        possible_moves = self.possible_goat_movess()
        move_to_be_made = self.select_random(possible_moves)
        self.make_move_goat(move_to_be_made)

    def make_move_goat(self,move_to_be_made):
        if move_to_be_made[0] == -1:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'G'
            self.goats_to_be_placed -= 1
        else:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'G'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'

    def select_random(self,pos_mo):
        n = len(pos_mo)
        return pos_mo[random.randint(0,n-1)]

    def possible_goat_movess(self):
        possible_goat_moves = []
        if self.goats_to_be_placed > 0:
            for i in range(5):
                for j in range(5):
                    if self.boardgrid[i][j]=='_':
                        possible_goat_moves.append([-1,-1,i,j])
        else:
            for i in range(5):
                for j in range(5):
                    if self.boardgrid[i][j]=='G':
                        if i-1>=0:
                            if(self.boardgrid[i-1][j] == '_'):
                                possible_goat_moves.append([i,j,i-1,j])
                        if i+1<5:
                            if(self.boardgrid[i+1][j] == '_'):
                                possible_goat_moves.append([i,j,i+1,j])
                        if j-1>=0:
                            if(self.boardgrid[i][j-1] == '_'):
                                possible_goat_moves.append([i,j,i,j-1])
                        if j+1<5:
                            if(self.boardgrid[i][j+1] == '_'):
                                possible_goat_moves.append([i,j,i,j+1])

                        if i-1>=0 and j-1>=0 and i%2==j%2:
                            if(self.boardgrid[i-1][j-1] == '_'):
                                possible_goat_moves.append([i,j,i-1,j-1])
                        if i-1>=0 and j+1<5 and i%2==j%2:
                            if(self.boardgrid[i-1][j+1] == '_'):
                                possible_goat_moves.append([i,j,i-1,j+1])
                        if i+1<5 and j-1>=0 and i%2==j%2:
                            if(self.boardgrid[i+1][j-1] == '_'):
                                possible_goat_moves.append([i,j,i+1,j-1])
                        if i+1<5 and j+1<5 and i%2==j%2:
                            if(self.boardgrid[i-1][j-1] == '_'):
                                possible_goat_moves.append([i,j,i+1,j+1])
        return possible_goat_moves