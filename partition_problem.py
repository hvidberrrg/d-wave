import dimod
from dwave.system import LeapHybridSampler

linear = {1: -40, 2: -24, 3: -49, 4: -13}
quadratic = {(1, 2): 16, (1, 3): 56, (1, 4): 8,
             (2, 3): 28, (2, 4): 4,
             (3, 4): 14}
offset = 0.0
vartype = dimod.BINARY
bqm = dimod.BinaryQuadraticModel(linear, quadratic, offset, vartype)

sampler = LeapHybridSampler()
sampleset = sampler.sample(bqm)
sample = sampleset.first.sample
print(sample)