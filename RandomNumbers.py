import random

random_fruit = random.choice(['pear', 'banana', 'apple', 'orange'])
print("Random fruit", random_fruit)

random_serie = random.sample(range(1000), 10)
print("Random serie: ", random_serie)

random_number = random.random()
print("Random number: ", random_number)

random_int = random.randint(0, 10)
print("Random int:", random_int)
