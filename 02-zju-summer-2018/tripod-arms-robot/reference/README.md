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

## 另一个绕不开的坑：**3D 打印机固件全是 GPL**

这个机器人是**从 Delta 3D 打印机改造**的，所以最自然的想法是
「直接把打印机固件的运动控制搬过来」。我去查了一圈：

| 固件 | 许可证 |
|:---|:---|
| [Marlin](https://github.com/MarlinFirmware/Marlin) | 🔴 GPL-3.0 |
| [Klipper](https://github.com/Klipper3d/klipper) | 🔴 GPL-3.0 |
| [GRBL](https://github.com/gnea/grbl) | 🔴 GPL-3.0 |
| [Candle](https://github.com/Denvi/Candle) | 🔴 GPL-3.0 |
| [Teacup](https://github.com/Traumflug/Teacup_Firmware) | 🔴 GPL-2.0 |

**这不是巧合** —— 3D 打印固件从 Sprinter / GRBL 一脉相承，
整个生态几十年来都建立在 GPL 上。**想用打印机固件的运控代码，就必须接受 GPL。**

### 那怎么办？

**关键认识：Delta 逆运动学的数学和代码来源无关。**

不管这段代码来自打印机固件、通用运动学库，还是论文推导，它算的都是同一件事 ——
**给定末端执行器的 (x, y, z)，求三个臂各自的转角**。这是个纯几何问题。

所以：

- ❌ 不需要（也不能）搬 GPL 的打印机固件
- ✅ 上面那两份 **MIT** 实现算的是**同一套公式**

**换行的教训是**：遇到「这个功能只有某个项目实现了」时，先问一句
「**它解决的数学问题是什么？**」—— 通常都有多个来源，挑许可证兼容的那个就行。

---

## 使用须知

- 这两份代码各自的 `LICENSE` 文件**必须保留**（MIT 的要求）
- 如果你在自己的项目里用，请同时保留原作者署名
- 本仓库对这两份代码**不做任何修改**，原样引入
