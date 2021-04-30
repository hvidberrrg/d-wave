import partition_problem as pp
import random

seed_numbers = [2, 8, 3 , 7, 9, 5, 4, 10]
set_of_numbers = list()
for i in range(125):
    for n in seed_numbers:
        set_of_numbers.append(n + i*100)

random.shuffle(set_of_numbers)
subset_of_numbers1, subset_of_numbers2 = pp.partition_numbers(set_of_numbers)

print("Input to the number partitioning problem:")
print(set_of_numbers)

print("First subset of numbers:")
print(subset_of_numbers1)
print("Size: ", end="")
print(len(subset_of_numbers1))

print("Second subset of numbers:")
print(subset_of_numbers2)
print("Size: ", end="")
print(len(subset_of_numbers2))

print("Perfectness: " + str(pp.perfectness(subset_of_numbers1, subset_of_numbers2)))
