# # Note: You get 5 attempts to guess it right
import random
import os
class HangingMan:
    def selMode():
        print("Select Mode: \n 1) Single Player \n 2) Multi player")
        mode = input()
        try:
            if(int(mode) < 1 or int(mode) > 2):
                print('Just select 1 or 2 god dammit')
                return HangingMan.defLevel()
            return int(mode)
        except: 
            print('Just select 1 or 2 god dammit')
            return HangingMan.selMode()
    def defLevel():
        print('Enter Difficulty: \n 1) Easy \n 2) Intermidiate \n 3) Hard')
        level = input()
        try:
            if(int(level) < 1 or int(level) > 3):
                print('Dude, can\'t u read? where tf do u see '+level+' level ????')
                return HangingMan.defLevel()
            return int(level)
        except:
            print('Please just use 1,2 or 3 dumbass')
            return HangingMan.defLevel()

    def checkWord(inp, hint, word):
        count = 0
        s = 'fail'
        bhint = list(hint)
        for w in word:
            # bhint = list(hint)
            if(inp.lower() == w):
                # if(bhint[count] == inp):
                #     s = 'fail'
                    # return {'status':'fail', 'hint':''.join(bhint)}
                bhint[count] = inp.lower()
                s = 'finish' if bhint.count('_') <= 0 else "success"
                # return {'status': 'finish' if bhint.count('_') <= 0 else "success", 'hint':''.join(bhint)}
            count = count+1
        return {'status':s, 'hint':''.join(bhint)}

    def main():    
        mode = HangingMan.selMode()
        level = 0 if mode == 2 else HangingMan.defLevel()
        if(level == 0):
            print('Enter your word:')
        word = "tomato" if level == 1 else "bonfire" if level == 2 else "befuddled" if level == 3 else input().lower()
        os.system('cls')
        if(level == 0):
            if(len(word) == 0):
                HangingMan.main()
            cHint = []
            for w in word:
                cHint.append('_')
            c = 0
            while(c != 2):
                flag = random.randint(0,len(word)-1)
                cHint[flag] = word[flag]
                c += 1
            cHint = "".join(cHint)
        print('#Note: You get 8 attempts to guess it right.')
        hint = '__ma__' if level == 1 else "____i_e" if level == 2 else "b_f______" if level == 3 else cHint
        limit = 0
        status = 0
        life = '00000000'
        print('Life: 8 ('+life+')')
        print(hint)
        print('Enter your guess: ')
        while(limit < 8):
            uin = input()
            chk = HangingMan.checkWord(uin, hint, word)
            if(chk['status'] == 'success'):
                print('~~~~~~~~~~~~ Right Answer ~~~~~~~~~~~')
            elif(chk['status'] == 'finish'):
                status = 1
                break
            else:
                print('******** Wrong Answer ********')
                b = list(life)
                b[len(b)-1] = ''
                life = ''.join(b)
                limit += 1

            hint = chk['hint']
            print('Life: '+str(8 - int(limit))+ '('+life+') \n')
            print(chk['hint'])
            print('Enter your guess: ')
        print('\n\n\n\n\n\n =========================================================\n\n'+chk['hint']+'\n ~*~*~*~*~*~*~*~ You Win ~*~*~*~*~*~*~*~') if status else print('\n\n\n\n\n\n =========================================================\n\n'+word+'\n~*~*~*~*~*~*~ You Loose ~*~*~*~*~*~*~*~*~')
        print('would u like to play again? y/n')
        again = input()
        if(again == 'y'):
            os.system('cls')
            HangingMan.main()
        else:
            exit()


class TicTacToe:
    def move(m,c,turn):
        spot = m-1 if m <= 3 else m if m > 3 and m <=6 else m+1
        cvas = list(c)
        mark = '0' if turn else 'x'
        if(cvas[spot] != '#'):
            return {'status':'error', 'canvas':''.join(cvas)}
        cvas[spot] = mark
        game = TicTacToe.victory(cvas, mark)
        if(game):
            print('~~~~~~~ '+mark+' WINS ~~~~~~~~')
            print(''.join(cvas))
            return {'status':False, 'canvas':''.join(cvas)}
        if((''.join(cvas)).count('#') <= 0):
            print('~~~~~~~~  Stale Mate ~~~~~~~')
            print(''.join(cvas))
            return {'status':False, 'canvas':''.join(cvas)}
        return {'status':True, 'canvas':''.join(cvas)}

    
    def victory(cvas, turn):
        c1 = cvas[0]+cvas[1]+cvas[2]
        c2 = cvas[4]+cvas[5]+cvas[6]
        c3 = cvas[8]+cvas[9]+cvas[10]

        c4 = cvas[0]+cvas[4]+cvas[8]
        c5 = cvas[1]+cvas[5]+cvas[6]
        c6 = cvas[2]+cvas[6]+cvas[10]

        c7 = cvas[0]+cvas[5]+cvas[10]
        c8 = cvas[2]+cvas[5]+cvas[8]

        return True if c1.count(turn) == 3 else True if c2.count(turn) == 3 else True if c3.count(turn) == 3 else True if c4.count(turn) == 3 else True if c5.count(turn) == 3 else True if c6.count(turn) == 3 else True if c7.count(turn) == 3 else True if c8.count(turn) == 3 else   False
    

    def aI(cvas):
        c1 = cvas[0]+cvas[1]+cvas[2]
        c2 = cvas[4]+cvas[5]+cvas[6]
        c3 = cvas[8]+cvas[9]+cvas[10]

        c4 = cvas[0]+cvas[4]+cvas[8]
        c5 = cvas[1]+cvas[5]+cvas[6]
        c6 = cvas[2]+cvas[6]+cvas[10]

        c7 = cvas[0]+cvas[5]+cvas[10]
        c8 = cvas[2]+cvas[5]+cvas[8]
        return {'status':True, 'path':'c1'} if c1.count('0') == 2 else {'status':True, 'path':'c2'} if c2.count('0') == 2 else {'status':True, 'path':'c3'} if c3.count('0') == 2 else {'status':True, 'path':'c4'} if c4.count('0') == 2 else {'status':True, 'path':'c5'} if c5.count('0') == 2 else {'status':True, 'path':'c6'} if c6.count('0') == 2 else {'status':True, 'path':'c7'} if c7.count('0') == 2 else {'status':True, 'path':'c8'} if c8.count('0') == 2 else   {'status':False, 'path':''}


    def cpu(cvas):
        checkTactis = TicTacToe.aI(cvas)
        if(checkTactis['status']):
            print(True)
        else:
            print(False)


    def action(canvas):
        mov = input()
        try:
            mov = int(mov)
            if(mov > 9 or mov < 0):
                os.system('cls')
                print('just enter 1-9 dude')
                print(canvas)
                return TicTacToe.action(canvas)
        except:
            os.system('cls')
            print('just enter 1-9 dude')
            print(canvas)
            return TicTacToe.action(canvas)
        return mov

    def singlePlayer(canvas):
        turn = True
        print(canvas)
        while(True):
            p1move = TicTacToe.action(canvas)
            if(p1move == 0):
                break
            os.system('cls')
            cvs = TicTacToe.move(p1move,canvas,turn)
            canvas = cvs['canvas']
            if(cvs['status'] == False):
                break
            if(cvs['status'] != 'error'):
                turn = False if turn else True
            print(canvas)
        
        print('Would you like to play again? y/n:')
        ask = input()
        if(ask.lower() == 'y'):
            os.system('cls')
            TicTacToe.main()
        exit()

    def multiPlayer(canvas):
        turn = True
        print(canvas)
        while(True):
            p1move = TicTacToe.action(canvas)
            if(p1move == 0):
                break
            os.system('cls')
            cvs = TicTacToe.move(p1move,canvas,turn)
            canvas = cvs['canvas']
            if(cvs['status'] == False):
                break
            if(cvs['status'] != 'error'):
                turn = False if turn else True
            print(canvas)
        
        print('Would you like to play again? y/n:')
        ask = input()
        if(ask.lower() == 'y'):
            os.system('cls')
            TicTacToe.main()
        exit()
        
    def main():
        os.system('cls')
        print('--------- Welcome to my TicTacToe ----------')
        # print('# Note: This is a multiplayer game so 2some is required #')
        print('Choose mode: \n 1) Single Player \n 2) Multiplayer')
        mode = input()
        os.system('cls')
        canvas = '###\n###\n###'
        if(int(mode) == 2):
            print('====== Multiplayer ======')
            TicTacToe.singlePlayer(canvas)
        else:
            print('====== Single Player ======')
            TicTacToe.multiPlayer(canvas)
       

hman = HangingMan
ttt = TicTacToe
print('Which game would you like to play? \n 1) Hanging Man \n 2) Tic Tac Toe')
select = int(input())

ttt.main() if select == 2 else hman.main()
