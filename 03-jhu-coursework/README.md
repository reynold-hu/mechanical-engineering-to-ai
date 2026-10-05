# 03 · Johns Hopkins University（2021–2023）

> **Robotics 硕士（MSE in Robotics）** —— 我正式转过来的地方。
> 15 个项目，来自 6 门课。

---

## 课程索引

按**课号**排列。每个目录里有该课的作业，每份作业旁边都有 `NOTES.md` 原理讲解。

| 课号 | 课程名 | 我的目录 | 教授 | 项目数 |
|:---|:---|:---|:---|:---:|
| **EN.553.688** | Computing for Applied Mathematics | [`applied-math/`](applied-math/) | Daniel Q. Naiman | 1 |
| **EN.601.475** | Machine Learning | [`machine-learning/`](machine-learning/) | Mark Dredze | 1 |
| **EN.520.438** | Deep Learning | [`deep-learning/`](deep-learning/) | Vishal M. Patel | 4 |
| — | Deep Learning · 期末项目 | [`deep-learning-final/`](deep-learning-final/) | 同上 | 3 |
| **EN.530.646** | Robot Devices, Kinematics, Dynamics, and Control（**RDKDC**） | [`rdkdc/`](rdkdc/) | — | 1 |
| **EN.530.691** | Haptic Interface Design for Human-Robot Interaction | [`haptics/`](haptics/) | — | 1 |
| （课号不明） | Artificial Intelligence · 计算机系 | [`ai-fundamentals/`](ai-fundamentals/) | Musad Haque | 3 |

> **两个说明：**
> 1. `ai-fundamentals/` 的课号**查不到** —— 授课人 Musad Haque 是 **JHUAPL（应用物理实验室）**
>    的研究员，非常规教职，公开资料里没有课程编号。
> 2. `deep-learning/` 和 `deep-learning-final/` **是同一门课**（EN.520.438），
>    分开是因为前者是平时小作业、后者是期末项目。

---

## 这个阶段的目录结构

```
03-jhu-coursework/
├── ai-fundamentals/          AI 通识课
│   ├── chess-playing-agent/      minimax + α-β 剪枝
│   ├── search-agents/            BFS / DFS / 一致代价搜索
│   └── resilient-swarming/       Boids 集群（MATLAB + Robotarium）
├── applied-math/             应用数学计算
│   └── python-in-applied-math/   8 个作业（最短路径/订单簿/SDE…）
├── machine-learning/         机器学习
│   └── bikeshare-data-analysis/
├── deep-learning/            深度学习 · 平时作业
│   ├── perceptron-logistic-regression/   从零手写梯度下降
│   ├── autoencoders/
│   ├── face-recognition/
│   └── fine-tuning/
├── deep-learning-final/      深度学习 · 期末
│   ├── neural-networks-image-classification/   CNN / CIFAR-10
│   ├── language-model-lyrics/                  LSTM 字符级语言模型
│   └── hand-gestures-recognition/              MediaPipe + 自采数据
├── rdkdc/                    机械臂运动学与控制
│   └── ur5-move-pick-place/      逆解 / 速率控制 / 梯度控制
└── haptics/                  触觉人机交互
    └── haptic-hat/               视障避障帽（Arduino）
```

---

## 这个阶段对我的意义

**这是「机械工程 → Robotics」真正发生的地方。**

我在 [`LEARNING-PATH.md`](../LEARNING-PATH.md) 里写了那张工科知识映射表 ——
**这个阶段就是它的验证**：

| 我本科有的 | 在 JHU 直接变现的地方 |
|:---|:---|
| 线性代数、微积分 | EN.553.688（应用数学）几乎没补数学 |
| 动力学、运动学 | EN.530.646（RDKDC）—— 运动学和雅可比我本科学过一半 |
| 反馈控制、机电一体化 | EN.530.691（Haptics）—— **课程推荐背景写的就是"动力学、反馈控制、机电一体化、MATLAB"** |
| MATLAB / 数值计算 | 多个项目直接用 MATLAB |

**但缺口也很清楚：** 编程工程化（Python 生态、软件设计）、CS 核心课（算法/数据结构）。
这就是 EN.553.688 和 EN.601.475 补的东西。
