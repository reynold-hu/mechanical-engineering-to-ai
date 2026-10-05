# Tripod Arms Grabbing Robot based on Delta 3D Printer

> 🟡 **部分完成** —— G-code 解析器写完了，**逆运动学当时没做**，参考实现见 `reference/`

- **导师**：Prof. Senyang W.
- **组员**：Reynold Hu, Keqin W.
- **场景**：浙江大学暑期学习，2018

---

## 这个项目是什么

把一个 Delta 3D 打印机改造成三臂抓取机器人。我当时负责的部分是**固件侧** ——
让机器能读懂上位机发来的 G-code 指令。

## 我实际做了什么

| 文件 | 说明 |
|:---|:---|
| `Gcode_interpreter CN.ino` | **手写的 G-code 解析器**（52 行）—— 解析 `G` / `X` / `F` 三个参数，串口逐字符读取 |

解析器逻辑很朴素：一个状态机，遇到 `G`/`X`/`F` 就切换到对应参数槽，
遇到回车结束一条指令。**没有用 GRBL 之类的现成库，是从零写的。**

## 当时没做完的部分 ⚠️

**Delta 并联机构的逆运动学从来没实现。** 机器能解析"移动到哪里"，
但**不知道三个臂该转到什么角度** —— 这一步缺失，项目就停在半路。

> 我翻出了原件，发现当时放的那个 `.m` 文件其实是从 **MATLAB 官方文档复制的示例**，
> 而且用的是 **KUKA iiwa**（串联臂），跟 Delta 并联机构根本不是一回事。
> 那个文件已从本仓库移除（MathWorks 版权 + 与本项目无关）。

### 补上了参考实现

`reference/` 目录下引入了**两份 MIT 许可的开源实现**，专门解决这个缺口：

| 目录 | 来源 | 语言 | 用途 |
|:---|:---|:---|:---|
| `reference/delta-kinematics-cpp/` | [12343954](https://github.com/12343954/Rotary-Delta-Robot-Kinematics) (MIT) | C++ / JS | 最接近 Arduino，移植成本最低 |
| `reference/delta-kinematics-notebooks/` | [wiesnerroyal](https://github.com/wiesnerroyal/delta-robot) (MIT) | Python | **推导过程清楚，适合当教材读** |

详见 [`reference/README.md`](reference/README.md)。

> **为什么不直接用最流行的那个？** Delta 运动学最流行的开源库是
> `tinkersprojects/Delta-Kinematics-Library`（53 ⭐，Arduino C++，本来最贴合），
> **但它是 GPL-3.0** —— 引入会让整个 MIT 仓库被迫改许可，所以放弃。
> 这是开源实践里非常典型的许可证陷阱。

## 想接着做的话

1. 读 `reference/delta-kinematics-notebooks/` 的推导，理解 Delta 逆解怎么来的
2. 把 `DeltaKinematics.cpp` 移植成 `.ino`（主要是去掉 C++ 标准库依赖）
3. 把逆解输出接到 `Gcode_interpreter CN.ino` 的 `X` 参数上 —— **这一步接上，项目就活了**

需要的数学基础：空间几何、余弦定理、并联机构的约束方程。
