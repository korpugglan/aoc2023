# Day 01
# Import packages
from extended_int import int_inf
import text_to_num
import re


# Define functions
def find_extreme_digit(str_list):
    """Finds the first digit in a list of strings, as digit or written in English.
       Args:
           str_list (list): List containing strings.
       Returns:
           String that can be converted to an integer or None
    """
    # Add exception for translation to prevent text_to_num from translating it
    exception_list = ["o"]
    # Loop through all the strings in the list
    for digit_str in str_list:
        # If we find a digit first, return it
        if digit_str.isdigit():
            return digit_str
        # If we find a written number, that is not part of the exception list, translate and return it
        elif digit_str not in exception_list and digit_str != text_to_num.alpha2digit(digit_str,
                                                                                      lang="en",
                                                                                      ordinal_threshold=int_inf):
            return text_to_num.alpha2digit(digit_str, lang="en")
        # Try the next item in the list
        else:
            continue
    return


# Read input file
day = "01"
input_file = open(f"{day}/input_{day}.txt")
input_list = input_file.read().splitlines()

# Part 1
# Create a new list of first and last digit for each row
calibration_list = [int(str(re.findall(r"\d", input_string)[0]) + str(re.findall(r"\d", input_string)[-1]))
                    for input_string in input_list]
# Print the sum of all the new numbers
print(f"Sum of calibration list: {sum(calibration_list)}")  # 54667

# Part 2
calibration_total = 0
# Loop through the whole input list
for input_string in input_list:
    # Create a substring list for all possible substrings
    string_length = len(input_string)
    substring_list = [input_string[i:j] for i in range(string_length) for j in range(i + 1, string_length + 1)]
    # Find the first and last digits (reverse the substring list to find the last one)
    first = find_extreme_digit(substring_list)
    last = find_extreme_digit(list(reversed(substring_list)))
    # Add the newly generated number to the total
    calibration_total += int(first + last)

print(f"New calibration total: {calibration_total}")  # 54203
