"""
Linear Regression of Mileage Data
---------------------------------

The file "mileage_data_1991.txt" contains information from 1991 about
several models of cars.  The fields in the file are:

MAKE/MODEL: Manufacturer and model name
VOL: Cubic feet of cab space
HP: Engine horsepower
MPG: Average miles per gallon
SP: Top speed (mph)
WT: Vehicle weight (100 lb) 

1. Read the data into an array. (This is already done.)

2. Use scipy.stats.linregress to compute the linear regression line
   for the weight (WT) and mileage (MPG) of the cars.  Print the correlation
   coefficient.

3. Repeat 2 for the weight and "gallons-per-mile" for the cars.

4. (Optional) For 2 and 3, plot the data with the weight on the x-axis, and
   plot the regression line. (Use separate figures for 2 and 3.)

See :ref:`mileage-solution`.
"""


from numpy import loadtxt, array
from matplotlib.pyplot import plot, show, xlim, xlabel, ylabel, figure
from scipy.stats import linregress

VOLUME = 0
HP = 1
MPG = 2
SP = 3
WT = 4

# Skip the first row, which is the headers, and don't try to read the
# first column, which is the make and model.
data = loadtxt('mileage_data_1991.txt', skiprows=1, usecols=(1,2,3,4,5))

# For convenience, pull out the WT and MPG columns.
wt = data[:,WT]
mpg = data[:,MPG]

gpm = 1.0/mpg

# Compute the linear regressions.
m1, b1, r1, p1, se1 = linregress(wt, mpg)
m2, b2, r2, p2, se2 = linregress(wt, gpm)

print "MPG: r =", r1
print "GPM: r =", r2

wt_lim = array([wt.min(), wt.max()])

figure(1)
plot(wt, mpg, 'bo')
plot(wt_lim, m1*wt_lim + b1, 'r')
xlim(15,60)
xlabel('Weight (100 lb)')
ylabel('MPG')

figure(2)
plot(wt, gpm, 'bo')
plot(wt_lim, m2*wt_lim + b2, 'r')
xlim(15,60)
xlabel('Weight (100 lb)')
ylabel('GPM')
show()
