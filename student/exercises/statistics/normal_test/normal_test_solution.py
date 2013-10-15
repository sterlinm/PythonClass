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

print "Testing x"
a, c, s = anderson(x, 'norm')
print "anderson:",
print a, c[2],
if a > c[2]:
    print "not normal"
else:
    print "no conclusion"

kstat, kp = kstest(zscore(x), 'norm')
print "ks:",
print kp,
if kp < 0.05:
    print "not normal"
else:
    print "no conclusion"

print 
print "Testing dx"
dx = diff(x)

a1, c1, s1 = anderson(dx, 'norm')
print "anderson:",
print a1, c1[2],
if a1 > c1[2]:
    print "not normal"
else:
    print "no conclusion"

kstat1, kp1 = kstest(zscore(dx), 'norm')
print "ks:",
print kp1,
if kp1 < 0.05:
    print "not normal"
else:
    print "no conclusion"
