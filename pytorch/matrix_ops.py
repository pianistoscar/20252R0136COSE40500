import torch

A = torch.tensor([[1.0, 2.0],
                  [3.0, 4.0]])

B = torch.tensor([[5.0, 6.0],
                  [7.0, 8.0]])

print("Matrix multiplication:")
print(torch.matmul(A, B))

print("Transpose of A:")
print(A.t())
