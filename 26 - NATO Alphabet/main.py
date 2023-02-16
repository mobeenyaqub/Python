import pandas

data_file = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_data = {row.letter: row.code for (index, row) in data_file.iterrows()}
print(nato_data)

word = "hello".upper()

break_word = [nato_data[letter] for letter in word]
print(break_word)
