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
input_list = input_file.read().splitlines()
print_line("*")

# Set up a seed dictionary
seed_dict = {seed: 0 for seed in input_list[0][7:].split(" ")}
print(seed_dict)
print_line("=")

# Loop through all the seeds to get a corresponding value, skipping the first two lines
hit_found = 0
for seed in ["432986705"]:
    # for seed in seed_dict.keys():
    print(f"Seed: {seed}")
    temp_nr = int(seed)
    print_line()
    for input_string in input_list[2:]:
        if input_string == "":
            hit_found = 0
        elif hit_found == 1:
            continue
        elif input_string[0].isdigit():
            map_list = [int(x) for x in input_string.split(" ")]
            dest_start = map_list[0]
            source_start = map_list[1]
            range_length = map_list[2]
            source_end = (source_start + range_length - 1)
            if source_start <= temp_nr <= source_end:
                temp_nr = dest_start
                hit_found = 1
        else:
            print(input_string)

    seed_dict[seed] = temp_nr
    print_line("=")

print(seed_dict)

print_line("*")
print("Ciao bella, ciao")

# TODO: reread instructions
# TODO: probably add any and pass as ranges selecting the nearest location at the end






