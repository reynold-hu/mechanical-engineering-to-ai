# 参考实现（第三方，MIT 许可）

这个目录里的代码**不是我写的**，是从两个 MIT 许可的开源项目引入的，
用来补全本项目缺失的 **Delta / 并联机构逆运动学**。

## 为什么放在这里

我 2018 年做这个项目时，只写了两个部分：

1. `Gcode_interpreter CN.ino` —— 手写的 G-code 解析器（G / X / F 三个参数）
2. 一个从 MATLAB 官方文档复制过来的示例（**用的还是 KUKA iiwa，不是我的三臂机构**）

**真正的缺口是：Delta 并联机构的逆运动学我从来没实现过。** 所以补上参考实现，
让后面看的人知道该怎么接。

---

## ① DeltaKinematics (C++ / C# / JS)

| | |
|---|---|
| 来源 | [`12343954/Rotary-Delta-Robot-Kinematics`](https://github.com/12343954/Rotary-Delta-Robot-Kinematics) |
| 作者 | Cooloo AI |
| 许可 | **MIT License** (Copyright © 2020 Cooloo AI) |
| 文件 | `DeltaKinematics.h/.cpp`、`Delta-Kinematics.cpp`、`ik_fk.js` |

**为什么选它**：C++ 实现，和 Arduino（`.ino` 本质是 C++）最接近，移植成本最低。

## ② Delta Robot Notebooks (Python)

| | |
|---|---|
| 来源 | [`wiesnerroyal/delta-robot`](https://github.com/wiesnerroyal/delta-robot) |
| 作者 | wiesnerroyal |
| 许可 | **MIT License** (Copyright © 2023 wiesnerroyal) |
| 文件 | `prismatic_joint_delta_kinematic.ipynb`、`rotation_joint_delta_kinematic.ipynb` |

**为什么选它**：把推导过程写清楚了，**适合当教学材料** —— 能看懂公式怎么来的，
不只是调用一个黑盒函数。

---

## 关于一个**没搬进来**的库

Delta 机器人运动学最流行的开源实现是
[`tinkersprojects/Delta-Kinematics-Library`](https://github.com/tinkersprojects/Delta-Kinematics-Library)（53 ⭐，
Arduino C++，本来是最贴合本项目的）——

**但它是 GPL-3.0。** 本仓库整体采用 MIT，引入 GPL 代码会导致**整个仓库被迫改为 GPL**，
所以没有采用。

> 这不是"不想用"，是许可证不兼容。**这也是开源实践中很常见的一个坑。**

## 使用须知

- 这两份代码各自的 `LICENSE` 文件**必须保留**（MIT 的要求）
- 如果你在自己的项目里用，请同时保留原作者署名
- 本仓库对这两份代码**不做任何修改**，原样引入
