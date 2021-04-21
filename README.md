# d-wave
**Static Analysis:** 
[![Scanned on SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=hvidberrrg_d-wave&metric=alert_status)](https://sonarcloud.io/dashboard?id=hvidberrrg_d-wave)

## The number partitioning problem

The variant of the number partitioning problem we look at here involves partitioning a set of numbers into two subsets such that the subset sums are as close to each other as possible. The formulation of the binary quadratic model is based on the QUBO optimization problem described in [1]. You can find more background on the hardness of the problem in [2].

It should be noted that [1] operates with symmetric QUBO matrices while the D-Wave [binary quadratic model](https://docs.ocean.dwavesys.com/en/stable/concepts/bqm.html) represents the QUBO variables as an upper-diagonal/upper-triangular matrix. The matrices used in [1] are easily transformed to upper-diagonal form by, for all <i>i</i> and <i>j</i> with <i>j > i</i>, replacing  <i>q<sub>ij</sub></i> with <i>q<sub>ij</sub> + q<sub>ji</sub></i> (i.e. just double the value of <i>q<sub>ij</sub></i> as the matrix is symmetric). All <i>q<sub>ij</sub></i> with <i>j < i</i> are replaced by <i>0</i>. So we are just doubling all values above the main diagonal and setting all values below the main diagonal to <i>0</i> 

If you run the implementation given in `partition_problem.py` you should see the example set `s = [25, 7, 13, 31, 42, 17, 21, 10]` partitioned into either `s1 = [25, 7, 13, 17, 21]`
and `s2 = [31, 42, 10]`, or `s1 = [7, 13, 42, 21]` and `s2 = [25, 31, 17, 10]`. Both are perfect partitions.

## References

[1] Fred Glover, Gary Kochenberger, Yu Du, "Quantum Bridge Analytics I: A Tutorial on Formulating and Using QUBO Models",
[arXiv:1811.11538](https://arxiv.org/abs/1811.11538)

[2] Stephan Mertens, "The Easiest Hard Problem: Number Partitioning", [arXiv:cond-mat/0310317](https://arxiv.org/abs/cond-mat/0310317)
