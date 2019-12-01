## Welcome to Pytorch

## Import convention seems to be just torch as opposed to how numpy and pandas set to np/pd.

import torch
import numpy as np
import pandas as pd

## torch is all about tensors. recall that a tensor is a type of matrix
# https://medium.com/@quantumsteinke/whats-the-difference-between-a-matrix-and-a-tensor-4505fbdc576c


a = torch.Tensor([1,2,3,4,5])
print(a.dtype)
print(a.type())
print(a.size())
print(a.ndimension())

a_col=a.view(5,1)

print(a_col)

a_col=a.view(-1,1)

print(a_col)

a = torch.Tensor([0,1,2,3,4,5])
a_col=a.view(6,1)
print(a_col)

numpy_array=np.array([0.0,1.0,2.0,3.0,4.0])
torch_tensor=torch.from_numpy(numpy_array)
back_to_numpy=torch_tensor.numpy()

print(numpy_array,torch_tensor,back_to_numpy)

pandas_series=pd.Series([0.1,2,0.3,10.1])
pandas_to_torch=torch.from_numpy(pandas_series.values)

print(pandas_series,pandas_to_torch)

a = torch.Tensor([0,1,2,3,4,5])
a_list = a.tolist()
print(a_list)

a = torch.Tensor([0,1,2,3,4,5])

print(a[0]) #prints a tensor
print(a[0].item()) # prints the number

c = torch.Tensor([10,0.5,20,3])
print(c)
c[0]=100
print(c)
c[3]=10
print(c)
d=c[1:3]
print(d)
d[0]=0
print(d)

print(c)
c[1:4]=torch.tensor([1,2,3])
print(c)

#vector arithmetic

u = torch.tensor([1,0])
v = torch.tensor([0,1])
z = u + v
print(z)

y = torch.tensor([1,2])
z = 2*y
print(z)

u = torch.tensor([1, 2, 3, -1])
v = u + 1
print(v)

u = torch.tensor([1, 2])
v = torch.tensor([3, 2])
z = u*v
print(z)

# dot product
 
u = torch.tensor([1,2])
v = torch.tensor([3,1])
z = torch.dot(u,v)
print(z)

# the act of adding a scalar to a tensor is called "broadcasting"
u = torch.tensor([1,2,3,-1])
z = u+1
print(z)


a = torch.tensor([1.0,-1.0,1.0,-1.0])
mean_a = a.mean()
print(mean_a)

b = torch.tensor([1,-2,3,4,5])
print(b.max())

pi = np.pi
x = torch.tensor([0, pi/2, pi])
y = torch.sin(x)
print(y)

#return evenly spaced numbers over a specified interval
#this is pretty neat.
z = torch.linspace(-2,2, steps=5)
print(z)

x=torch.linspace(0,2*pi,100)
y=torch.sin(x)

import matplotlib.pyplot as plt
plt.plot(x.numpy(),y.numpy())
