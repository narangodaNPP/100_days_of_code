import random

random_integer = random.randint(1, 10)
print(random_integer)

random_float = random.random() # gives floating point value between 0-1
print(random_float)

random_float = random.random() * 5 # gives floating point value between 0-5
print(random_float)

lv_score = random.randint(1, 100)
print(f"Your love score is {lv_score}.")
