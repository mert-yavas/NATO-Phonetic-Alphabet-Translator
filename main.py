# Import the pandas library to read CSV data
import pandas

# Read the NATO phonetic alphabet data from a CSV file into a dictionary
data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    # Get user input for a word and convert it to uppercase
    user_input = input("Enter a word= ").upper()
    try:
        # Create a list of NATO phonetic alphabet codes for each letter in the user's input
        nato_phonetic_type = [phonetic_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_phonetic()
    else:
        # Print the list of NATO phonetic alphabet codes
        print(nato_phonetic_type)


generate_phonetic()
