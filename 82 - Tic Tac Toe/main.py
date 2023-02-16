game = [0, 1, 2, 3, 4, 5, 6, 7, 8]
marked = []
turn = 0


def board():
    print(f'{game[0]} | {game[1]} | {game[2]}')
    print('---------')
    print(f'{game[3]} | {game[4]} | {game[5]}')
    print('---------')
    print(f'{game[6]} | {game[7]} | {game[8]}')


def check_result():
    global game, turn

    result = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [1, 4, 7], [0, 3, 6], [2, 5, 8]]
    check = False

    if len(marked) > 2:
        for character in ['X', 'O']:
            for i in result:
                for j in i:
                    if game[j] == character:
                        check = True
                    else:
                        check = False
                        break
                if check:
                    if character == 'X':
                        print(f"Player 1 has won!!")
                    else:
                        print(f"Player 2 has won!!")
                    return False
                elif len(marked) == 9:
                    print("It's a draw!")

    return True


def add_to_list(mark):
    global turn, marked
    if turn % 2 == 0:
        game[mark] = 'X'
    else:
        game[mark] = 'O'

    marked.append(mark)
    turn += 1


while check_result():
    position = int(input("\n\nEnter position: "))
    while position > 8 or position < 0 or position in marked:
        position = int(input("\n\nRe-enter position: "))

    add_to_list(position)
    board()
