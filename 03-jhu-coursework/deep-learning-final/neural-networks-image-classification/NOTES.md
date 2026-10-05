# 原理讲解：CNN 与 CIFAR-10

> 这个作业教**「卷积到底在做什么」**，以及**「怎么把模型调好」**。

---

## 一、数据集：CIFAR-10

- **6 万张 32×32 彩色图**，10 类（飞机/汽车/鸟/猫/鹿/狗/青蛙/马/船/卡车）
- 比 MNIST 难得多 —— **MNIST 上随便一个模型都 99%，CIFAR-10 上 90% 都算不错**

**为什么难？** 32×32 分辨率下，猫和狗的差别只有几个像素。
而且同一个类内部差异极大（猫有各种姿态、颜色、角度）。

---

## 二、卷积：三个关键性质

### ① 局部连接

**全连接层的问题：** 32×32×3 的图接到 1024 维隐藏层，
参数量 = 3072 × 1024 ≈ **300 万**。

**卷积的解法：** 每个神经元只看**一个小窗口**（比如 3×3）。

**依据：** 图像中相邻像素高度相关，远处像素的关联可以后面再组合。

### ② 权重共享

**同一个卷积核在整张图上滑动。**

**依据：** 「猫耳朵」这个模式，出现在图左上角和右下角，**检测方式应该一样** ——
这叫**平移不变性**。

**效果：** 3×3×3 的卷积核只有 27 个参数，不是 300 万。

### ③ 层次化

```
Conv1  → 边缘、颜色
Conv2  → 纹理、简单形状
Conv3  → 部件（眼睛、轮子）
Conv4+ → 物体
```

**每一层在前一层的输出上再卷积，感受野逐层扩大。**

---

## 三、关键组件

```python
nn.Conv2d(3, 32, kernel_size=3, padding=1)   # 卷积：提特征
nn.BatchNorm2d(32)                            # 批归一化：稳定训练
nn.ReLU()                                     # 激活：引入非线性
nn.MaxPool2d(2)                               # 池化：降分辨率
nn.Dropout(0.5)                               # 随机丢弃：防过拟合
```

**各自的角色：**

| 组件 | 作用 | 为什么需要 |
|:---|:---|:---|
| **Conv** | 提取局部特征 | 利用图像的空间结构 |
| **BatchNorm** | 归一化每层输入 | 让训练更稳、能用更大学习率 |
| **ReLU** | `max(0,x)` | 非线性，且梯度不消失（相比 sigmoid） |
| **Pooling** | 降采样 | 减少计算量，增大感受野 |
| **Dropout** | 训练时随机置零 | 防过拟合 |

---

## 四、作业的重点：优化器与调度

这个作业的题目明确说 *"Applied different optimizers, learning rate scheduling
and try different architectures"* —— **重点是「怎么调」，不是「调出什么」。**

### 优化器对比

| 优化器 | 思想 | 特点 |
|:---|:---|:---|
| **SGD** | 沿梯度走 | 简单，但慢、对学习率敏感 |
| **SGD + Momentum** | 加「惯性」 | 冲过局部最小值和小坑 |
| **RMSProp** | 按梯度平方的滑动平均缩放 | 每个参数自适应 |
| **Adam** | Momentum + RMSProp | **默认首选**，收敛快 |

**Momentum 的直觉：** 像小球滚下山 —— 有惯性，不会在坡上的小坑里卡住。

```python
v = beta * v + (1-beta) * grad      # 速度累积
w = w - lr * v                       # 用速度而不是梯度更新
```

### 学习率调度

**核心矛盾：** 训练初期要大学习率（快速下降），后期要小（精细收敛）。

| 调度策略 | 做法 |
|:---|:---|
| **StepLR** | 每 N 轮学习率 × 0.1 |
| **CosineAnnealing** | 按余弦曲线平滑衰减 |
| **OneCycleLR** | 先升后降（近年流行） |
| **ReduceLROnPlateau** | 指标不降了就降学习率 |

```python
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
```

---

## 五、自己动手

```python
# 1. 跑通 Cifar_10_main.ipynb，看基线

# 2. 优化器对比实验（这个作业的核心）
for opt in ['SGD', 'SGD+Momentum', 'RMSProp', 'Adam']:
    # 同样的网络、同样的 epoch 数，画 loss 曲线对比

# 3. 学习率调度对比
#    固定 LR vs StepLR vs Cosine —— 看最终准确率

# 4. 数据增强（提升最明显的一招）
transform = transforms.Compose([
    transforms.RandomCrop(32, padding=4),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
])
```

**建议的改进方向：**
- **数据增强** —— CIFAR-10 上最有效的提升手段
- **残差连接** —— 换 ResNet-18，准确率立刻上 95%
- **标签平滑** —— 防止模型过度自信
- **集成** —— 训几个模型投票

> 📚 **深入方向**：ResNet、数据增强（AutoAugment）、知识蒸馏、Vision Transformer
