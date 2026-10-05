<div align="center">

<img src="assets/avatar.png" alt="Reynolds Hu" width="132" />

# Reynolds Learning Archive

**学生时期的课程作业与个人项目归档**

<sub>浙江大学 · 罗格斯大学 · 约翰霍普金斯大学 · 课外自学</sub>

<br />

[![License](https://img.shields.io/badge/License-MIT-1a1a1a?style=flat-square)](LICENSE)
[![Projects](https://img.shields.io/badge/Projects-19-1a1a1a?style=flat-square)](#项目索引)
[![Datasets](https://img.shields.io/badge/Datasets-not_included-1a1a1a?style=flat-square)](#关于数据集)
[![Focus](https://img.shields.io/badge/Focus-ML_·_Robotics_·_Applied_Math-1a1a1a?style=flat-square)](#项目索引)

<br />

<sub><i>Code and approach only — no datasets, no trained weights.</i></sub>

</div>

---

## 这是什么

这里收的是我学生阶段做过的一批小项目：机器学习、深度学习、机器人学、应用数学、嵌入式，
横跨几所学校和几门课。代码水平参差不齐 —— 有些是课堂作业，有些是做到一半的个人项目。

**请按「学习记录」而不是「工程范例」来看待。**

<div align="center">

| ✅ 开源 | ❌ 不开源 | 🧹 已清理 |
|:---|:---|:---|
| 全部代码 | 数据集 | notebook 输出 |
| 算法思路 | 模型权重 | 绝对路径 |
| 实验设计 | 课程材料 | 他人用户名 |

</div>

> 数据集不在仓库里，**不是疏漏，是有意的**。每个受影响的项目目录下有 `DATA.md`，
> 说明需要什么数据、从哪获取、代码期望什么路径。

---

## 目录结构

```
reynold-learning-archive/
├── 01-jhu-ai-mini/               JHU · AI 小项目（Musad Haque 教授）
├── 02-jhu-deep-learning/         JHU · 深度学习（Vishal M. Patel 教授）
├── 03-jhu-dl-final/              JHU · 深度学习期末项目
├── 04-jhu-robotics/              JHU · 机器人学
├── 05-jhu-applied-math/          JHU · 应用数学计算（Daniel Q. Naiman 教授）
├── 06-rutgers-senior-design/     罗格斯大学 · 毕业设计
├── 07-coursera/                  Coursera 课程项目
└── 08-personal/                  课外个人项目
```

---

## 项目索引

### `01` · JHU AI 小项目

<sub>Instructor: Musad Haque, PhD</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`chess-playing-agent`](01-jhu-ai-mini/chess-playing-agent) | 国际象棋对弈 agent（搜索 + 评估函数） | Python · Jupyter |
| [`search-agents`](01-jhu-ai-mini/search-agents) | 搜索 agent：BFS 等图搜索算法 | Python · Jupyter |
| [`resilient-swarming`](01-jhu-ai-mini/resilient-swarming) | 基于 Boids 规则的弹性集群仿真 | **MATLAB** · Robotarium |

### `02` · JHU 深度学习

<sub>Instructor: Vishal M. Patel</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`perceptron-logistic-regression`](02-jhu-deep-learning/perceptron-logistic-regression) | 从零实现感知机与逻辑回归，MNIST 十分类 | PyTorch · NumPy |
| [`autoencoders`](02-jhu-deep-learning/autoencoders) | 自编码器做图像重建与去噪 | PyTorch · Jupyter |
| [`face-recognition`](02-jhu-deep-learning/face-recognition) | k-NN 及其他算法做人脸识别 | NumPy · Jupyter |
| [`fine-tuning`](02-jhu-deep-learning/fine-tuning) | 微调 AlexNet / VGG-16 于 LFW | PyTorch |

### `03` · JHU 深度学习期末

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`neural-networks-image-classification`](03-jhu-dl-final/neural-networks-image-classification) | CNN 分类 CIFAR-10，对比优化器与调度 | PyTorch · Jupyter |
| [`language-model-lyrics`](03-jhu-dl-final/language-model-lyrics) | 字符级 LSTM 语言模型 + 采样 | PyTorch · Jupyter |
| [`hand-gestures-recognition`](03-jhu-dl-final/hand-gestures-recognition) | MediaPipe 手部关键点手势识别（**数据自采**） | MediaPipe · PyTorch |

### `04` · JHU 机器人学

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`ur5-move-pick-place`](04-jhu-robotics/ur5-move-pick-place) | UR5 机械臂移动与抓放轨迹规划 | **MATLAB** · R-VIZ |
| [`orb-slam2`](04-jhu-robotics/orb-slam2) | ORB-SLAM2 相关（部分文件） | **C++** |

### `05` · JHU 应用数学计算

<sub>Instructor: Prof. Daniel Q. Naiman</sub>

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`bikeshare-data-analysis`](05-jhu-applied-math/bikeshare-data-analysis) | 共享单车行程时长影响因素分析 | pandas · Jupyter |
| [`python-in-applied-math`](05-jhu-applied-math/python-in-applied-math) | **8 个作业**：最小代价路径、订单簿模拟、随机微分方程、布朗运动、Nim 博弈… | NumPy · Jupyter |

### `06` · 罗格斯大学 · 毕业设计

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`low-cost-ventilator`](06-rutgers-senior-design/low-cost-ventilator) | 面向 COVID-19 患者的低成本呼吸机 | **Arduino** |

### `07` · Coursera

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`self-driving-vehicle-control`](07-coursera/self-driving-vehicle-control) | 自动驾驶横向控制 | Python |

### `08` · 课外个人项目

| 项目 | 内容 | 技术栈 |
|:---|:---|:---|
| [`haptic-hat`](08-personal/haptic-hat) | 为视障人士做的触觉避障帽 | **Arduino** |
| [`quadruped-robot-linkages`](08-personal/quadruped-robot-linkages) | 四足机器人连杆机构设计 | **MATLAB** |
| [`tripod-arms-robot`](08-personal/tripod-arms-robot) | 基于 Delta 3D 打印机的三臂抓取机器人 | **MATLAB** |

---

## 关于数据集

**本仓库不包含任何数据集、模型权重或课程提供的材料。** 每个需要的项目目录下有
`DATA.md` 说明获取方式。原因：

| 原因 | 例子 |
|:---|:---|
| 课程材料，版权归课程方 | 最小代价路径地形矩阵、订单簿模拟数据 |
| 第三方数据集许可 | Extended Yale Face Database B |
| 个人隐私 | 摄像头自采的手势数据 |

另外，所有 Jupyter notebook 的**输出单元格已清空**，代码中的**绝对路径已替换为
`<DATA_DIR>` 占位符**。

> 前者可能残留真实数据（base64 图像、数据行），后者会泄漏用户名 —— 包括协作者的。

---

## 合作者署名

以下项目是**小组作业**，成果属于全体成员：

| 项目 | 合作者 |
|:---|:---|
| `low-cost-ventilator` | Zhijing Hu · Travis B Thompson-Sevcik · Kevin J Donlan · Pik Luen Li · Prabhdeep Singh |
| `orb-slam2` | Zhijing Hu · Zhikun Gan |
| `hand-gestures-recognition` | Zhijing Hu · Zhikun Gan · Yifei Che |
| `tripod-arms-robot` | Zhijing Hu · Keqin Wang |

其余项目为个人独立完成。

---

## 许可

代码采用 [MIT License](LICENSE)。

但请注意：**部分项目是课程作业**，其中的算法框架与任务描述可能源自课程材料，
版权归原课程与授课教师所有。

> 如果你是这些课程的**在读同学** —— 请勿直接抄袭提交。
> 这个仓库的用途是让你看懂思路，而不是给你答案。

<div align="center">
<br />
<sub>Maintained by <a href="https://github.com/reynold-hu">Reynolds Hu</a></sub>
</div>
