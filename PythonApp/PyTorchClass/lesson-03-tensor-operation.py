import torch
torch.manual_seed(1)

# Ex-1: torch.cat

flag = 0
if flag:
    t = torch.ones((2, 3))
    t_0 = torch.cat([t, t], dim=0)
    t_1 = torch.cat([t, t, t], dim=1)
    print("t_0:{} shape:{}\nt_1:{} shape:{}".format(t_0, t_0.shape, t_1, t_1.shape))


# Ex-2: torch.stack
flag = 0
if flag:
    t = torch.ones((2, 3))
    t_stack = torch.stack([t, t, t], dim=0)
    print("t_stack:{} shape:{}".format(t_stack, t_stack.shape))


# Ex-3: torch.chunk

flag = 0
if flag:
    a = torch.ones((2, 7))
    list_of_tensors = torch.chunk(a, dim=1, chunks=3)

    for idx, t in enumerate(list_of_tensors):
        print("Tensor-{}:{}, shape is {}".format(idx+1, t, t.shape))



# Ex-4: torch.split

flag = 0
if flag:
    t = torch.ones((2, 5))

    list_of_tensors = torch.split(t, [2, 1, 2], dim=1)
    for idx, t in enumerate(list_of_tensors):
        print("Tensor-{}: {}, shape is {}".format(idx+1, t, t.shape))


# Ex-5: torch.index_select

flag = 0
if flag:
    t = torch.randint(0, 9, size=(3, 3))
    idx = torch.tensor([0, 2], dtype=torch.long)
    t_select = torch.index_select(t, dim=0, index=idx)
    print("t:\n{}\nt_select:\n{}".format(t, t_select))


# Ex-6: torch.masked_select
flag = 0
if flag:
    t = torch.randint(0, 9, size=(3,3))
    mask = t.le(5)
    t_select = torch.masked_select(t, mask)
    print("t:\n{}\nt_select:\n{}".format(t, t_select))

# Ex-7: torch.reshape
flag = 0
if flag:
    t = torch.randperm(8)
    t_reshape = torch.reshape(t, (-1, 2, 2,))
    print("t:{}\nt_reshape:{}".format(t, t_reshape))

    t[0] = 1024
    print("t:{}\nt_reshape:{}".format(t, t_reshape))
    print("Memory of t.data: {}".format(id(t.data)))
    print("Memory of t_reshape.data: {}".format(id(t_reshape)))


# Ex-8: torch.transpose
flag = 0
if flag:
    t = torch.rand((2, 3, 4))
    t_transpose = torch.transpose(t, dim0=1, dim1=2) # c*h*w, h*w*c
    print("Shape of t: {}\n t_transpose: {}".format(t.shape, t_transpose.shape))


# Ex-9: torch.squeeze
flag = 0
if flag:
    t = torch.rand((1, 2, 3, 1))
    t_sq = torch.squeeze(t)
    t_0 = torch.squeeze(t, dim=0)
    t_1 = torch.squeeze(t, dim=1)
    print(t.shape)
    print(t_sq.shape)
    print(t_0.shape)
    print(t_1.shape)


# Ex-9: torch.squeeze
flag = 1
if flag:
    t_0 = torch.randn((3, 3))
    t_1 = torch.ones_like(t_0)
    t_add = torch.add(t_0, t_1)
    print("t_0:\n{}\nt_1:\n{}\nt_add:\n{}".format(t_0, t_1, t_add))