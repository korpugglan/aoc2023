# Day 03
# Define functions
def check_for_symbol(input_string, range_start, range_end):
    check_string = input_string[range_start:range_end]
    for check in check_string:
        if check == "." or check.isdigit():
            continue
        else:
            return True
    return False


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


# Load input data
day = "03"
input_file = open(f"{day}/input_{day}.txt")
input_list = input_file.read().splitlines()

# Total score
total_score = 0
max_row_nr = len(input_list) - 1
for row_nr, input_row in enumerate(input_list):
    print_line("=", repetition=144)
    print(input_row)

    digit_string = ""
    position_list = []
    max_position = len(input_row) - 1

    for position, character in enumerate(input_row):
        # If digit, add it to string and append position
        if character.isdigit():
            digit_string += character
            position_list.append(position)

        # If a digit string has been created and (character is not a digit or is a digit on the last position)
        if digit_string != "" and (not character.isdigit() or position == max_position):
            print(f"Digit string: {digit_string}")
            # Define horizontal check positions
            left_check_position = min(position_list) - 1
            right_check_position = max(position_list) + 1

            # Check left
            if left_check_position >= 0:
                if check_for_symbol(input_row, left_check_position, left_check_position + 1):
                    print("Found one on the left")
                    total_score += int(digit_string)
                    digit_string = ""
                    position_list = []
                    continue
            # Check right
            if right_check_position <= max_position:
                if check_for_symbol(input_row, right_check_position, right_check_position + 1):
                    print("Found one on the right")
                    total_score += int(digit_string)
                    digit_string = ""
                    position_list = []
                    continue

            # Fix for ranges
            if left_check_position < 0:
                left_check_position = 0
            if right_check_position >= max_position:
                right_check_position = max_position

            # Check above
            if row_nr > 0:
                if check_for_symbol(input_list[row_nr - 1], left_check_position, right_check_position + 1):
                    print("Found one above")
                    total_score += int(digit_string)
                    digit_string = ""
                    position_list = []
                    continue
            # Check below
            if row_nr < max_row_nr:
                if check_for_symbol(input_list[row_nr + 1], left_check_position, right_check_position + 1):
                    print("Found one below")
                    total_score += int(digit_string)
                    digit_string = ""
                    position_list = []
                    continue
            # print(digit_string)
            # print(position_list)

            digit_string = ""
            position_list = []

    print(f"Total score: {total_score}")  # 533287 too low

