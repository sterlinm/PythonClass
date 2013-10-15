
"""
Chi-square test
---------------

1. A six-sided die is rolled 50 times, and the number of occurrences
   of each side are recorded in the following table::

      +-------------+-----+-------+------+-----+------+------+
      | Side        |  1  |   2   |   3  |  4  |   5  |   6  |
      +-------------+-----+-------+------+-----+------+------+
      | Occurrences |  6  |   1   |   9  |  7  |  14  |  13  |
      +-------------+-----+-------+------+-----+------+------+
  
   Is the die fair?   That is, is each side equally likely?


2. 17 woman and 18 men are asked whether they prefer chocolate or
   vanilla ice cream.  The following table shows the result::
   
       +-------+-----------+---------+
       | Group | Chocolate | Vanilla |
       +-------+-----------+---------+
       | Women |    12     |    5    |
       +-------+-----------+---------+
       | Men   |    10     |    8    |
       +-------+-----------+---------+
   
   Use the chi-square test to investigate the relation between an
   individual's sex and the individual's preference for ice cream.
   Then apply Fisher's exact test (scipy.stats.fisher_exact), and
   compare the results.

See :ref:`chi-square-solution`.         
"""

import numpy as np
from scipy.stats import chisquare, chi2_contingency, fisher_exact

# 1. Six-sided die.

print "H0: Each side of the die is equally probable."

num = np.array([6, 1, 9, 7, 14, 13])

chi2, p = chisquare(num)

print "p = %6.4f" % p
if p < 0.05:
    print "Reject H0."
else:
    print "Do not reject H0."


# 2. Ice cream preference.

print
print "H0: Preference for ice cream flavor is independent of sex."

table = np.array([[12, 5], [10, 8]])

chi2, p, dof, ex = chi2_contingency(table)

print "Chi-squared test: p = %6.4f" % p
if p < 0.05:
    print "Reject H0."
else:
    print "Do not reject H0."

odds_ratio, pvalue = fisher_exact(table)
print "Fisher exact test: p = %6.4f" % pvalue
if pvalue < 0.05:
    print "Reject H0."
else:
    print "Do not reject H0."
