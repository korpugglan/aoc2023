# Day 01
# Import packages
from extended_int import int_inf
import text_to_num
import re


# Define functions
def find_extreme_digit(substr_list):
    # Add exception for translation to prevent text_to_num from translating it
    exception_list = ["o"]
    for substr in substr_list:
        # If we find a digit first, return it
        if substr.isdigit():
            return substr
        # If we find a written number, that is not part of the exception list, translate and return it
        elif substr not in exception_list and substr != text_to_num.alpha2digit(substr,
                                                                                lang="en",
                                                                                ordinal_threshold=int_inf):
            return text_to_num.alpha2digit(substr, lang="en")
        # Try the next one
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
for input_string in input_list:
    # print(f"input string: {input_string}")
    string_length = len(input_string)
    # Create a substring list for all possible substrings
    substring_list = [input_string[i:j] for i in range(string_length) for j in range(i + 1, string_length + 1)]
    # print(substring_list)
    # Find the first and last digits
    first = find_extreme_digit(substring_list)
    last = find_extreme_digit(reversed(substring_list))
    # Add the newly generated number to the total
    calibration_total += int(first + last)
    # print(f"calibration temp: {calibration_total}")
    # print("=" * 20)

print(f"New calibration total: {calibration_total}")
