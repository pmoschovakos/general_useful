import random

def generate_numbers(amount):
    random_numbers = []
    
    # We use an underscore '_' as the variable name because we just 
    # need the loop to run 'amount' times, but we don't actually 
    # need to use the loop counter itself.
    for _ in range(amount):
        # random.randint(a, b) generates a random integer N such that a <= N <= b.
        # The smallest 6-digit number is 100,000 and the largest is 999,999.
        new_number = random.randint(1000000, 9999999)
        random_numbers.append(new_number)
        
    return random_numbers

# Generate exactly 100 numbers
dataset = generate_numbers(24)

print(f"Successfully generated {len(dataset)} random 6-digit numbers.\n")

# Let's print the first 10 just to verify our output
print("Here:")
print(dataset[:100])