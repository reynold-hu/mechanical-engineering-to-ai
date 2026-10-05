# 02 · 浙江大学暑期学习（2018）

> **第一次用代码解决工程问题。**
> 时间上它在 Rutgers 本科期间（2018 年暑假），但在路径上是独立的转折点。

---

## 项目

| 项目 | 内容 | 技术栈 | 完成度 |
|:---|:---|:---|:---:|
| [`tripod-arms-robot`](tripod-arms-robot/) | 基于 Delta 3D 打印机的三臂抓取机器人 | **Arduino** · MATLAB | 🟡 |

- **导师**：Prof. Senyang W.
- **组员**：Reynold Hu、Keqin W.

---

## 我做了什么，没做什么

**做完了的：** `Gcode_interpreter CN.ino` —— **手写的 G-code 解析器**（52 行）。
一个状态机，解析 `G` / `X` / `F` 三个参数。**没有用 GRBL 之类的现成库。**

**没做的：逆运动学。** 机器能解析"移动到哪里"，
但**不知道三个臂该转到什么角度** —— 项目就停在半路。

> 我后来翻出原件才发现：当时放在那里的 `.m` 文件是从 **MATLAB 官方文档复制的示例**，
> 而且用的是 **KUKA iiwa**（串联臂），和 Delta 并联机构根本不是一回事。
> 那个文件已移除（MathWorks 版权 + 与本项目无关）。

**缺口现已补上** —— `reference/` 目录下引入了两份 **MIT 许可**的 Delta 逆运动学实现。
详见 [`tripod-arms-robot/NOTES.md`](tripod-arms-robot/NOTES.md)。

---

## 为什么这一步重要

**从"机械"到"编程"的第一次跳跃。**

之前在 Rutgers 做的是纯机械设计（连杆、结构）。这个项目第一次要求我：

- 读别人的协议（G-code）
- 用状态机解析它
- 把机械动作翻译成电机指令

**技术上不难，但思维上是个转折** —— 从"设计物理结构"转向"控制物理结构"。

**而且它撞上了一个至今仍在的墙：3D 打印机固件全是 GPL。**
详见 [`tripod-arms-robot/reference/README.md`](tripod-arms-robot/reference/README.md)。
