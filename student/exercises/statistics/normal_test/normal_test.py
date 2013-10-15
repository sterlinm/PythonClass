"""
Test for Normal Distribution
----------------------------

The file "rdata.txt" contains a column of numbers.

1. Load the data "rdata.txt" into an array called 'x'.

2. Apply the Anderson-Darling (scipy.stats.anderson) and Kolmogorov-Smirnov
   (scipy.stats.kstest) tests to 'x', using a 5 percent confidence level.
   What do you conclude?
   
3. Apply the Anderson-Darling and Kolmogorov-Smirnov tests to 'dx', where
   'dx = numpy.diff(x)', using a five percent confidence level.  What do you
   conclude?

See :ref:`normal-test-solution`.
"""

from numpy import loadtxt, diff
from scipy.stats import anderson, kstest, zscore

x = loadtxt('rdata.txt')
