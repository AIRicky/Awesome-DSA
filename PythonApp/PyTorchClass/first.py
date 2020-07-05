import numpy as np
import torch
import torchvision


# print("Hello pytorch {}".format(torch.__version__))

# example 1

# flag = True
flag = False
if flag:
    arr = np.ones((3, 3))
    print("ndarray 的数据类型", arr.dtype)

    t = torch.tensor(arr)
    # t = torch.tensor(arr, device='cuda')

    print(t)


# example 2
flag = True
# flag = False
if flag:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    t = torch.from_numpy(arr)

    print("ndarray: ", arr)
    print("tensor: ", t)

    arr[0, 0] = 0
    print("ndarray: ", arr)
    print("tensor: ", t)

    t[1, 1] = 0
    print("ndarray: ", arr)
    print("tensor: ", t)


# example 3

# flag = True
flag = False
if flag:
    out_t = torch.tensor([1])
    t = torch.zeros((3, 3), out=out_t)
    print(t, '\n', out_t)
    print(id(t), id(out_t), id(t) == id(out_t))


# example 4
# flag = True
flag = False
if flag:
    t1 = torch.full((3, 3), 1)
    arr = np.array([[1, 2, 3], [4, 5, 6]])

    t2 = torch.full_like(torch.from_numpy(arr), 3)
    print(t1, '\n', t2)


# example 5
# flag = True
flag = False
if flag:
    t = torch.arange(2, 10, 2)
    print(t)
    print(t.dtype)


# example 6
# flag = True
flag = False
if flag:
    t1 = torch.linspace(2, 10, 5)
    print(t1)

    t2 = torch.linspace(2, 10, 6)
    print(t2)

    t3 = torch.logspace(2, 6, 3, 2)
    print(t3)

    t4 = torch.eye(5)
    print(t4)



