# 从机械工程到 CS：一条没人写过的路线

> 这不是给零基础的人看的。
> 这是给**已经有工科背景、想转 CS / Robotics** 的人看的。

---

## 为什么需要单独一条路线

现在最权威的 CS 自学指南是 [csdiy.wiki](https://csdiy.wiki/)（**68.6k stars**），
它给出的零基础路线是：

```
Crash Course 科普 → 哈佛 CS50 → 伯克利 CS61A → CS61B + LeetCode → 方向选修
```

**它假设你从零开始。**

但如果你是机械、土木、化工、EE 出身，你**不是从零开始** —— 你手上已经有一半的资产，
只是没人告诉你这些资产怎么接上去。

> 我搜遍了这个领域的资料，明确写着「**未涉及如何从机械工程专业切入的具体衔接建议**」。
>
> **这个缺口就是这份文档存在的理由。**

---

## 你已经有的一半资产

这是这份文档最有价值的部分。**不要从零开始学，先看看你已经会什么。**

| 你已有的（机械/工科） | 直接对应 CS / Robotics | 意味着什么 |
|:---|:---|:---|
| 微积分、线性代数、常微分方程 | **ML 的数学基础**、优化、概率 | 🔥 **不用重修** —— 纯文商科转码者要补一两年 |
| 理论力学、动力学 | 机器人动力学、状态估计、控制理论 | 直接能读控制类论文 |
| 运动学（连杆、自由度、位姿） | 正/逆运动学、SE(3)、DH 参数 | 可以直接上机器人学研究生课 |
| 数值方法、有限元 | 数值优化、仿真、微分方程数值解 | 优化器对你不是新概念 |
| MATLAB / Simulink | **编程思维已起步** | 转 Python 是换语法，不是从零学编程 |
| 实验设计、误差分析、测量不确定度 | 实验方法论、模型评估、置信区间 | 做 ML 实验时直接迁移 |
| CAD、几何建模、点云 | 计算机图形学、SLAM 的几何部分、视觉 | 空间直觉是你的优势 |

**结论：你的缺口主要在「编程工程化」和「CS 核心课」，不在数学。**

---

## 路线

下面这条路是**我自己走过的**（2017–2023），每个阶段标注：

- 🏁 **里程碑** —— 我在那个阶段做出来的东西（都在这个仓库里）
- 📚 **对应开源资源** —— 你可以拿来替代或补充的公开课程

### 阶段 0 · 机械工程本科

**Rutgers University, 2017–2021**

这个阶段你不需要学 CS。你需要的是**把工科的数学和力学基础打扎实** —— 它们后来全都成了资产。

- 🏁 [`low-cost-ventilator`](01-rutgers-mechanical/low-cost-ventilator) —— 本科毕业设计，低成本呼吸机（机械 + Arduino）
- 🏁 [`quadruped-robot-linkages`](01-rutgers-mechanical/quadruped-robot-linkages) —— 四足机器人连杆机构设计

> **诚实说明**：这两个项目**几乎没有代码**，是纯机械设计。这很正常 —— **起点就是这样，不必自卑。**

### 阶段 1 · 第一次跨出去

**浙江大学暑期学习, 2018**

转折点是「开始用代码解决工程问题」。

- 🏁 [`tripod-arms-robot`](02-zju-summer-2018/tripod-arms-robot) —— 基于 Delta 3D 打印机的三臂抓取机器人（MATLAB 运动学）

📚 **同时补编程基础：**
- [MIT Missing Semester](https://missing.csail.mit.edu/) —— 命令行、Git、Shell 脚本。**10 小时，工科生必看**
- [哈佛 CS50](https://cs50.harvard.edu/x/) —— 编程入门，讲得极好

### 阶段 2 · 正式入场：Robotics 硕士

**Johns Hopkins University, 2021–2023**

这是我真正转过来的地方。JHU 的 Robotics MSE 核心课是：

| 课程 | 编号 | 内容 |
|:---|:---|:---|
| Algorithms for Sensor-Based Robotics | `EN.601.663` | 运动规划、定位与建图，ROS 环境 |
| **RDKDC** | `EN.530.646` | 刚体运动、正逆运动学、轨迹生成、机械臂动力学与控制 |

#### 2.1 应用数学计算

📚 [Computing for Applied Mathematics](https://e-catalogue.jhu.edu/) — JHU `EN.553.688`（Daniel Q. Naiman）
- 🏁 [`python-in-applied-math`](03-jhu-coursework/applied-math/python-in-applied-math) —— 8 个作业：最小代价路径、订单簿模拟、随机微分方程、布朗运动、Nim 博弈

> **这一门课把我从 MATLAB 思维转成了 Python 工程思维。**

#### 2.2 机器学习

📚 [JHU Machine Learning](https://www.cs475.org/) — `EN.601.475`（Mark Dredze）· **课程网站公开可访问**
- 🏁 [`bikeshare-data-analysis`](03-jhu-coursework/machine-learning/bikeshare-data-analysis) —— 共享单车行程时长影响因素分析

#### 2.3 深度学习

📚 JHU Deep Learning — `EN.520.438`（ECE 开设，**Vishal M. Patel** 授课）
- 🏁 [`perceptron-logistic-regression`](03-jhu-coursework/deep-learning/perceptron-logistic-regression) —— 从零实现感知机与逻辑回归
- 🏁 [`autoencoders`](03-jhu-coursework/deep-learning/autoencoders) —— 图像重建与去噪
- 🏁 [`face-recognition`](03-jhu-coursework/deep-learning/face-recognition) —— k-NN 人脸识别
- 🏁 [`fine-tuning`](03-jhu-coursework/deep-learning/fine-tuning) —— 微调 AlexNet / VGG-16

#### 2.4 AI 基础

📚 JHU 计算机系 Musad Haque 的 AI 课
- 🏁 [`chess-playing-agent`](03-jhu-coursework/ai-fundamentals/chess-playing-agent) —— 国际象棋对弈 agent
- 🏁 [`search-agents`](03-jhu-coursework/ai-fundamentals/search-agents) —— BFS 等图搜索
- 🏁 [`resilient-swarming`](03-jhu-coursework/ai-fundamentals/resilient-swarming) —— Boids 集群仿真（MATLAB + Robotarium）

#### 2.5 机器人学

📚 JHU **RDKDC** `EN.530.646` — [课程目录](https://e-catalogue.jhu.edu/course-descriptions/robotics/)
- 🏁 [`ur5-move-pick-place`](03-jhu-coursework/rdkdc/ur5-move-pick-place) —— UR5 机械臂移动与抓放

> **这门课是我机械背景直接变现的地方** —— 运动学、雅可比、轨迹规划，我本科学过一半。

#### 2.6 触觉与人机交互

📚 **Haptic Interface Design for Human-Robot Interaction** — JHU `EN.530.691`（机械系）
- 🏁 [`haptic-hat`](03-jhu-coursework/haptics/haptic-hat) —— 为视障人士做的触觉避障帽

> 这门课的推荐背景写的是「动力学、反馈控制、机电一体化、MATLAB」——
> **几乎就是我本科机械专业的课程表。** 这是转专业的人最容易忽略的优势：
> 有些研究生课，你的本科基础比 CS 出身的人还硬。

### 阶段 3 · 深度学习进阶

- 🏁 [`neural-networks-image-classification`](03-jhu-coursework/deep-learning-final/neural-networks-image-classification) —— CNN 分类 CIFAR-10
- 🏁 [`language-model-lyrics`](03-jhu-coursework/deep-learning-final/language-model-lyrics) —— 字符级 LSTM 语言模型
- 🏁 [`hand-gestures-recognition`](03-jhu-coursework/deep-learning-final/hand-gestures-recognition) —— MediaPipe 手势识别（**数据自采**）

📚 补充：
- [Stanford CS231n](http://cs231n.stanford.edu/) —— 视觉与 CNN（公认最好的 CV 课）
- [Stanford CS224n](http://web.stanford.edu/class/cs224n/) —— NLP 与 LSTM

### 阶段 4 · 硬件与嵌入式的另一条线

- 🏁 [`haptic-hat`](03-jhu-coursework/haptics/haptic-hat) —— 为视障人士做的触觉避障帽（Arduino）

📚 [Nand2Tetris](https://www.nand2tetris.org/) —— 从门电路造一台计算机，理解硬件到软件的桥

### 旁支 · Coursera

- 🏁 [`self-driving-vehicle-control`](04-coursera/self-driving-vehicle-control) —— 自动驾驶横向控制

---

## 这条路之后

**这个仓库到 2023 年为止 —— 它是我学生时代的终点，不是我的终点。**

如果你也在走这条路，几点来自我的经验：

1. **数学别重修。** 你已经会了，去学编程工程化和 CS 核心课（数据结构、算法、操作系统）。
2. **项目比课程重要。** 简历上写「实现了一个 Scheme 解释器」比「学完了 CS61A」有用一百倍。
3. **机械背景是优势，不是包袱。** 做 Robotics / 具身智能 / 仿真的人，最缺的就是你这个背景。
4. **别停在学生时代。** 我这些项目大部分不完整，**这没关系** —— 关键是你得往前走。现在这个时代，agent、具身智能、世界模型，都是工科背景能直接切入的方向。

---

## 开源资源汇总

| 资源 | 用途 | 费用 |
|:---|:---|:---|
| [csdiy.wiki](https://csdiy.wiki/) | 最全的 CS 自学路线（68.6k ⭐） | 免费 |
| [MIT Missing Semester](https://missing.csail.mit.edu/) | 命令行 / Git / Shell —— **工科生第一课** | 免费 |
| [哈佛 CS50](https://cs50.harvard.edu/x/) | 编程入门 | 免费 |
| [Nand2Tetris](https://www.nand2tetris.org/) | 硬件到软件的全栈理解 | 免费 |
| [JHU EN.601.475 ML](https://www.cs475.org/) | 机器学习（课程网站公开） | 免费 |
| [JHU EN.601.465 NLP](https://www.cs.jhu.edu/~jason/465/) | 自然语言处理（syllabus 公开） | 免费 |
| [Stanford CS231n](http://cs231n.stanford.edu/) | 计算机视觉 | 免费 |
| [Stanford CS224n](http://web.stanford.edu/class/cs224n/) | NLP | 免费 |

> 链接均为**逐个验证可访问**（2026-10 检查）。JHU 的 `ams.jhu.edu` 和 `lcsr.jhu.edu` 会拦截脚本访问，
> 浏览器打开通常正常，故未列入上表。
