# Day 05
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


# Load input data
day = "05"
input_file = open(f"{day}/input_{day}.txt")
# input_file = open(f"input_{day}.txt")
input_list = input_file.read().splitlines()
print_line("*")

# Set up a seed dictionary
seed_dict = {int(seed): 0 for seed in input_list[0][7:].split(" ")}

# Loop through all the seeds to get a corresponding location value, skipping the first two lines
for seed in seed_dict.keys():
    temp_nr = seed
    hit_found = 0
    # Loop through all the input lines
    for input_string in input_list[2:]:
        # Reset on empty line
        if input_string == "":
            hit_found = 0
        # Skip if a match has been found
        elif hit_found == 1:
            continue
        # Check for matches
        elif input_string[0].isdigit():
            map_list = [int(x) for x in input_string.split(" ")]
            # If a match has been found, set the temp_nr to the destination number
            if map_list[1] <= temp_nr < (map_list[1] + map_list[2] - 1):
                temp_nr = map_list[0] + (temp_nr - map_list[1])
                hit_found = 1

    # Save to dictionary
    seed_dict[seed] = temp_nr

# Get the lowest location value from the dictionary
result_part_1 = min(seed_dict.values())
print(f"Solution for part I is: {result_part_1}")  # 2621354867


print_line("*")
print("Ciao bella, ciao")



