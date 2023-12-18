# Use Python's random number module to generate a random number.
import random

# Generate five random numbers (between 1 and 69)
LuckyNumbers = sorted(random.randint(1, 69) for _ in range(5))

# Generate the Powerball number (1 and 26)
Powerball = random.randint(1, 26)

# Print the generated numbers, (Ammended with sorted() to display generated numbers
# in sequence.)
print(f"Your 5 lucky numbers are: {LuckyNumbers}")
print(f"and your Powerball number is {Powerball}. Good luck!")

#Source: https://runestone.academy/ns/books/published/py4e-int/functions/randomnumbers.html
