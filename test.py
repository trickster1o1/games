# Note: You get 5 attempts to guess it right

class HangingMan:
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
            if(inp == w):
                # if(bhint[count] == inp):
                #     s = 'fail'
                    # return {'status':'fail', 'hint':''.join(bhint)}
                bhint[count] = inp
                s = 'finish' if bhint.count('_') <= 0 else "success"
                # return {'status': 'finish' if bhint.count('_') <= 0 else "success", 'hint':''.join(bhint)}
            count = count+1
        return {'status':s, 'hint':''.join(bhint)}

    def main():    
        level = HangingMan.defLevel()
        word = "tomato" if level == 1 else "bonfire" if level == 2 else "befuddled" 
        print('#Note: You get 8 attempts to guess it right.')
        hint = '__ma__' if level == 1 else "____i_e" if level == 2 else "b_f______"
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
            print('Life: '+str(8 - int(limit))+ '('+life+')')
            print(chk['hint'])
            print('Enter your guess: ')
        print(chk['hint']+'\n ~*~*~*~*~*~*~*~ You Win ~*~*~*~*~*~*~*~') if status else print('~*~*~*~*~*~*~ You Loose ~*~*~*~*~*~*~*~*~')
        print('would u like to play again? y/n')
        again = input()
        if(again == 'y'):
            HangingMan.main()
        else:
            exit()


hman = HangingMan
hman.main()