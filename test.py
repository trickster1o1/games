# Note: You get 5 attempts to guess it right

word = "nischal"
print('#Note: You get 8 attempts to guess it right.')

def checkWord(inp, hint):
    count = 0
    for w in word:
        bhint = list(hint)
        if(inp == w):
            if(bhint[count] == inp):
                return {'status':'fail', 'hint':''.join(bhint)}
            bhint[count] = inp
            return {'status': 'finish' if bhint.count('_') <= 0 else "success", 'hint':''.join(bhint)}
        count = count+1
    return {'status':'fail', 'hint':''.join(bhint)}

def main():
    hint = 'n__c__l'
    limit = 0
    status = 0
    life = '00000000'
    print('Life: 8 ('+life+')')
    print(hint)
    print('Enter your guess: ')
    while(limit < 8):
        uin = input()
        chk = checkWord(uin, hint)
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
    print('~*~*~*~*~*~*~*~ You Win ~*~*~*~*~*~*~*~') if status else print('~*~*~*~*~*~*~ You Loose ~*~*~*~*~*~*~*~*~')
    print('Press Enter key to exit')
    input()



main()