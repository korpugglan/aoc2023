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

# Set up a new seed dictionary
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
print_line("=")


# TODO: redo, this is way too slow


sts_list = []
stf_list = []
ftw_list = []
wtl_list = []
ltt_list = []
tth_list = []
htl_list = []


def find_match(nr_in, checklist):
    nr_out = nr_in
    for item in checklist:
        if item[0] <= nr_in < (item[0] + item[2]):
            nr_out = item[1] + (nr_in - item[0])
            break

    return nr_out


def set_up_lists(lines_file):
    global sts_list
    global stf_list
    global ftw_list
    global wtl_list
    global ltt_list
    global tth_list
    global htl_list
    last_string = ""

    for lines_file_string in lines_file:
        if lines_file_string == "":
            last_string = ""
        elif lines_file_string[0].isalpha():
            last_string = lines_file_string

        if last_string == "seed-to-soil map:" and lines_file_string[0].isdigit():
            sts_list.append([int(x) for x in lines_file_string.split(" ")])
        elif last_string == "soil-to-fertilizer map:" and lines_file_string[0].isdigit():
            stf_list.append([int(x) for x in lines_file_string.split(" ")])
        elif last_string == "fertilizer-to-water map:" and lines_file_string[0].isdigit():
            ftw_list.append([int(x) for x in lines_file_string.split(" ")])
        elif last_string == "water-to-light map:" and lines_file_string[0].isdigit():
            wtl_list.append([int(x) for x in lines_file_string.split(" ")])
        elif last_string == "light-to-temperature map:" and lines_file_string[0].isdigit():
            ltt_list.append([int(x) for x in lines_file_string.split(" ")])
        elif last_string == "temperature-to-humidity map:" and lines_file_string[0].isdigit():
            tth_list.append([int(x) for x in lines_file_string.split(" ")])
        elif last_string == "humidity-to-location map:" and lines_file_string[0].isdigit():
            htl_list.append([int(x) for x in lines_file_string.split(" ")])

    return


set_up_lists(input_list[2:])
# Set up a new seed dictionary
seed_list = input_list[0][7:].split(" ")
range_dict = {}
for seed_list_index in range(0, len(seed_list), 2):
    range_dict[int(seed_list[seed_list_index])] = int(seed_list[seed_list_index + 1])

location = 0
match_found = 0
while True:
    test_nr = location
    print(f"Start location: {test_nr}")
    test_nr = find_match(test_nr, htl_list)
    test_nr = find_match(test_nr, tth_list)
    test_nr = find_match(test_nr, ltt_list)
    test_nr = find_match(test_nr, wtl_list)
    test_nr = find_match(test_nr, ftw_list)
    test_nr = find_match(test_nr, stf_list)
    test_nr = find_match(test_nr, sts_list)
    # print(f"Number to test: {test_nr}")

    if test_nr >= min(range_dict.keys()):
        for range_start, range_length in range_dict.items():
            if range_start <= location < (range_start + range_length):
                match_found = 1
                break

    if match_found == 1:
        print(f"Solution for part II is: {location}")  #
        break

    location += 1

print_line("*")
print("Ciao bella, ciao")
