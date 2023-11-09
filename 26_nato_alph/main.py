import pandas

# Creating a dictionary from csv_file
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


# Create a list of the phonetic code words from a word that the user inputs.
def generate_nato():
    user_word = input("Enter the word: ")
    try:
        word_list = [data_dict[letter] for letter in user_word.upper()]
    except KeyError:
        print("Sorry, only letters in the alphabet, please.")
        generate_nato()
    else:
        print(word_list)


generate_nato()