import torch

a = torch.tensor([1, 2, 3])
b = torch.tensor([4, 5, 6])

dot = torch.dot(a, b)
element_wise = a * b

print(f"Dot product: {dot}")
print(f"Element-wise Multiplication: {element_wise}")