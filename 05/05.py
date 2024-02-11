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
# print(seed_dict)
# print_line("=")

# Loop through all the seeds to get a corresponding value, skipping the first two lines
hit_found = 0
# for seed in ["432986705"]:
for seed in seed_dict.keys():
    print(f"Seed: {seed}")
    temp_nr = int(seed)
    # print_line()
    # Run through all the input lines
    for input_string in input_list[2:]:
        # Reset the hit found counter on empty line
        if input_string == "":
            hit_found = 0
        # Keep skipping to the next line if a hit has been found
        elif hit_found == 1:
            continue
        # Check row for hits
        elif input_string[0].isdigit() and hit_found == 0:
            map_list = [int(x) for x in input_string.split(" ")]
            dest_start = map_list[0]
            source_start = map_list[1]
            range_length = map_list[2]
            source_end = (source_start + range_length - 1)
            # Get the new number on hit
            if source_start <= temp_nr <= source_end:
                temp_nr = dest_start + (temp_nr - source_start)
                hit_found = 1
        # else:
        #     print(f"{input_string} {temp_nr}")

    seed_dict[seed] = temp_nr
    print_line("=")

result_part_1 = min(seed_dict.values())
print(f"Solution for part I is: {result_part_1}")  # 216013985 too low

print_line("*")
print("Ciao bella, ciao")



