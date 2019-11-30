import torch

a = torch.Tensor([1,2,3,4,5])
print(a.dtype)
print(a.type())
print(a.size())
print(a.ndimension())

a_col=a.view(5,1)

print(a_col)