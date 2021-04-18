import dimod
from dwave.system import LeapHybridSampler


def generate_partition_problem_bqm(s):
    linear = dict()
    quadratic = dict()
    c = sum(s)
    for i in range(len(s)):
        linear[i] = s[i]*(s[i] - c)
        for j in range(1 + i, len(s)):
            quadratic[(i, j)] = 2*s[i]*s[j]
    
    offset = 0.0
    vartype = dimod.BINARY
    return dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)


def sample_dwave(bqm, sample_label):
    sampler = LeapHybridSampler()
    sample_set = sampler.sample(bqm, label = sample_label)
    return sample_set.first.sample


def partition_numbers(s):
    s1 = list()
    s2 = list()
    bqm = generate_partition_problem_bqm(s)
    sample_label = "Partition Problem (" + str(len(s)) + " numbers)"
    sample = sample_dwave(bqm, sample_label)
    for i in range(len(sample)):
        if sample[i] == 1:
            s1.append(s[i]) 
        else:
            s2.append(s[i])
    
    return s1, s2


def perfectness(s1, s2):
    return abs(sum(s1) - sum(s2))


def main():
    #s = [4, 2, 7, 1]
    #s = [25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1, 25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1, 25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1, 25, 7, 13, 31, 42, 17, 21, 10, 4, 3, 8, 1]
    s = [25, 7, 13, 31, 42, 17, 21, 10]
    s1, s2 = partition_numbers(s)

    print(s1)
    print(s2)
    print("Perfectness: " + str(perfectness(s1, s2)))


main()
