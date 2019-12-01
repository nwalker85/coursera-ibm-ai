## wtf is a tensor?
# https://www.kdnuggets.com/2018/05/wtf-tensor.html

# the gist that I understand so far is that 
# it is a n-dimensional matrix whose data is tied to something else,
# so when you change x, the tensor also changes

# an individual, 0 dimentional tensor, is called a scalar.

import numpy as np

x = np.array(42)
print(x)
print('A scalar is of rank %d' %(x.ndim))

# a single dimension tensor is called a vector, most commonly referred to as an array in CS.

x = np.array([1, 1, 2, 3, 5, 8])
print(x)
print('A vector is of rank %d' %(x.ndim))

# 2d = matrix

x = np.array([[1, 4, 7],
              [2, 5, 8],
              [3, 6, 9]])
print(x)
print('A matrix is of rank %d' %(x.ndim))

# 3d+ = tensor

x = np.array([[[1, 4, 7],
               [2, 5, 8],
               [3, 6, 9]],
              [[10, 40, 70],
               [20, 50, 80],
               [30, 60, 90]],
              [[100, 400, 700],
               [200, 500, 800],
               [300, 600, 900]]])
print(x)
print('This tensor is of rank %d' %(x.ndim))


## wtf is a derivative?


# Here's my example: I throw a ball straight up at a speed of 6 meters
# per second somewhere where there's absolutely no air (no air 
# resistance). When will it be at its highest point?

# I can write the ball's height in an equation: the height at any 
# time t will be the ball's upward velocity times the amount of time 
# it's been going up (6m/sec times time, t) minus its gravitational 
# acceleration downward times the amount of time it's been up there 
# squared (10 m/sec/sec *that's the acceleration of gravity* times 
# time squared, t^2).  

# Leaving out the units so that the math is easier to see here:

#    Height = 6t-10t^2.

# If we take the derivative of this function, we have an equation for 
# the slope of this function at any given time, t. The value of t for 
# which this new equation is equal to zero is the same t at which the 
# height of the ball will be a maximum.

# Derivative of height = 6-20t = 0
#                    6 = 20t
#                    t = 6/20 second

# The ball will reach its maximum height in 6/20 of a second.




#input
velocity = 6 #m/s/s

#constant
gravity = 9.8 #m/s/s

time = 0

#formula for height
height = time * velocity - gravity * time * time

# y = 6x-9.8x^2

# If we take the derivative of this function, we have an equation for 
# the slope of this function at any given time, t.

# dx/dy = limit(h->0)[(6(x+h)-10(x+h)^2)/h]
# dx/dy = 6-19.6x = 0

# 0 = 6-19.6x
# 19.6x = 6
# x = 6/19.6
# if you throw a ball straight up at an initial velocity of 6 m/s, it will take 0.3061 seconds to reach its maximum height

# what is the max height?

v = 6
g = 9.8
t = 0.3061
h = (t*v)-(g*t**2)
print(h)


