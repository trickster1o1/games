# Note: You get 5 attempts to guess it right

word = "nischal"
print('#Note: You get 8 attempts to guess it right.')
status = 0

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
    return 0

def main():
    hint = 'n__c__l'
    limit = 0
    print(hint)
    print('Enter your guess: ')
    while(limit <8):
        uin = input()
        chk = checkWord(uin, hint)
        if(chk['status'] == 'success'):
            print('~~~~~~~~~~~~ Right Answer ~~~~~~~~~~~')
        elif(chk['status'] == 'finish'):
            print('~*~*~*~*~*~*~*~* you\'ve wone *~*~*~*~*~*~*~*')
            break
        else:
            print('******** Wrong Answer ********')
        limit += 1
        hint = chk['hint']
        print(chk['hint'])
        print('Enter your guess: ')



    
        




main()