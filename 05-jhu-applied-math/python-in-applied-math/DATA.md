# 数据集说明

本仓库**不包含数据集**。8 个作业里有 3 个依赖外部数据，说明如下。

## 目录

| 目录 | 作业 | 是否需要外部数据 |
|---|---|---|
| `001FirstOtterAssignment` | Otter 环境入门 | ❌ 不需要 |
| `002SmallGenomeAssignment` | 基因组数据 | ❌ 代码内生成 |
| `003NimAssignment` | Nim 博弈 | ❌ 不需要 |
| `004LeastCostPath` | 最小代价路径 | ✅ **需要** |
| `005BrownianMotionAssignment` | 布朗运动 | ❌ 代码内生成 |
| `006Orderbook` | 订单簿模拟 | ✅ **需要** |
| `007LeastCostPathRevisited` | 最小代价路径（重做） | ✅ **需要** |
| `008StochasticDifferentialEquations` | 随机微分方程 | ✅ **需要** |

---

## 004 / 007 — 最小代价路径

**需要**：`H1.npy` ~ `H5.npy`、`V1.npy` ~ `V5.npy`（地形高度/代价矩阵）

这是课程提供的**地形栅格数据**，属于课程材料，故未随仓库发布。
如果是同门课程，从课程页面重新下载；否则可以在代码里**自行构造同形状的随机矩阵**跑通流程：

```python
import numpy as np
for i in range(1, 6):
    np.save(f'H{i}.npy', np.random.rand(256, 256))
    np.save(f'V{i}.npy', np.random.rand(256, 256))
```

（H\* 为水平代价，V\* 为垂直代价；实际形状以 notebook 里的读取逻辑为准。）

## 006 — 订单簿模拟

**需要**：`TRADES.csv`、`requests.csv`、`initial_customer_data.csv`、`final_customer_data.csv`

课程提供的**模拟交易数据**，同样未随仓库发布。
这些是订单簿模拟的输入/输出记录，可用 `ProcessRequests.ipynb` 里的逻辑自行生成一份同结构的合成数据跑通。

## 008 — 随机微分方程

**需要**：`SP500Daily.csv`、`SP500Weekly.csv`

标普 500 指数的日线/周线收盘价。**公开数据**，可自行获取：

- Yahoo Finance：<https://finance.yahoo.com/quote/%5EGSPC/history/>
- Stooq：<https://stooq.com/q/d/?s=%5Espx>

下载后整理成两列（日期、收盘价）的 CSV，命名为 `SP500Daily.csv` / `SP500Weekly.csv` 即可。

---

## 为什么不含数据

本仓库的定位是**公开技术方案、不开源数据集**。原始数据可能涉及课程材料授权、
第三方数据许可或个人隐私，因此统一不随仓库分发。

各 `.ipynb` 已清除输出单元格，避免残留数据痕迹。
