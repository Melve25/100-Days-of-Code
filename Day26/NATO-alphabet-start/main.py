import pandas


nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}
user_input = input("Enter a word: ")
code_words_list = [nato_data_dict[letter] for letter in user_input.upper()]

print(code_words_list)

