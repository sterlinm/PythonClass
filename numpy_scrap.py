# Numpy Scrap Work
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# Documentation
# http://docs.scipy.org/doc

# Examples
# http://www.scipy.org/Numpy_Example_List_With_Doc

# Arrays
x = np.array([1.0, 3.2, 4.0])
y = np.array([1,2,3])

# Object Type vs Data Type
# The type of x and y is numpy.ndarray
print 'Type of x:', type(x)
print 'Type of y:', type(y)
# But dtype of x is 'float64'
print 'Data type of x:', x.dtype
# And dtype of y is 'float64'
print 'Data type of y:', y.dtype

# Simple Array Math
a = np.array([1,2,3,4])
b = np.array([2,3,4,5])
a + b # element by element addition
a * b # element by element multiplication
a ** b


# Create array from 0 to 10
x = np.arange(11.)

# multiply entire array by scalar value
c = (2*pi)/10.
c
c*x

# Plotting
x = np.linspace(-2,2,100)
plt.plot(x, np.sin(x))
plt.hold(True)
plt.plot(x, np.cos(x), 'r')
plt.show()

#clear figure
# clf()

# Subplots
plt.figure()
plt.subplot(3,2,1)
plt.plot(x, np.sin(x))
plt.subplot(3,2,2)
plt.plot(x, np.cos(x))
plt.subplot(3,1,2)
plt.plot(x, np.tan(x))
plt.subplot(3,1,3)
plt.plot(x, np.arctan(x))
plt.show()

# Indexing vs Fancy Indexing
# Indexing creates a view of an array while fancy indexing creates a copy
x = np.arange(12).reshape(3,4)+1
y = x[0,:]
y[1] = -999 # modifies x
z = x[[0],:]
z[0][-1] = 999 # modifies z but not x