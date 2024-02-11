# Day XX
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
day = "99"
input_file = open(f"{day}/input_{day}.txt")
# input_file = open(f"input_{day}.txt")
input_list = input_file.read().splitlines()
print_line("*")

print_line("*")
print("Ciao bella, ciao")
