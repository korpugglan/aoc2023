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


def update_total_score_and_reset_digit_data():
    global total_score
    global digit_string
    global position_list

    total_score += int(digit_string)
    digit_string = ""
    position_list = []

    return

# Load input data
day = "03"
input_file = open(f"{day}/input_{day}.txt")
input_list = input_file.read().splitlines()

# Initial variables
total_score = 0
digit_string = ""
position_list = []
max_row_nr = len(input_list) - 1
# Loop through all the input rows
for row_nr, input_row in enumerate(input_list):
    # Define the last position for this row
    max_position = len(input_row) - 1
    # Loop through all the characters in the input row
    for position, character in enumerate(input_row):
        # If it is a digit, add it to a digit string and append its position to a list
        if character.isdigit():
            digit_string += character
            position_list.append(position)

        # If a digit string exists and the current character is either not a digit or in the last position in the string
        if digit_string != "" and (not character.isdigit() or position == max_position):
            # Define horizontal check positions
            # Setting to 0 prevents indexing issues and has a check performed on a digit in the worst case
            if min(position_list) - 1 < 0:
                left_check_position = 0
            else:
                left_check_position = min(position_list) - 1
            if max(position_list) + 1 > max_position:
                right_check_position = max_position
            else:
                right_check_position = max(position_list) + 1

            # Check left
            if check_for_symbol(input_row, left_check_position, left_check_position + 1):
                update_total_score_and_reset_digit_data()
                continue
            # Check right
            if check_for_symbol(input_row, right_check_position, right_check_position + 1):
                update_total_score_and_reset_digit_data()
                continue
            # Check above
            if row_nr > 0 and \
               check_for_symbol(input_list[row_nr - 1], left_check_position, right_check_position + 1):
                update_total_score_and_reset_digit_data()
                continue
            # Check below
            if row_nr < max_row_nr and \
               check_for_symbol(input_list[row_nr + 1], left_check_position, right_check_position + 1):
                update_total_score_and_reset_digit_data()
                continue

            digit_string = ""
            position_list = []

print(f"Total score: {total_score}")  # 533775

