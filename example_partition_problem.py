import qubo.partition_problem as pp

set_of_numbers = [25, 7, 13, 31, 42, 17, 21, 10]  # The set of numbers is represented as a list to maintain ordering
subset_of_numbers1, subset_of_numbers2 = pp.partition_numbers(set_of_numbers)

print("Input to the number partitioning problem: ", end="")
print(set_of_numbers)
print("First subset of numbers: ", end="")
print(subset_of_numbers1)
print("Second subset of numbers: ", end="")
print(subset_of_numbers2)
print("Perfectness: " + str(pp.perfectness(subset_of_numbers1, subset_of_numbers2)))
