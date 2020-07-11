import torch

w = torch.tensor([1.], requires_grad=True)
x = torch.tensor([2.], requires_grad=True)

a = torch.add(w, x)
b = torch.add(w, 1)
y = torch.mul(a, b)

y.backward()
print(w.grad)

print("Is_leaf: \n", w.is_leaf, x.is_leaf, a.is_leaf, b.is_leaf, y.is_leaf)

print("Gradient: \n", w.grad, x.grad, a.grad, b.grad, y.grad)

print("Grad_fn:\n", w.grad_fn, x.grad_fn, a.grad_fn, b.grad_fn, y.grad_fn)

