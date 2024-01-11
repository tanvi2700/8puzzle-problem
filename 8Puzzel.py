class Eight_Puzzle:

    def __init__(self,currstate):
        self.currstate=currstate
        self.g_state= [0,1,2,3,4,5,6,7,8]
        
    def gstate(self,state):
        return state==self.g_state
    
    board= [' ' for x in range(10)]
    def printBoard(self,state):
        print('\n')
        print(' ' + str(state[0]) + ' | ' + str(state[1]) + '   | ' + str(state[2]))
        print('   |     |   ')
        print('-------------')
        print('   |     |   ')
        print(' ' + str(state[3]) + ' | ' + str(state[4]) + '   | ' + str(state[5]))

        print('-------------')
        print('   |     |   ')
        print(' ' + str(state[6]) + ' | ' + str(state[7]) + '   | ' + str(state[8]))
        print('\n')

        
    def up(self,state):
        pos=state.index(0)
        if pos>2:
            state[pos-3],state[pos]=state[pos],state[pos-3]
            self.currstate=state
            self.printBoard(self.currstate)
            print(state,"up")
    def down(self,state):
        pos=state.index(0)
        if pos<6:
            state[pos+3],state[pos]=state[pos],state[pos+3]
            self.currstate=state
            self.printBoard(self.currstate)
            print(state,"down")
    def right(self,state):
        pos=state.index(0)
        if pos%3 != 2 :
            state[pos+1],state[pos]=state[pos],state[pos+1]
            self.currstate=state
            self.printBoard(self.currstate)
            print(state,"right")
    def left(self,state):
        pos=state.index(0)
        if pos%3 != 0 :
            state[pos-1],state[pos]=state[pos],state[pos-1]
            self.currstate=state
            self.printBoard(self.currstate)
    
        
pz=Eight_Puzzle([7,2,4,5,0,6,8,3,1])
pz.gstate(pz.currstate)
pz.printBoard(pz.currstate)
pz.up(pz.currstate)
pz.down(pz.currstate)
pz.right(pz.currstate)
pz.left(pz.currstate)
