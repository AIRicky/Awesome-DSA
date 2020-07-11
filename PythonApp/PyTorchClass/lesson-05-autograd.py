import torch
torch.manual_seed(1)

# Ex-1: retain_graph

flag = 0
if flag:
    w = torch.tensor([1.], requires_grad=True)
    x = torch.tensor([2.], requires_grad=True)

    a = torch.add(w, x)
    b = torch.add(w, 1)
    y = torch.mul(a, b)

    y.backward(retain_graph=True)
    y.backward()


# Ex-2: grad_tensors
flag = 0
if flag:
    w = torch.tensor([1.], requires_grad=True)
    x = torch.tensor([2.], requires_grad=True)

    a = torch.add(w, x)
    b = torch.add(w, 1)

    y0 = torch.mul(a, b)
    y1 = torch.add(a, b)

    loss = torch.cat([y0, y1], dim=0)
    grad_tensors = torch.tensor([1., 2.])

    loss.backward(gradient=grad_tensors)
    print(w.grad)

# Ex-3: autograd.grad
flag = 0
if flag:
    x = torch.tensor([3.], requires_grad=True)
    y = torch.pow(x, 2)

    grad_1 = torch.autograd.grad(y, x, create_graph=True)
    print(grad_1)

    grad_2 = torch.autograd.grad(grad_1[0], x)
    print(grad_2)


# Ex-4:
flag = 0
if flag:
    a = torch.ones((1, ))
    print(id(a), a)
    a += torch.ones((1, ))
    print(id(a), a)


# Ex-5
flag = 0
if flag:
    w = torch.tensor([1.], requires_grad=True)
    x = torch.tensor([2.], requires_grad=True)

    a = torch.add(w, x)
    b = torch.add(w, 1)
    # y = wx*(w+1)
    y = torch.mul(a, b)

    w.add_(1)
    y.backward()

# Ex-6
flag = 0
if flag:
    w = torch.tensor([1.], requires_grad=True)
    x = torch.tensor([2.], requires_grad=True)

    a = torch.add(w, x)
    b = torch.add(w, 1)
    y = torch.mul(a, b)

    print(a.requires_grad, b.requires_grad, y.requires_grad)

# Ex-7
flag = 1
if flag:
    w = torch.tensor([1.], requires_grad=True)
    x = torch.tensor([2.], requires_grad=True)

    for i in range(4):
        a = torch.add(w, x)
        b = torch.add(w, 1)
        y = torch.mul(a, b)

        y.backward()
        print(w.grad)

        w.grad.zero_()