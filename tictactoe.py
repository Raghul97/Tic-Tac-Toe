
print('Welcome to the tictac toe game!!!')
cond = True
while cond:
    player1 = input('Enter the symbol of player 1 (x or o): ')
    if player1 in 'xo':
        cond = False
    else:
        print('Enter a valid symbol: ')
        cond = True

if player1 == 'x':
    player2 = 'o'
else:
    player2 = 'X'

print(f'Player one has choosen: {player1}')
print(f'Player two has choosen: {player2}')

print('Let the Fun begins!!!\n')

numb = [7, 8, 9, 4, 5, 6, 1, 2, 3]
ind = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
mark = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
emp = []
play1 = []
play2 = []
game = True


def clear_screen():
    import os
    os.system('cls')


def myboard(val):
    clear_screen()
    if val != 11:
        pos = numb.index(val)

        if pos < 3:
            ind[0][pos] = val
        elif pos < 6:
            pos = pos - 3
            ind[1][pos] = val
        else:
            pos = pos - 6
            ind[2][pos] = val
    else:
        return True

    for i in range(3):
        for j in range(3):
            if ind[i][j] in play1:
                mark[i][j] = player1
                print(mark[i][j], end=" ")
            elif ind[i][j] in play2:
                mark[i][j] = player2
                print(mark[i][j], end=" ")
            else:
                print(' ', end=" ")
            if j < 2:
                print('|', end=" ")
        if i < 2:
            print('\n----------')

    play = check()
    return play


def newgame():
    global game, numb, ind, mark, emp, play1, play2
    new = True
    while new:
        res = input('Do you like to play again?(y or n): ')
        if res not in 'yn':
            print('Enter a valid option yes or no: ')
            new = True
        else:
            if res == 'y':
                game = True
                print('Here we go!!!')
                print('Welcome to the tictac toe game!!!')
                cond = True
                while cond:
                    player1 = input('Enter the symbol of player 1 (x or o): ')
                    if player1 in 'xo':
                        cond = False
                    else:
                        print('Enter a valid symbol: ')
                        cond = True

                if player1 == 'x':
                    player2 = 'o'
                else:
                    player2 = 'X'

                print(f'Player one has choosen: {player1}')
                print(f'Player two has choosen: {player2}')

                print('Let the Fun begins!!!\n')
                new = False
                numb = [7, 8, 9, 4, 5, 6, 1, 2, 3]
                ind = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                mark = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
                emp = []
                play1 = []
                play2 = []
                game = True

            else:
                print('Thank you, Hope we meet again!')
                game = False
                new = False


while game:

    def playerone():
        cond = True
        while cond:
            choosen = input('\nPlayer one choose the value on board from 1 to 9: ')
            try:
                choosen = int(choosen)
            except:
                print('Choose a valid option from 1 to 9')
                continue
            if choosen not in emp:
                if choosen in numb:
                    emp.append(choosen)
                    play1.append(choosen)
                    cond = False
                    play = myboard(choosen)
                    if not play:
                        newgame()
                        break
                    playertwo()
                else:
                    print('Choose a valid option from 1 to 9')
                    cond = True
            else:
                print('Already found, Kindly select another value')
                cond = True


    def playertwo():
        cond2 = True
        while cond2:
            choosen1 = input('\nPlayer two choose the value on board from 1 to 9: ')
            try:
                choosen1 = int(choosen1)
            except:
                print('Choose a valid option from 1 to 9')
                continue
            if choosen1 not in emp:
                if choosen1 in numb:
                    emp.append(choosen1)
                    play2.append(choosen1)
                    cond2 = False
                    play = myboard(choosen1)
                    if not play:
                        newgame()
                        break
                    playerone()
                else:
                    print('Choose a valid option from 1 to 9')
                    cond2 = True
            else:
                print('Already found, Kindly select another value')
                cond2 = True


    def check():
        print('\n')
        if mark[0][0] == mark[0][1] == mark[0][2] == player1:
            print('player 1 wins!!')
            return False
        elif mark[1][0] == mark[1][1] == mark[1][2] == player1:
            print('player 1 wins!!')
            return False
        elif mark[2][0] == mark[2][1] == mark[2][2] == player1:
            print('player 1 wins!!')
            return False
        elif mark[0][0] == mark[1][0] == mark[2][0] == player1:
            print('player 1 wins!!')
            return False
        elif mark[0][1] == mark[1][1] == mark[2][1] == player1:
            print('player 1 wins!!')
            return False
        elif mark[0][2] == mark[1][2] == mark[2][2] == player1:
            print('player 1 wins!!')
            return False
        elif mark[0][0] == mark[1][1] == mark[2][2] == player1:
            print('player 1 wins!!')
            return False
        elif mark[0][2] == mark[1][1] == mark[2][0] == player1:
            print('player 1 wins!!')
            return False
        elif mark[0][0] == mark[0][1] == mark[0][2] == player2:
            print('player 2 wins!!')
            return False
        elif mark[1][0] == mark[1][1] == mark[1][2] == player2:
            print('player 2 wins!!')
            return False
        elif mark[2][0] == mark[2][1] == mark[2][2] == player2:
            print('player 2 wins!!')
            return False
        elif mark[0][0] == mark[1][0] == mark[2][0] == player2:
            print('player 2 wins!!')
            return False
        elif mark[0][1] == mark[1][1] == mark[2][1] == player2:
            print('player 2 wins!!')
            return False
        elif mark[0][2] == mark[1][2] == mark[2][2] == player2:
            print('player 2 wins!!')
            return False
        elif mark[0][0] == mark[1][1] == mark[2][2] == player2:
            print('player 2 wins!!')
            return False
        elif mark[0][2] == mark[1][1] == mark[2][0] == player2:
            print('player 2 wins!!')
            return False
        else:
            if len(emp) == len(numb):
                print('Match Draw')
                return False
            else:
                return True





    playerone()








