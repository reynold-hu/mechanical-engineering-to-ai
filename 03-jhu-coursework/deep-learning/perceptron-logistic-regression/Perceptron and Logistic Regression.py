import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from dataset import MNIST
from torchvision import transforms
import numpy as np

class LogisticRegression(torch.nn.Module):
    def __init__(self, input_dim, output_dim):
        super(LogisticRegression, self).__init__()
        self.linear = torch.nn.Linear(input_dim, output_dim)

    def forward(self, x):
        outputs = self.linear(x)
        return outputs

def clsDigitModel(digit):
    batch_size = 64
    learning_rate = 0.002
    epochs = 1

    train_loader = torch.utils.data.DataLoader(
        MNIST(target_label=digit, train=True, transform=transforms.ToTensor()),
        batch_size=batch_size, shuffle=True)

    test_loader = torch.utils.data.DataLoader(
        MNIST(target_label=digit, train=False, transform=transforms.ToTensor()),
        batch_size=batch_size, shuffle=False)

    ## set the bias is 1
    w1, b1 = torch.randn(1, 784, requires_grad=True), torch.ones(1, requires_grad=True)
    torch.nn.init.kaiming_normal_(w1)
    
    ## A Simple Single Layer Perceptron Model
    def forward(x):
        x = x@w1.t() + b1
        return x

    optimizer = optim.SGD([w1, b1], lr=learning_rate)
    criteon = nn.BCEWithLogitsLoss()

    for epoch in range(epochs):
        for batch_idx, (data, target) in enumerate(train_loader):
            data = data.view(-1, 28 * 28)
            out = forward(data)
            out = out.squeeze(dim=-1)
            targetT = target.float()
            loss = criteon(out, targetT)
            optimizer.zero_grad()
            loss.backward()
            optimizer.step()
            if epoch % 2 == 0 and batch_idx % 200 == 0 and 0:
                print('epochs : {} [{}/{} ({:.0f}%)]\tLoss: {:.6f}'.format(epoch, batch_idx * len(data), len(train_loader.dataset), \
                    100. * batch_idx / len(train_loader), loss.item()))

    test_loss = 0
    correct = 0
    sample_size = 0
    pred_lists = []
    label_lists = []
    #label_1_cnt = 0
    #pred_1_cnt = 0
    for data, target in test_loader:
        data = data.view(-1, 28 * 28)
        logits = forward(data)
        logits = logits.squeeze(dim=-1)
        targetT = target.float()

        logits_arr = logits.data.numpy()
        target_arr = target.data.numpy()
        pred_lists.extend(logits_arr)
        label_lists.extend(target_arr)

        pred_arr = np.where(logits_arr >= 0.5, 1, 0)
        correct += np.sum(np.equal(pred_arr, target_arr))
        #label_1_cnt += len(np.where(target_arr == 1)[0])
        #pred_1_cnt += len(np.where(pred_arr == 1))
        sample_size += len(data)

    acc = correct * 1.0 / sample_size
    print(digit, correct, sample_size, acc)
    #print(digit, correct, sample_size, acc, label_1_cnt, pred_1_cnt, pred_1_cnt * 1.0 / label_1_cnt)
    return pred_lists, label_lists


if __name__ == '__main__':
    pred_all = []
    label_all = []
    for cur_digit in range(10):
        pred_lists, label_lists = clsDigitModel(cur_digit)
        pred_all.append(pred_lists)
        label_all.append(label_lists)
    label_arr = np.array(label_all)
    pred_arr = np.array(pred_all)
    #print(label_arr.shape)
    #print(pred_arr.shape)
    ## get the overall test accuracy
    gt = np.argmax(label_arr, axis=0)
    pred = np.argmax(pred_arr, axis=0)
    #print(gt.shape, pred.shape)
    correct = np.sum(np.equal(pred, gt))
    print(correct, correct * 1.0 / gt.shape[0])
