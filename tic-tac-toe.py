import os
import time
import random
from assets.Board import board

def metaGameTrackerPrint(meta):
        print('\n \t\t\t'+meta[1]+' | '+meta[2]+' | '+meta[3]+' \n \t\t\t--+---+-- \n \t\t\t'+meta[4]+' | '+meta[5]+' | '+meta[6]+' \n \t\t\t--+---+-- \n \t\t\t'+meta[7]+' | '+meta[8]+' | '+meta[9]+' \n\n')

def check_Instance_OR_Index(input):
    if input.isdigit() == False or int(input) < 1 or int(input) > 9:
        return False
    return True

def metaGameCounter(metaGame):
    counter = 0
    for c in range(1,10):
        if metaGame[c] == 'X' or metaGame[c] == 'O':
            counter+=1
    return counter

def playableInstances(metaGame,metaTracker):
    res = []
    for i in metaTracker:
        if metaTracker[i].isdigit() and (metaGame.game[i].getMove() == 'O' or metaGame.game[i].getMove() == ' '):
            res.append(i)
    return res

def playableIndex(metaGame):
    res = []
    for i in metaGame:
        if metaGame[i] == ' ':
            res.append(i)
    return res

def metaGameValidator(metaGame,counter,metaTracker):
    if counter > 2 :
        if metaGame[1] == metaGame[2] == metaGame[3] != ' ':
            metaGame = metaGame[1]
        elif metaGame[4] == metaGame[5] == metaGame[6] != ' ':
            metaGame = metaGame[4]
        elif metaGame[7] == metaGame[8] == metaGame[9] != ' ':
            metaGame = metaGame[7]
        elif metaGame[1] == metaGame[4] == metaGame[7] != ' ':
            metaGame = metaGame[1]
        elif metaGame[2] == metaGame[5] == metaGame[8] != ' ':
            metaGame = metaGame[2]
        elif metaGame[3] == metaGame[6] == metaGame[9] != ' ':
            metaGame = metaGame[3]
        elif metaGame[1] == metaGame[5] == metaGame[9] != ' ':
            metaGame = metaGame[1]
        elif metaGame[3] == metaGame[5] == metaGame[7] != ' ':
            metaGame = metaGame[3]

        if metaGame == 'X' or metaGame == 'O':
            return metaGame,False,metaTracker

        if counter == 9 and (metaGame != 'X' or metaGame != 'O'):
            metaGame = board()
            metaTracker = { 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',}
            print('No winner for the metaGame!!!! \nRestarting metaGame')
            time.sleep(4)
            for inst in range(1,10):                                                            #creates a board object inside each metaGame instances 
                metaGame.game[inst] = board()
            return metaGame.game,True,metaTracker
        return metaGame,False,metaTracker
    
def computer(rand):
    return random.choice(rand)

def main():
    print('\n\t\t\t\tTic-Tac-Toe \U0001F603\n')
    print('Game Instructions:')
    print('\n→ This is a variation of the classic game of tic-tac-toe, where 2 players take turns putting X\'s and O\'s in a 3x3 grid, and the first to get 3 in a row wins.' +
          '\n→ In this version, there are 9 instances of the game being played simultaneously. Each turn, a player may make a single move in any one of the 9 game instances.' +
          '\n→ The game instances are themselves arranged in a 3x3 grid, constituting a meta-game. '
          '\n→ Each time a player wins a game instance, they take the corresponding square in the meta-game.' +
          '\n→ If a game instance results in a tie, that game instance is replaced with a fresh instance with no moves played. The game is over when a player wins the meta-game.\n\n')
    metaGame = board()         #Stores all the 9 games
    metaTracker = { 1:'1', 2:'2', 3:'3', 4:'4', 5:'5', 6:'6', 7:'7', 8:'8', 9:'9',}     #Tracks the instances played
    playerCount = 0   
    for inst in range(1,10):                                                            #creates a board object inside each metaGame instances 
        metaGame.game[inst] = board()

    while True:
        comp = input('Select the number of players playing(One player - 1, Two players - 2):')
        if comp.isdigit() and int(comp) in {1,2}:
            playerCount = int(comp)
            break
        print('Maximium number of players is 2, please select between 1 & 2 \U0001F611\n')
        time.sleep(1.7)
    
    while True:
        os.system('cls')
        for player in ['X','O']:

            if player == 'X':
                print('Player 1 (X)')
            else:
                if playerCount == 1:
                    print('Player 2 - Computer (O)')
                else:
                    print('Player 2 (O)')
            metaGameTrackerPrint(metaTracker)
            if player == 'X' or (player == 'O' and playerCount == 2):
                while True:
                    instance = input('Please select the instance you want to play(1,2,3.....,9):')
                    if check_Instance_OR_Index(instance) == False:
                        print('Wrong Instance Entry!!!!! Try Again \U0001F611\n')
                        time.sleep(.5)
                        continue
                    elif metaTracker[int(instance)] != instance:
                        print('The instance was already played..... Play a diffirent instance\n')
                        time.sleep(.5)
                        continue
                    elif metaGame.game[int(instance)].getMove() != ' ' and metaGame.game[int(instance)].getMove() != player:
                        print('It is not your move at that instance!!! Play a different instance \U0001F611\n')
                        time.sleep(.5)
                        continue
                    instance = int(instance)
                    break
            else:
                instance = computer(playableInstances(metaGame,metaTracker))
                print('Please select the instance you want to play(1,2,3.....,9): ' + str(instance))
                time.sleep(3)
            os.system('cls')

            if player == 'X':
                print('Player 1 (X)')
            else:
                if playerCount == 1:
                    print('Player 2 - Computer (O)')
                else:
                    print('Player 2 (O)')

            #Records the move of the player 
            while player == 'X' or (player == 'O' and playerCount == 2):
                print('\n \t\t   Instance being played:'+str(instance))
                metaGame.game[instance].printBoard()
                print('\n\n\t\t\t' + ' 1 | 2 | 3 \n\t\t\t --+---+-- \n\t\t\t 4 | 5 | 6 \n\t\t\t --+---+-- \n\t\t\t 7 | 8 | 9\n')
                play = input('Select the index you want to play from the options(eq:1,2,3....9):')
                if check_Instance_OR_Index(play) == True and metaGame.game[instance].playCheck(int(play)) == True:
                    play = int(play)
                    break
                print('\nWrong Index Entry!!!!!  Please try again. \U0001F611\n')
                time.sleep(2)
                os.system('cls')

            #Records the move of the computer(if computer is playing)
            if player == 'O' and playerCount == 1:
                metaGame.game[instance].printBoard()
                print('\n\n\t\t\t' + ' 1 | 2 | 3 \n\t\t\t --+---+-- \n\t\t\t 4 | 5 | 6 \n\t\t\t --+---+-- \n\t\t\t 7 | 8 | 9\n')
                play = computer(playableIndex(metaGame.game[instance].game))
                print('Select the index you want to play from the options(eq:1,2,3....9): '+ str(play))
                time.sleep(4)

            metaGame.game[instance].playGame(player,play)
            status = metaGame.game[instance].validator()
            os.system('cls')
            if status == 'X' or status == 'O':
                print('\n\t\t\t   ' + status + ' Won')
                metaGame.game[instance].printBoard()
                metaGame.game[instance],metaTracker[instance] = status,status
                time.sleep(1)
                os.system('cls')
                
            else:
                print('\n\n\t\t Your move has been recorded!!!!\n')
                if status == 'reset': 
                    print('\t\t Game Completed -- No Winner -- Game Resetting... \U0001F972\U0001F972')
                    time.sleep(3)
            
            if status != 'X' and status != 'O': metaGame.game[instance].printBoard()
            
            if player == 'O' and playerCount == 1 : time.sleep(3)
            else: time.sleep(1.5)

            counter = metaGameCounter(metaGame.game)
            status = False
            if counter > 2:
                metaGame.game,status,metaTracker = metaGameValidator(metaGame.game,counter,metaTracker)
                if metaGame.game == 'X' or metaGame.game == 'O':
                    print('\n\n\t\t     '+metaGame.game + ' Won the game')
                    metaGameTrackerPrint(metaTracker)
                    print('\t\t     Congratulations \U0001F44F\U0001F44F\U0001F44F')
                    time.sleep(5)
                    return
            os.system('cls')
            if status:
                break
        

    
if __name__ == '__main__':
    main()