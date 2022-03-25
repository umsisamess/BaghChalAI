import random

class Tiger:

    def __init__(self,boardgrid,tigers_trapped,goats_killed):
        self.boardgrid = boardgrid
        self.tigers_trapped = tigers_trapped
        self.goats_killed = goats_killed

    def possible_tiger_movess(self):
        possible_tiger_moves = []
        self.tigers_trapped = 0
        for i in range(5):
            for j in range(5):
                if self.boardgrid[i][j]=='T':
                    flag = 0
                    if i-1>=0:
                        if(self.boardgrid[i-1][j] == '_'):
                            possible_tiger_moves.append([i,j,i-1,j])
                            flag = 1
                    if i+1<5:
                        if(self.boardgrid[i+1][j] == '_'):
                            possible_tiger_moves.append([i,j,i+1,j])
                            flag = 1
                    if j-1>=0:
                        if(self.boardgrid[i][j-1] == '_'):
                            possible_tiger_moves.append([i,j,i,j-1])
                            flag = 1
                    if j+1<5:
                        if(self.boardgrid[i][j+1] == '_'):
                            possible_tiger_moves.append([i,j,i,j+1])
                            flag = 1

                    if i-1>=0 and j-1>=0 and i%2==j%2:
                        if(self.boardgrid[i-1][j-1] == '_'):
                            possible_tiger_moves.append([i,j,i-1,j-1])
                            flag = 1
                    if i-1>=0 and j+1<5 and i%2==j%2:
                        if(self.boardgrid[i-1][j+1] == '_'):
                            possible_tiger_moves.append([i,j,i-1,j+1])
                            flag = 1
                    if i+1<5 and j-1>=0 and i%2==j%2:
                        if(self.boardgrid[i+1][j-1] == '_'):
                            possible_tiger_moves.append([i,j,i+1,j-1])
                            flag = 1
                    if i+1<5 and j+1<5 and i%2==j%2:
                        if(self.boardgrid[i+1][j+1] == '_'):
                            possible_tiger_moves.append([i,j,i+1,j+1])
                            flag = 1

                    if i-2>=0:
                        if(self.boardgrid[i-2][j] == '_' and self.boardgrid[i-1][j]=='G'):
                            possible_tiger_moves.append([i,j,i-2,j])
                            flag = 1
                    if i+2<5:
                        if(self.boardgrid[i+2][j] == '_' and self.boardgrid[i+1][j]=='G'):
                            possible_tiger_moves.append([i,j,i+2,j])
                            flag = 1
                    if j-2>=0:
                        if(self.boardgrid[i][j-2] == '_' and self.boardgrid[i][j-1]=='G'):
                            possible_tiger_moves.append([i,j,i,j-2])
                            flag = 1
                    if j+2<5:
                        if(self.boardgrid[i][j+2] == '_' and self.boardgrid[i][j+1]=='G'):
                            possible_tiger_moves.append([i,j,i,j+2])
                            flag = 1

                    if i-2>=0 and j-2>=0 and i%2==j%2:
                        if(self.boardgrid[i-2][j-2] == '_' and self.boardgrid[i-1][j-1]=='G'):
                            possible_tiger_moves.append([i,j,i-2,j-2])
                            flag = 1
                    if i-2>=0 and j+2<5 and i%2==j%2:
                        if(self.boardgrid[i-2][j+2] == '_' and self.boardgrid[i-1][j+1]=='G'):
                            possible_tiger_moves.append([i,j,i-2,j+2])
                            flag = 1
                    if i+2<5 and j-2>=0 and i%2==j%2:
                        if(self.boardgrid[i+2][j-2] == '_' and self.boardgrid[i+1][j-1]=='G'):
                            possible_tiger_moves.append([i,j,i+2,j-2])
                            flag = 1
                    if i+2<5 and j+2<5 and i%2==j%2:
                        if(self.boardgrid[i+2][j+2] == '_' and self.boardgrid[i+1][j+1]=='G'):
                            possible_tiger_moves.append([i,j,i+2,j+2])  
                            flag = 1

                    if flag==0:
                        self.tigers_trapped += 1 
            
        return possible_tiger_moves

    def select_random(self,pos_mo):
        n = len(pos_mo)
        return pos_mo[random.randint(0,n-1)]

    def make_a_tiger_move(self):
        possible_moves = self.possible_tiger_movess()
        move_to_be_made = self.select_random(possible_moves)
        self.make_move_tiger(move_to_be_made)

    def make_move_tiger(self,move_to_be_made):
        if abs(move_to_be_made[2]-move_to_be_made[0])==2 or abs(move_to_be_made[3]-move_to_be_made[1])==2:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'T'
            self.boardgrid[(move_to_be_made[2]+move_to_be_made[0])//2][(move_to_be_made[3]+move_to_be_made[1])//2] = '_'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'
            self.goats_killed += 1
        else:
            self.boardgrid[move_to_be_made[2]][move_to_be_made[3]] = 'T'
            self.boardgrid[move_to_be_made[0]][move_to_be_made[1]] = '_'
    
    