import torch
import numpy as np
torch.manual_seed(1)

# Ex-1: 用torch.tensor创建张量

flag = 0
if flag:
    arr = np.ones((3, 3))
    print("Type of ndarry:", arr.dtype)

    # t = torch.tensor(arr, device='cuda')
    t = torch.tensor(arr)
    print(t)

# Ex-2: 用torch.from_numpy 创建张量

flag = 0
if flag:
    arr = np.array([[1, 2, 3], [4, 5, 6]])
    # t = torch.tensor(arr)
    t = torch.from_numpy(arr)
    print("numpy array: ", arr, "type: ", arr.dtype)
    print("torch tensor: ", t)

    print("Modify array:")
    arr[0, 0] = 0
    print("numpy array: ", arr)
    print("torch tensor: ", t)

    print("Modify tensor: ")
    t[0, 0] = -1
    print("numpy array: ", arr)
    print("torch tensor: ", t)


# Ex-3: torch.zeros
flag = 0
if flag:
    out_t = torch.tensor([1])
    t = torch.zeros((3, 3), out=out_t)
    # t = torch.zeros((3, 3))
    print(t, '\n', out_t)
    print(id(t), id(out_t), id(t) == id(out_t))


# Ex-4: torch.full

flag = 0
if flag:
    t = torch.full((3, 3), 1.0)
    print(t)

# Ex-5: torch.arrange

flag = 0
if flag:
    t = torch.arange(2, 10, 1.5)
    print(t)

# Ex-6: torch.linspace

flag = 0
if flag:
    t = torch.linspace(2, 10, 5)
    print(t)


# Ex-7 : torch.normal

flag = 0
if flag:
    # mean = torch.arange(1, 5, dtype=torch.float)
    # std = torch.arange(1, 5, dtype=torch.float)
    # t_normal = torch.normal(mean, std)
    # print("mean:{}\nstd:{}".format(mean, std))
    # print(t_normal)

    # t_normal = torch.normal(0., 1., size=(4, ))
    # print(t_normal)

    mean = torch.arange(1, 5, dtype=torch.float)
    std = 1
    t_normal = torch.normal(mean, std)
    print("mean: {}\n std: {}".format(std, mean))
    print(t_normal)
