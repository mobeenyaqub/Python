import random
import hangman_art
import hangman_words

print(hangman_art.logo,'\n\n\n\n')

chosen_word = random.choice(hangman_words.word_list)
used_words = []
blanks = list('_' * len(chosen_word))
x = 0
x = 0
wrong_attempts = 7
check = False

while wrong_attempts > 0:
  guess = input("Guess a letter: ").lower()

  for letter in chosen_word:
      if letter == guess:
          blanks[x] = guess
          x += 1
          check = True
      else:
        x += 1

  if not check and guess not in used_words:
      wrong_attempts -= 1
      print(hangman_art.stages[wrong_attempts])
  if guess in used_words:
    print(f'\n\nLetter  "{guess}"  already used\n\n')
  if guess not in used_words:
     used_words.append(guess)
  if '_' not in blanks:
    break

  print(blanks)
  print(f"\n\nYou have already used : {' '.join(used_words)}\n\n")
  check = False    
  x = 0

if '_' in blanks:
  print(f"\n\nYou lose!. The word was {chosen_word}")
else:
  print('\n\nYou won!. The word is {chosen_word}')