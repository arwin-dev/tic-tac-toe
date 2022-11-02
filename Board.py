class board:
    def __init__(self):
        self.game = {
            1:' ', 2:' ', 3:' ',
            4:' ', 5:' ', 6:' ',
            7:' ', 8:' ', 9:' ',
        }
        self.size = 1
        self.turn = ' '
        self.result = None

    def playGame(self,play,index):
        if play == 'X' and (self.turn == 'X' or self.turn == ' '):
            self.game[index] = 'X'
            self.turn = 'O'
        else:
            self.game[index] = 'O'
            self.turn = 'X'
        self.size += 1
        

    def reset(self):
        self.game = {
            1:' ', 2:' ', 3:' ',
            4:' ', 5:' ', 6:' ',
            7:' ', 8:' ', 9:' ',
        }
        self.size = 1
        self.turn = ' '
        return 'reset'

    def getMove(self):
        return self.turn

    def lenght(self):
        return self.size

    def print(self):
        print(self.game)

    def validator(self):
        
        if self.size > 4:
            if self.game[1] == self.game[2] == self.game[3] != ' ':
                self.result = self.game[1]
            elif self.game[4] == self.game[5] == self.game[6] != ' ':
                self.result = self.game[4]
            elif self.game[7] == self.game[8] == self.game[9] != ' ':
                self.result = self.game[7]
            elif self.game[1] == self.game[4] == self.game[7] != ' ':
                self.result = self.game[1]
            elif self.game[2] == self.game[5] == self.game[8] != ' ':
                self.result = self.game[2]
            elif self.game[3] == self.game[6] == self.game[9] != ' ':
                self.result = self.game[3]
            elif self.game[1] == self.game[5] == self.game[9] != ' ':
                self.result = self.game[1]
            elif self.game[3] == self.game[5] == self.game[7] != ' ':
                self.result = self.game[3]

            if self.result =='X' or self.result == 'O':
                return self.result
            
            if self.size == 10 and (self.reset != 'X' or self.reset != 'O'):
                return self.reset()
            

    def printBoard(self):
        print(      '\n\t\t\t' +
                    self.game[1] + ' | ' + self.game[2] + ' | ' +self.game[3] + '\n\t\t\t' +
                        '--+' + '---+' + '---  '                                + '\n\t\t\t' +  
                    self.game[4] + ' | ' + self.game[5] + ' | ' +self.game[6] + '\n\t\t\t' +
                        '--+' + '---+' + '---  '                                + '\n\t\t\t' +  
                    self.game[7] + ' | ' + self.game[8] + ' | ' +self.game[9] + '\n\t\t\t' 
            )

    def playCheck(self,index):
        if self.game[index] != ' ':
            return False
        return True