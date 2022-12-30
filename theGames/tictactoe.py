import random
import os

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


    def aiMove(cvas, checkTactis):
            if(checkTactis['path'] == 'c1'):
                return TicTacToe.move(1 if cvas[0] == '#' else 2 if cvas[1] == '#' else 3, cvas, False)
            elif(checkTactis['path'] == 'c2'):
                return TicTacToe.move(4 if cvas[4] == '#' else 5 if cvas[5] == '#' else 6, cvas, False)
            elif(checkTactis['path'] == 'c3'):
                return TicTacToe.move(7 if cvas[8] == '#' else 8 if cvas[9] == '#' else 9, cvas, False)
            elif(checkTactis['path'] == 'c4'):
                return TicTacToe.move(1 if cvas[0] == '#' else 4 if cvas[4] == '#' else 7, cvas, False)
            elif(checkTactis['path'] == 'c5'):
                return TicTacToe.move(2 if cvas[1] == '#' else 5 if cvas[5] == '#' else 8, cvas, False)
            elif(checkTactis['path'] == 'c6'):
                return TicTacToe.move(3 if cvas[2] == '#' else 6 if cvas[6] == '#' else 9, cvas, False)
            elif(checkTactis['path'] == 'c7'):
                return TicTacToe.move(1 if cvas[0] == '#' else 5 if cvas[5] == '#' else 9, cvas, False)
            else:
                return TicTacToe.move(3 if cvas[2] == '#' else 5 if cvas[5] == '#' else 7, cvas, False)
    
    def cpu(cvas):
        checkTactis = TicTacToe.aI(cvas)
        ko = TicTacToe.aiKiller(cvas)
        if(ko['status']):
            return TicTacToe.aiMove(cvas, ko)
        if(checkTactis['status']):
            return TicTacToe.aiMove(cvas,checkTactis)
        else:
            if(cvas[5] == '#'):
                return TicTacToe.move(5, cvas, False)
            elif(cvas[0] == '#'):
                return TicTacToe.move(1, cvas, False)
            else:
                check = TicTacToe.move(random.randint(1,9), cvas, False)
                while(check['status'] == 'error'):
                    numb = random.randint(1,9)
                    check = TicTacToe.move(numb, cvas, False)
                return check


    def victory(cvas, turn):
        c1 = cvas[0]+cvas[1]+cvas[2]
        c2 = cvas[4]+cvas[5]+cvas[6]
        c3 = cvas[8]+cvas[9]+cvas[10]

        c4 = cvas[0]+cvas[4]+cvas[8]
        c5 = cvas[1]+cvas[5]+cvas[9]
        c6 = cvas[2]+cvas[6]+cvas[10]

        c7 = cvas[0]+cvas[5]+cvas[10]
        c8 = cvas[2]+cvas[5]+cvas[8]

        return True if c1.count(turn) == 3 else True if c2.count(turn) == 3 else True if c3.count(turn) == 3 else True if c4.count(turn) == 3 else True if c5.count(turn) == 3 else True if c6.count(turn) == 3 else True if c7.count(turn) == 3 else True if c8.count(turn) == 3 else   False
    

    def aI(cvas):
        c1 = cvas[0]+cvas[1]+cvas[2]
        c2 = cvas[4]+cvas[5]+cvas[6]
        c3 = cvas[8]+cvas[9]+cvas[10]

        c4 = cvas[0]+cvas[4]+cvas[8]
        c5 = cvas[1]+cvas[5]+cvas[9]
        c6 = cvas[2]+cvas[6]+cvas[10]

        c7 = cvas[0]+cvas[5]+cvas[10]
        c8 = cvas[2]+cvas[5]+cvas[8]
        return {'status':True, 'path':'c1'} if c1.count('0') == 2 and c1.count('x') <= 0 else {'status':True, 'path':'c2'} if c2.count('0') == 2 and  c2.count('x') <= 0 else {'status':True, 'path':'c3'} if c3.count('0') == 2 and  c3.count('x') <= 0 else {'status':True, 'path':'c4'} if c4.count('0') == 2 and  c4.count('x') <= 0 else {'status':True, 'path':'c5'} if c5.count('0') == 2 and  c5.count('x') <= 0 else {'status':True, 'path':'c6'} if c6.count('0') == 2 and  c6.count('x') <= 0 else {'status':True, 'path':'c7'} if c7.count('0') == 2 and c7.count('x') <= 0 else {'status':True, 'path':'c8'} if c8.count('0') == 2 and  c8.count('x') <= 0 else   {'status':False, 'path':''}

    def aiKiller(cvas):
        c1 = cvas[0]+cvas[1]+cvas[2]
        c2 = cvas[4]+cvas[5]+cvas[6]
        c3 = cvas[8]+cvas[9]+cvas[10]

        c4 = cvas[0]+cvas[4]+cvas[8]
        c5 = cvas[1]+cvas[5]+cvas[9]
        c6 = cvas[2]+cvas[6]+cvas[10]

        c7 = cvas[0]+cvas[5]+cvas[10]
        c8 = cvas[2]+cvas[5]+cvas[8]

        return {'status':True, 'path':'c1'} if c1.count("x") == 2 and c1.count("0") <= 0 else {'status':True, 'path':'c2'} if c2.count("x") == 2 and  c2.count("0") <= 0 else {'status':True, 'path':'c3'} if c3.count("x") == 2 and  c3.count("0") <= 0 else {'status':True, 'path':'c4'} if c4.count("x") == 2 and  c4.count("0") <= 0 else {'status':True, 'path':'c5'} if c5.count("x") == 2 and  c5.count("0") <= 0 else {'status':True, 'path':'c6'} if c6.count("x") == 2 and  c6.count("0") <= 0 else {'status':True, 'path':'c7'} if c7.count("x") == 2 and c7.count("0") <= 0 else {'status':True, 'path':'c8'} if c8.count("x") == 2 and  c8.count("0") <= 0 else   {'status':False, 'path':''}


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

    def singlePlayer(canvas):
        turn = True
        print(canvas)
        while(True):
            p1move = TicTacToe.action(canvas) if turn else 1
            if(p1move == 0):
                break
            os.system('cls')
            cvs = TicTacToe.move(p1move,canvas,turn) if turn else TicTacToe.cpu(canvas)
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
            TicTacToe.multiPlayer(canvas)
        else:
            print('====== Single Player ======')
            TicTacToe.singlePlayer(canvas)
       