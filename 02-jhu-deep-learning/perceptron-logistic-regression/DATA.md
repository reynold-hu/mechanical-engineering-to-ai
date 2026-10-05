# 数据集说明

本仓库**不包含数据集**。运行代码前请自行获取。

## 需要的数据

MNIST 手写数字数据集，共 4 个文件：

| 文件 | 内容 |
|---|---|
| `train-images-idx3-ubyte.gz` | 60,000 张训练图像 |
| `train-labels-idx1-ubyte.gz` | 训练标签 |
| `t10k-images-idx3-ubyte.gz` | 10,000 张测试图像 |
| `t10k-labels-idx1-ubyte.gz` | 测试标签 |

## 获取方式

**方式一：官方源**

```bash
# 官方镜像（Yann LeCun）
curl -O http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
curl -O http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
curl -O http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
curl -O http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
```

**方式二：走 torchvision（推荐，代码里已经用了）**

本项目的 `dataset.py` 继承自 `torchvision.datasets.mnist`，会自动下载并缓存：

```python
from torchvision import datasets
datasets.MNIST(root='./data', train=True, download=True)
```

## 代码期望的路径

把 4 个 `.gz` 文件放在本项目根目录，或改用上面的 torchvision 自动下载方式。
