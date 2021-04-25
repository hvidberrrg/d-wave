# D-Wave experiments
**Static Analysis:** 
[![Scanned on SonarCloud](https://sonarcloud.io/api/project_badges/measure?project=hvidberrrg_d-wave&metric=alert_status)](https://sonarcloud.io/dashboard?id=hvidberrrg_d-wave)

This repository implements some of the examples given in "Quantum Bridge Analytics I: A Tutorial on Formulating and Using QUBO Models" by Glover et al. [1]. It should be noted that [1] operates with symmetric QUBO matrices while the D-Wave [binary quadratic model](https://docs.ocean.dwavesys.com/en/stable/concepts/bqm.html) represents the QUBO variables as an upper-diagonal/upper-triangular matrix. A symmetric matrix <i>Q</i> is easily transformed to upper-diagonal form by replacing  <i>q<sub>ij</sub></i> with <i>q<sub>ij</sub> + q<sub>ji</sub></i>, for all <i>i</i> and <i>j</i> with <i>j > i</i>. All <i>q<sub>ij</sub></i> with <i>j < i</i> are replaced by <i>0</i>. So we are just doubling all values above the main diagonal (as the matrix is symmetric) and setting all values below the main diagonal to <i>0</i> 


## The number partitioning problem

The variant of the number partitioning problem we look at here involves partitioning a set of numbers into two subsets such that the subset sums are as close to each other as possible. The formulation of the binary quadratic model is based on the QUBO optimization problem described in [1]. You can find more background on the hardness of the problem in [2].

Consider a set of numbers <i>S = {s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>n</sub>}</i> and let <i>x<sub>i</sub> = 1</i> if <i>s<sub>i</sub></i> is assigned to subset 1; <i>0</i> otherwise. The sum for subset 1 is then given by <i>sum<sub>1</sub> = &Sigma;s<sub>i</sub>x<sub>i</sub>, 1&le;i&le;n</i>, and the sum for subset 2 is given by <i>sum<sub>2</sub> = &Sigma;s<sub>i</sub> - &Sigma;s<sub>i</sub>x<sub>i</sub>, 1&le;i&le;n</i>.

The difference in the sums is then <i>diff = &Sigma;s<sub>i</sub> - 2&Sigma;s<sub>i</sub>x<sub>i</sub> = c - 2&Sigma;s<sub>i</sub>x<sub>i</sub>, 1&le;i&le;n</i>. (where <i>c</i> denotes the (constant) sum of all the numbers in the set).

The difference is minimized by minimizing:
<i>diff<sup>2</sup> = (c - 2&Sigma;s<sub>i</sub>x<sub>i</sub>)<sup>2</sup>, 1&le;i&le;n = x<sup>T</sup>Qx</i>

Where <i>x</i> is the (<i>n</i>-)vector deciding whether a given number belongs to set 1 or set 2, and <i>Q</i> is a symmetric <i>n X n</i> matrix where <i>q<sub>ii</sub> = s<sub>i</sub>(s<sub>i</sub> - c)</i> and <i>q<sub>ij</sub> = s<sub>i</sub>s<sub>j</sub> = s<sub>j</sub>s<sub>i</sub></i> (to convince myself I scribbled down the [math](images/math/number_partitioning_problem.jpg) - note that <i>x = x<sup>2</sup></i> as <i>x</i> either has the value <i>0</i> or <i>1</i>).

If you run the implementation given in `partition_problem.py` you should see the example set `s = [25, 7, 13, 31, 42, 17, 21, 10]` partitioned into either `s1 = [25, 7, 13, 17, 21]`
and `s2 = [31, 42, 10]`, or `s1 = [7, 13, 42, 21]` and `s2 = [25, 31, 17, 10]`. Both are perfect partitions.

## References

[1] Fred Glover, Gary Kochenberger, Yu Du, "Quantum Bridge Analytics I: A Tutorial on Formulating and Using QUBO Models",
[arXiv:1811.11538](https://arxiv.org/abs/1811.11538)

[2] Stephan Mertens, "The Easiest Hard Problem: Number Partitioning", [arXiv:cond-mat/0310317](https://arxiv.org/abs/cond-mat/0310317)

[3] Abhijith et al., "Quantum Algorithm Implementations for Beginners", [arXiv:1804.03719](https://arxiv.org/abs/1804.03719)
