import torch
import matplotlib.pyplot as plt
torch.manual_seed(1)

lr = 0.01

x = torch.rand(20, 1) * 10
y = 2 * x + 5 + torch.randn(20, 1)

w = torch.randn((1), requires_grad=True)
b = torch.randn((1), requires_grad=True)

for iteration in range(1000):

    # forward
    wx = torch.mul(w, x)
    y_pred = torch.add(wx, b)

    # compute MSE loss
    loss = 0.5*((y-y_pred)**2).mean()

    # backward
    loss.backward()

    # update para.
    w.data.sub_(lr * w.grad)
    b.data.sub_(lr * b.grad)

    # clear the grad
    w.grad.zero_()
    b.grad.zero_()

    # plot
    if iteration % 20 == 0:
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), y_pred.data.numpy(), 'r-', lw=2)
        # plt.text(2, 20, "Loss=%.4f" % loss.data.numpy(), fontdict={'size': 10, 'color': 'red'})
        print("Loss of Iteration-{}: {}".format(iteration, loss.data.numpy()))
        plt.xlim(1.5, 10)
        plt.ylim(8, 28)
        plt.title("Iteration: {} \nw:{} b:{} loss: {}".format(iteration, w.data.numpy(),
                                                              b.data.numpy(), loss.data.numpy()))
        plt.pause(0.5)

        if loss.data.numpy() < 1:
            break


