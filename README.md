<div align="center">

<img src="assets/avatar.png" alt="Reynold Hu" width="132" />

# Reynold Learning Archive

**一个机械工程师转 CS / Robotics 的真实轨迹**

<sub>Rutgers 机械工程本科 → 浙大暑校 → JHU Robotics 硕士 → ?</sub>

<br />

[![License](https://img.shields.io/badge/License-MIT-1a1a1a?style=flat-square)](LICENSE)
[![Milestones](https://img.shields.io/badge/Milestones-18-1a1a1a?style=flat-square)](#路线总览)
[![Datasets](https://img.shields.io/badge/Datasets-not_included-1a1a1a?style=flat-square)](#关于数据集)
[![Path](https://img.shields.io/badge/%E5%AD%A6%E4%B9%A0%E8%B7%AF%E7%BA%BF-LEARNING--PATH.md-1a1a1a?style=flat-square)](LEARNING-PATH.md)

<br />

<sub><i>Not a portfolio. A trail of evidence — for people walking the same road.</i></sub>

</div>

---

## 这不是作品集，是一条路

市面上不缺「怎么学 CS」的指南。[csdiy.wiki](https://csdiy.wiki/)（68.6k ⭐）已经把零基础路线写得很好：

```
CS50 → CS61A → CS61B + LeetCode → 方向选修
```

**但它假设你从零开始。如果你是机械、土木、化工、EE 出身 —— 你不是。**

我叫 Reynold，本科机械工程，后来转到 Robotics。这个仓库是我 **2017–2023** 走过的每一个里程碑，
连**做得不完整的部分一起**放出来。

> **👉 路线本身写在 [`LEARNING-PATH.md`](LEARNING-PATH.md)**
> —— 包括一张「**你已有的工科知识怎么接到 CS 上**」的映射表，那是这份资料里最值钱的部分。

---

## 路线总览

| 阶段 | 时期 | 内容 | 里程碑 |
|:---|:---|:---|:---:|
| **01** | 2017–2021 | **机械工程本科** @ Rutgers | 2 |
| **02** | 2018 夏 | **浙大暑校** —— 第一次用代码解决工程问题 | 1 |
| **03** | 2021–2023 | **Robotics 硕士** @ JHU —— 正式入场 | 13 |
| **04** | — | JHU 课外项目 | 1 |
| **05** | — | Coursera | 1 |

```
reynold-learning-archive/
├── LEARNING-PATH.md          ⭐ 路线主文档（从这里开始）
├── 01-rutgers-mechanical/    机械本科 —— 起点
├── 02-zju-summer-2018/       浙大暑校
├── 03-jhu-coursework/        JHU 课程（按课号分组）
│   ├── applied-math/         EN.553.688
│   ├── machine-learning/     EN.601.475
│   ├── deep-learning/        EN.520.438
│   ├── deep-learning-final/  期末项目
│   ├── ai-fundamentals/      计算机系 AI 课
│   ├── rdkdc/                EN.530.646
│   └── haptics/              EN.530.691
└── 04-coursera/
```

---

## 里程碑清单

### 01 · 机械工程本科 <sub>Rutgers, 2017–2021</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`low-cost-ventilator`](01-rutgers-mechanical/low-cost-ventilator) | 面向 COVID-19 患者的低成本呼吸机（毕业设计） | **Arduino** |
| [`quadruped-robot-linkages`](01-rutgers-mechanical/quadruped-robot-linkages) | 四足机器人连杆机构设计 | **MATLAB** |

<sub>🟡 这两个几乎没有代码，是纯机械设计。**起点就是这样。**</sub>

### 02 · 浙江大学暑期学习 <sub>2018</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`tripod-arms-robot`](02-zju-summer-2018/tripod-arms-robot) | 基于 Delta 3D 打印机的三臂抓取机器人 | **MATLAB** |

### 03 · JHU Robotics 硕士课程 <sub>2021–2023</sub>

**应用数学** <sub>EN.553.688 · Daniel Q. Naiman</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`python-in-applied-math`](03-jhu-coursework/applied-math/python-in-applied-math) | **8 个作业**：最小代价路径、订单簿模拟、随机微分方程、布朗运动、Nim 博弈 | NumPy · Jupyter |

**机器学习** <sub>EN.601.475 · Mark Dredze ｜ [课程网站](https://www.cs475.org/)公开</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`bikeshare-data-analysis`](03-jhu-coursework/machine-learning/bikeshare-data-analysis) | 共享单车行程时长影响因素分析 | pandas |

**深度学习** <sub>EN.520.438 · ECE · Vishal M. Patel</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`perceptron-logistic-regression`](03-jhu-coursework/deep-learning/perceptron-logistic-regression) | 从零实现感知机与逻辑回归，MNIST 分类 | PyTorch · NumPy |
| [`autoencoders`](03-jhu-coursework/deep-learning/autoencoders) | 自编码器做图像重建与去噪 | PyTorch |
| [`face-recognition`](03-jhu-coursework/deep-learning/face-recognition) | k-NN 及其他算法做人脸识别 | NumPy |
| [`fine-tuning`](03-jhu-coursework/deep-learning/fine-tuning) | 微调 AlexNet / VGG-16 于 LFW | PyTorch |

**深度学习期末**

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`neural-networks-image-classification`](03-jhu-coursework/deep-learning-final/neural-networks-image-classification) | CNN 分类 CIFAR-10，对比优化器与调度 | PyTorch |
| [`language-model-lyrics`](03-jhu-coursework/deep-learning-final/language-model-lyrics) | 字符级 LSTM 语言模型 + 采样 | PyTorch |
| [`hand-gestures-recognition`](03-jhu-coursework/deep-learning-final/hand-gestures-recognition) | MediaPipe 手势识别（**数据自采**） | MediaPipe · PyTorch |

**AI 基础** <sub>计算机系 · Musad Haque</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`chess-playing-agent`](03-jhu-coursework/ai-fundamentals/chess-playing-agent) | 国际象棋对弈 agent | Python |
| [`search-agents`](03-jhu-coursework/ai-fundamentals/search-agents) | BFS 等图搜索算法 | Python |
| [`resilient-swarming`](03-jhu-coursework/ai-fundamentals/resilient-swarming) | Boids 集群仿真 | **MATLAB** · Robotarium |

**机器人学** <sub>EN.530.646 · RDKDC ｜ [课程目录](https://e-catalogue.jhu.edu/course-descriptions/robotics/)</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`ur5-move-pick-place`](03-jhu-coursework/rdkdc/ur5-move-pick-place) | UR5 机械臂移动与抓放轨迹规划 | **MATLAB** · R-VIZ |

**触觉与人机交互** <sub>EN.530.691 · Haptic Interface Design</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`haptic-hat`](03-jhu-coursework/haptics/haptic-hat) | 为视障人士做的触觉避障帽 | **Arduino** |

### 04 · Coursera

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`self-driving-vehicle-control`](04-coursera/self-driving-vehicle-control) | 自动驾驶横向控制 | Python |

---

## 关于数据集

**本仓库不包含任何数据集、模型权重或课程提供的材料。** 每个需要的项目目录下有
`DATA.md` 说明获取方式 —— 原因包括课程材料授权、第三方数据集许可、以及自采数据中的个人隐私。

所有 Jupyter notebook 的**输出单元格已清空**，代码中的**绝对路径已替换为 `<DATA_DIR>` 占位符**。

---

## 合作者署名

以下项目是**小组作业**，成果属于全体成员：

| 项目 | 合作者 |
|:---|:---|
| `low-cost-ventilator` | Reynold Hu · Travis T-S. · Kevin D. · Pik Luen L. · Prabhdeep S. |
| `hand-gestures-recognition` | Reynold Hu · Zhikun G. · Yifei C. |
| `tripod-arms-robot` | Reynold Hu · Keqin W. |

---

## 完成度

**这个仓库里的项目不是都做完了** —— 每个项目 README 顶部有标注：

| 徽章 | 含义 | 数量 |
|:---:|:---|:---:|
| 🟢 | 完成 | 12 |
| 🟡 | 部分完成（README 里写明卡在哪） | 6 |
| 🔴 | 草稿 | 0 |

> **未完成不是缺陷，是这条路的真实样子。** 每个 🟡 项目都写了「当时卡在哪」和「想接着做需要补什么」。

---

## 许可

代码采用 [MIT License](LICENSE)。请注意：**部分项目是课程作业**，其中的算法框架与任务描述
可能源自课程材料，版权归原课程与授课教师所有。

### 引入的第三方代码

`02-zju-summer-2018/tripod-arms-robot/reference/` 下有两份**第三方 MIT 许可代码**，
用于补全该项目缺失的 Delta 机构逆运动学。各自的 `LICENSE` 文件与原作者署名**已保留**：

| 来源 | 作者 | 许可 |
|:---|:---|:---|
| [12343954/Rotary-Delta-Robot-Kinematics](https://github.com/12343954/Rotary-Delta-Robot-Kinematics) | Cooloo AI | MIT |
| [wiesnerroyal/delta-robot](https://github.com/wiesnerroyal/delta-robot) | wiesnerroyal | MIT |

> **为什么只有这一个项目引入了外部代码？** 因为它是唯一一个我确认真有明确缺口、
> 且能找到**许可证兼容**实现的项目。Delta 运动学最流行的开源库
> （`tinkersprojects/Delta-Kinematics-Library`，53 ⭐）是 **GPL-3.0** ——
> 引入会导致整个仓库被迫改许可，所以放弃。详见
> [`reference/README.md`](02-zju-summer-2018/tripod-arms-robot/reference/README.md)。

> **如果你正在上这些课 —— 请勿直接抄袭提交。**
> 这个仓库的用途是让你看懂思路，以及看清楚**一条真实的路长什么样**。

<div align="center">
<br />
<sub>学生时代的终点，不是终点 —— <a href="https://github.com/reynold-hu">@reynold-hu</a></sub>
</div>
