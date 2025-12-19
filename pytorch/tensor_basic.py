import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

print("a + b =", a + b)
print("a * b =", a * b)
print("dot product =", torch.dot(a, b))
