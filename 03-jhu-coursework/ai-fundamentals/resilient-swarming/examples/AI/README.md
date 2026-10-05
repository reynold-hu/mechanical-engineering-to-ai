# ⚠️ 这个目录里的代码**不是我写的**

## 来源

| | |
|:---|:---|
| **作者** | **Safwan Alam、Musad Haque** |
| **年份** | 2018–2019 |
| **性质** | JHU 课程提供的**示例代码**（不是我的作业答案） |

每个 `.m` 文件顶部都保留了原始署名：

```matlab
%% Authors: Safwan Alam, Musad Haque - 2018
```

## 为什么保留在这里

这些是**理解这个作业背景的必要材料** —— 它们定义了通信模型、邻居查找、
状态估计这些底层模块，我的作业是在它们的基础上做的。

**它们是"脚手架"，不是"答案"。** 而且文件里的 `TODO` 注释是原作者自己的笔记
（比如 "Move visual parameters out of here"），不是留给学生的作业要求。

## 我的部分在哪

同级的其他目录是我的工作：

```
formation_control/       编队控制（我的实现）
barrier_certificates/    避障证书（我的实现）
graph/                   图论工具
controllers/             控制器
patch_generation/        障碍物生成
utilities/               工具函数
```

## 许可证说明

本仓库整体采用 MIT。**这个子目录的代码版权归原作者（Safwan Alam / Musad Haque）。**

- 保留在原位是为了**保持上下文完整**（删掉的话示例代码引用会断）
- **如果你要复用，请遵守原作者的权利**，不要直接当作 MIT 使用
- 如果你是该课程的授课教师，希望移除这些文件，请联系仓库作者

> 与之类似的情况：`ur5-move-pick-place/tf_frame.m`（作者 Mengze X.，已按匿名规则处理）。
> 更早还有一个 MathWorks 官方示例文件，因与本项目机器人无关且版权属 MathWorks，已移除。
