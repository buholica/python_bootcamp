#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

names_list = []
letter_pattern = ""

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()
    for name in names:
        new_name = name.strip("\n")
        names_list.append(new_name)

with open("./Input/Letters/starting_letter.txt") as letter:
    letter_pattern = letter.read()

for name in names_list:
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w") as final_letter:
        new_letter_pattern = letter_pattern.replace("[name]", name)
        final_letter.write(new_letter_pattern)
