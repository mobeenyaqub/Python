alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

direction = int(input("Type '1' to encrypt, type '2' to decrypt:\n"))
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def encrypt(text, shift):
    msg = ""
    for letter in text:
        msg += alphabet[(alphabet.index(letter) + shift) % 26]
    return msg


def decrypt(text, shift):
    msg = ""
    for letter in text:
        msg += alphabet[(alphabet.index(letter) - shift) % 26]
    return msg


if direction == 1:
    print(f"Encrypted message: {encrypt(text,shift)}")
else:
    print(f"Decrypted message: {decrypt(text,shift)}")
