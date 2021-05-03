rand_num = None
position = None
counter = 0
win = False
table = [[1,2,3],[4,5,6],[7,8,9]]
repetition_check = []

def RandomPlayerSelector():
     from random import randint
     rand_num = randint(1,2)
    
     if rand_num % 2 != 0:
         print("\n\t\t\t\tIt's player 1 turn")
     else:
        print("\n\t\t\t\tIt's player 2 turn")
     
     return rand_num

def GameBoard(table):
   
    print(f'\n\n')
    for y in table:
        print(f'\t',end="")
        for i in y:
            print(f'{i}   |   ',end=" ")
            
        print(f'\n\t',end="")
        print("_______________________")
        print(f'\n')

    print(f'\n\n')


def RefreshGameBoard(table):
    table.clear()
    table = [[1,2,3],[4,5,6],[7,8,9]]
    return table

def UpdateGameBoard(rand_num,position):
    global table  
    count1 = 0
    count2 = 0
    for y in table:
        for i in y:
            if position == table[count1][count2]:
                if rand_num % 2 != 0:
                    table[count1][count2] = 'X'
                    break
                elif rand_num % 2 == 0:
                      table[count1][count2] = 'O'
                      break
                else:
                    continue
            count2+=1
        count1+=1
        count2 = 0

    rand_num+=1
    return rand_num


def UserInput(rand_num,counter, repetition_check):
    if rand_num % 2 != 0:
        val = 'X'
    else:
        val = 'O'

    position = int(input(f"Enter a position number to add {val} : "))

    while position not in range(1,10) or position in repetition_check:
        if position in repetition_check:
            print("\nPosition already taken")
        print("\nInvalid position chosen. Try again\n")
        position = int(input(f"Enter a position to add {val} : "))


    repetition_check.append(position)
    counter+=1
    return position,counter, repetition_check


def WinnerCheck():
    if table[0][0] == 'X' and table[0][1] == 'X' and table[0][2] == 'X':
        return 1
    elif table[1][0] == 'X' and table[1][1] == 'X' and table[1][2] == 'X':
        return 1
    elif table[2][0] == 'X' and table[2][1] == 'X' and table[2][2] == 'X':
        return 1
    elif table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        return 1
    elif table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        return 1
    elif table[0][1] == 'X' and table[1][1] == 'X' and table[2][1] == 'X':
        return 1
    elif table[0][0] == 'X' and table[1][0] == 'X' and table[2][0] == 'X':
        return 1
    elif table[0][2] == 'X' and table[1][2] == 'X' and table[2][2] == 'X':
        return 1
    elif table[0][0] == 'O' and table[0][1] == 'O' and table[0][2] == 'O':
        return 2
    elif table[1][0] == 'O' and table[1][1] == 'O' and table[1][2] == 'O':
        return 2
    elif table[2][0] == 'O' and table[2][1] == 'O' and table[2][2] == 'O':
        return 2
    elif table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        return 2
    elif table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O':
        return 2
    elif table[0][1] == 'O' and table[1][1] == 'O' and table[2][1] == 'O':
        return 2
    elif table[0][0] == 'O' and table[1][0] == 'O' and table[2][0] == 'O':
        return 2
    elif table[0][2] == 'O' and table[1][2] == 'O' and table[2][2] == 'O':
        return 2
    else:
        return False
       

def InGame(table):

   global rand_num
   global position 
   global counter
   global repetition_check

   GameBoard(table)

   while counter != 9:
      position,counter,repetition_check = UserInput(rand_num,counter, repetition_check)
      rand_num = UpdateGameBoard(rand_num,position)
      GameBoard(table)

      check = WinnerCheck()

      if check == 1:
          print("\n\n\t\t\t******Player 1 Win******\n\n")
          break
      if check == 2:
           print("\n\n\t\t\t******Player 2 Win******\n\n")
           break

   check = WinnerCheck()
   if check == False:
    print("\nIt's a draw\n")

# Calling Functions

enter_key = input("Press any key to randomly select between player 1 or 2, to start with : ")

rand_num = RandomPlayerSelector()

print("\n\t\t\t\t   Player 1 : X\n\t\t\t\t   Player 2 : O\n\n")

InGame(table)