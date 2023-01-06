import random
import time
import math

pi = math.pi

def generate_random_number():
    num_1 = random.randint(1, 9999)
    float_num_1 = random.randint(1, 9999)
    return float(f"{num_1}.{float_num_1}")

def generate_formula(operation):
    num_1 = generate_random_number()
    num_2 = generate_random_number()
    if operation == 0:
        return f"{num_1} + {num_2} = {num_1 + num_2}"
    elif operation == 1:
        return f"{num_1} - {num_2} = {num_1 - num_2}"
    elif operation == 2:
        return f"{num_1} x {num_2} = {num_1 * num_2}"
    elif operation == 3:
        return f"{num_1} / {num_2} = {num_1 / num_2}"

num_iterations = random.randint(1, 101)
count = 0

while count < num_iterations:
    formula = generate_formula(random.randint(0, 3))
    print(formula)
    time.sleep(pi)
    count += 1
