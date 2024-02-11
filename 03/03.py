# Day 03 (VERY UGLY CODE AND SOLUTION)
# Define functions
def check_for_symbol(input_string, range_start, range_end):
    check_string = input_string[range_start:range_end]
    for check in check_string:
        if check == "." or check.isdigit():
            continue
        else:
            return True
    return False


def complete_number(row, start_index, max_index):
    number = row[start_index]

    left_index = start_index - 1
    while left_index >= 0 and row[left_index].isdigit():
        number = row[left_index] + number
        left_index -= 1

    right_index = start_index + 1
    while right_index <= max_index and row[right_index].isdigit():
        number = number + row[right_index]
        right_index += 1

    return int(number)


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

# Part 01
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

# Part 02
# Initial variables
new_total_score = 0
max_row_nr = len(input_list) - 1
# Loop through all the input rows
for row_nr, input_row in enumerate(input_list):
    max_position = len(input_row) - 1
    # Loop through the row string and find *
    for position, character in enumerate(input_row):
        if character == "*":
            # Create a new empty numbers list for this particular *
            numbers_list = []

            # Define horizontal check positions
            # Setting to 0 prevents indexing issues and has a check performed on a digit in the worst case
            if position - 1 < 0:
                left_check_position = 0
            else:
                left_check_position = position - 1
            if position + 1 > max_position:
                right_check_position = max_position
            else:
                right_check_position = position + 1

            # Keep checking for adjacent number until it finds 2 of them
            # Check above
            if row_nr > 0:
                # Get the values to check for above
                check_range = input_list[row_nr - 1][left_check_position:right_check_position + 1]
                # If the digits are split, there are two numbers
                if check_range[0].isdigit() and not check_range[1].isdigit() and check_range[2].isdigit():
                    numbers_list.append(complete_number(input_list[row_nr - 1], left_check_position, max_position))
                    numbers_list.append(complete_number(input_list[row_nr - 1], right_check_position, max_position))
                # Otherwise, if any digit is found, add the single number
                elif any(x.isdigit() for x in check_range):
                    for nr, x in enumerate(check_range):
                        if x.isdigit():
                            numbers_list.append(complete_number(input_list[row_nr - 1],
                                                                left_check_position + nr,
                                                                max_position))
                            break

            # Check horizontal
            if input_row[left_check_position].isdigit():
                numbers_list.append(complete_number(input_row, left_check_position, max_position))
            if input_row[right_check_position].isdigit():
                numbers_list.append(complete_number(input_row, right_check_position, max_position))

            # Check below
            if row_nr < max_row_nr:
                # Get the values to check for below
                check_range = input_list[row_nr + 1][left_check_position:right_check_position + 1]
                # If the digits are split, there are two numbers
                if check_range[0].isdigit() and not check_range[1].isdigit() and check_range[2].isdigit():
                    numbers_list.append(complete_number(input_list[row_nr + 1], left_check_position, max_position))
                    numbers_list.append(complete_number(input_list[row_nr + 1], right_check_position, max_position))
                # Otherwise, if any digit is found, add the single number
                elif any(x.isdigit() for x in check_range):
                    for nr, x in enumerate(check_range):
                        if x.isdigit():
                            numbers_list.append(complete_number(input_list[row_nr + 1],
                                                                left_check_position + nr,
                                                                max_position))
                            break

            # Add the factor of the numbers to the total score if two have been found
            if len(numbers_list) == 2:
                new_total_score += (numbers_list[0] * numbers_list[1])

            numbers_list = []

print(f"New total score: {new_total_score}")  # 78236071
