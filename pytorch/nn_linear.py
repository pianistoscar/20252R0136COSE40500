import torch
import torch.nn as nn

model = nn.Linear(3, 1)

x = torch.randn(5, 3)
y = model(x)

print("Input shape:", x.shape)
print("Output shape:", y.shape)
