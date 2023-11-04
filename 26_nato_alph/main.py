import pandas

# Creating a dictionary from csv_file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter the word: ")
word_list = [data_dict[letter] for letter in user_word.upper()]

#word_list = []
# for letter in user_word.upper():
#     for key in data_dict:
#         if letter == key:
#             word_list.append(data_dict[key])

print(word_list)