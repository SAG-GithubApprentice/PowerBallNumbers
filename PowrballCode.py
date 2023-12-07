# Use Python's random number module to generate a random number.
import random

# Generate five random numbers (between 1 and 69)
LuckyNumbers = [random.randint(1, 69) for _ in range(5)]

# Generate the Powerball number (1 and 26)
Powerball = random.randint(1, 26)

# Print the generated numbers, (Ammended with sorted() to display generated numbers
# in sequence.)
print("Your Lucky 5 Numbers:", sorted(LuckyNumbers))
print("Your Powerball Number:", Powerball)
print("Good Luck!")

#Source: https://runestone.academy/ns/books/published/py4e-int/functions/randomnumbers.html