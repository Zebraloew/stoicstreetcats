import random
import string

def generate_random_sequence(length=10):
    # Characters to choose from include ASCII letters and digits
    characters = string.ascii_letters + string.digits
    # Use random.choices to select `length` characters from the pool
    random_sequence = ''.join(random.choices(characters, k=length))
    return random_sequence

# Generate a random 10-character sequence
# random_sequence = generate_random_sequence()
# print("Random 10-character sequence:", random_sequence)
