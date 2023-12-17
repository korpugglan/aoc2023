# Day 01
# Import packages
import text_to_num
import re

# Read input file
day = "01"
input_file = open(f"{day}/input_{day}.txt")
input_list = input_file.read().splitlines()

# Create a new list of first and last digit for each row
calibration_list = [int(str(re.findall(r"\d", input_string)[0]) + str(re.findall(r"\d", input_string)[-1]))
                    for input_string in input_list]
# Print the sum of all the new numbers
print(f"Sum of calibration list: {sum(calibration_list)}")

# Transform to keep digits
# for input_string in input_list[:5]:
#     print("=" * 20)
#     print(f"old input string: {input_string}")
#     string_length = len(input_string)
#     # Create a substring list for all possible substrings
#     substring_list = [input_string[i:j] for i in range(string_length) for j in range(i + 1, string_length + 1)]
#     # Remove all substrings containing digits and the string "o" which translates when it shouldn't
#     substring_list = [x for x in substring_list if not any(character.isdigit() for character in x) and x != "o"]
#     # Translate all substrings that are recognised as a number and replace them in the input string
#     for substring in substring_list:
#         new_substring = text_to_num.alpha2digit(substring, lang="en")
#         if substring != new_substring:
#             input_string = input_string.replace(substring, str(new_substring))
#             # print(f"substring: {substring}, translated: {new_substring}")
# #     # # new_data_row = ''.join(filter(lambda i: i.isdigit(), data_row))
#     print(f"new input string: {input_string}")

# print(input_list)
# [int(s) for s in txt.split() if s.isdigit()]
