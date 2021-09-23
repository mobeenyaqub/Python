import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = int(input("Type 1 to to encrypt, type 2 to decrypt:\n"))
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

text = list(text)
plain_text = []
cipher_text = []


def caesar(text, shift, enc_or_dec):
    i = 0
    position = 0
    message = []
    for letter in text:
      if letter in alphabet:
        for find in alphabet:
            if letter == find:
                if enc_or_dec:
                    position = i + shift
                else:
                    position = i - shift
                if position > 26:
                    position -= 26
                message.append(alphabet[position])
            i += 1  #
        i = 0  #
      else:
        message.append(letter)
    return message

def encrypt(text, shift):
    cipher_text = caesar(text, shift, True)
    print(f'Encrypted message : ', end='')
    for char in cipher_text:
        print(char, end='')
    print('\n\n')

def decrypt(text, shift):
    plain_text = caesar(text, shift, False)
    print(f'Decrypted message : ', end='')
    for char in plain_text:
        print(char, end='')
    print('\n\n')

def start_over(dir):
  if dir == 1:
    encrypt(text, shift)
  elif dir == 2:
    decrypt(text, shift)
  else:
    print('Invalid option selected.')

start_over(direction)

choice = int(input("\n\nPress 1 to start over. Press 2 to exit.\nEnter your choice : "))
    
while choice != 2:
  direction = int(input("\n\nType 1 to to encrypt, type 2 to decrypt:\n"))
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  start_over(direction)
  choice = int(input("\n\nPress 1 to start over. Press any key to exit.\nEnter your choice : "))
else:
  print("\n\nHave a great day.")