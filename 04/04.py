# Day 04
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
day = "04"
input_file = open(f"{day}/input_{day}.txt")
input_list = input_file.read().splitlines()
print_line("*")

total_score = 0
for card in input_list:
    # Extract two number lists from the card string
    number_str_list = card[10:].split("|")
    winning_numbers = [x for x in number_str_list[0].split(" ") if not x == ""]
    numbers_you_have = [x for x in number_str_list[1].split(" ") if not x == ""]
    # Start at 0.5 because the first hit is worth 1
    card_score = 0.5
    # Calculate card score
    for winning_nr in winning_numbers:
        if winning_nr in numbers_you_have:
            card_score *= 2
    # Add card score to total
    if card_score >= 1:
        total_score += card_score

print(f"Total score for part I is {int(total_score)}")  # 19135
print_line("*")

# Set up card dictionary to keep track of number of cards
card_dict = {k: 1 for k in range(1, 189)}
for card in input_list:
    # Extract card number and two number lists from the card string
    card_nr = int(card[5:].split(":")[0].strip())
    number_str_list = card[10:].split("|")
    winning_numbers = [x for x in number_str_list[0].split(" ") if not x == ""]
    numbers_you_have = [x for x in number_str_list[1].split(" ") if not x == ""]
    # Get the number of hits per card
    nr_of_hits = 0
    for winning_nr in winning_numbers:
        if winning_nr in numbers_you_have:
            nr_of_hits += 1

    # Create a "number of copies" based on how many of this card exist
    if nr_of_hits > 0:
        for card_to_copy in range(card_nr + 1, card_nr + nr_of_hits + 1):
            if card_to_copy in card_dict.keys():
                card_dict[card_to_copy] = card_dict[card_to_copy] + card_dict[card_nr]

total_nr_of_cards = sum(card_dict.values())
print(f"Total score for part II is {int(total_nr_of_cards)}")  # 5704953
