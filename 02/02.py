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

# Calculate total score, summing the game numbers of possible combinations
total_score = 0
for game in input_list:
    print_line()
    print(f"TOTAL SCORE: {total_score}")
    print(game)
    extraction = re.match(r"^Game\s(\d+):\s(.*)$", game)
    score = int(extraction[1])
    search_string = extraction[2]
    for colour, max_amount in cube_dict.items():
        amounts = re.findall(r"(\d+) " + re.escape(colour), search_string)
        amounts = list(map(int, amounts))
        print(f"colour: {colour}, colour max: {max_amount}, found: {amounts}, max found: {max(amounts)}")
        if max(amounts) > max_amount:
            print("Failed")
            break
    else:
        total_score += score
        print("Passed")
        continue

print(total_score)  # 2377

