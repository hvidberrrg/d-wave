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

def sample_dwave(s):
    bqm = generate_partition_problem_bqm(s)
    sampler = LeapHybridSampler()
    sampleset = sampler.sample(bqm, label="Partition Problem (" + str(len(s)) + " numbers)")
    return sampleset.first.sample

#s = [4, 2, 7, 1]
s = [25, 7, 13, 31, 42, 17, 21, 10]
sample = sample_dwave(s)
print(sample)