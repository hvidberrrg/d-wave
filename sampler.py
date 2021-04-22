from __future__ import annotations
import dimod
from dwave.system import LeapHybridSampler


def sample_dwave(bqm: dimod.BinaryQuadraticModel, sample_label: str) -> dict[int, int]:
    """Ask the DWave sampler to return the best sample for the supplied binary quadratic model

    Args:
        bqm (dimod.BinaryQuadraticModel):
            Binary qudratic model representing the problem
        sample_label (str):
            Label to use for the sample - appears in the DWave dashboard

        Returns:
            A dictionary mapping the location of each element in the input "vector" to the
            corresponding 0/1 value returned by the sampler
    """
    sampler = LeapHybridSampler()
    sample_set = sampler.sample(bqm, label=sample_label)
    return sample_set.first.sample
