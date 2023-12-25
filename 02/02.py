# Day 02
# Import packages
import re


# Define functions
def print_line(print_chars="-", repetition=100):
    """Prints an amount of strings in a row.
       Args:
           print_chars (str): The string to print repeatedly.
           repetition (int): The amount of times the string is printed.
       Returns:
           None
    """
    print(print_chars * repetition)
    return


# Global variables
cube_dict = {"red": 12,
             "green": 13,
             "blue": 14}

# Read the input file
day = "02"
input_file = open(f"{day}/input_{day}.txt")
input_list = input_file.read().splitlines()

# Part 01: Calculate total score, summing the game numbers of possible combinations
total_score = 0
# Go through each input line
for game in input_list:
    # Extract the game number as int and rest of text as to search in from input
    extraction = re.match(r"^Game\s(\d+):\s(.*)$", game)
    score = int(extraction[1])
    search_string = extraction[2]
    # Go through each colour in the dictionary to test if the numbers are not surpassed
    for colour, max_amount in cube_dict.items():
        # Get the amounts from the game for the colour as integers
        amounts = re.findall(r"(\d+) " + re.escape(colour), search_string)
        amounts = list(map(int, amounts))
        # If the highest of the amounts is more than the dictionary value for the colour, break the loop
        if max(amounts) > max_amount:
            break
    # Else only runs if the for loop has successfully completed
    else:
        # Add the game number to the total score
        total_score += score
        continue

print(f"Part One total score: {total_score}")  # 2377

# Part 02: Calculate a total score, multiplying the minimum amount of cubes needed for the combination and summing them
new_total_score = 0
# Go through each input line
for game in input_list:
    # Reset the subtotal each time around
    subtotal = 1
    # Go through each colour in the dictionary to get their highest value to multiply with
    for colour in cube_dict.keys():
        # Get the amounts from the game for the colour as integers
        amounts = re.findall(r"(\d+) " + re.escape(colour), game)
        amounts = list(map(int, amounts))
        # Multiply the highest value for the current colour with the subtotal
        subtotal *= max(amounts)
    # Add the subtotal to the total score
    new_total_score += subtotal

print(f"Part Two total score: {new_total_score}")  # 71220
