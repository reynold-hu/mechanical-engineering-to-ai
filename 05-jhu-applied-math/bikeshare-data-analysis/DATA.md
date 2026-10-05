# 数据集说明

本仓库**不包含数据集**。运行代码前请自行获取。

## 需要的数据

| 文件 | 说明 |
|---|---|
| `201912-capitalbikeshare-tripdata.csv` | Capital Bikeshare 2019 年 12 月原始行程数据 |
| `X_train.csv` / `X_test.csv` | 预处理后的特征（代码自行生成） |
| `y_train.csv` / `y_test.csv` | 预处理后的标签（代码自行生成） |
| `labels.csv` | 标签映射（代码自行生成） |

> 后 5 个文件是 notebook 从原始数据**派生**出来的中间产物，不需要单独下载。

## 获取方式

Capital Bikeshare 的行程数据公开发布：

- 官方数据页：<https://capitalbikeshare.com/system-data>
- 直接下载 2019 年 12 月：`https://s3.amazonaws.com/capitalbikeshare-data/201912-capitalbikeshare-tripdata.zip`

如需其他月份，把年份月份替换掉即可（如 `202001-...`）。

## 代码期望的路径

把 `201912-capitalbikeshare-tripdata.csv` 放在本项目根目录。

## 数据结构（原始数据主要字段）

| 字段 | 含义 |
|---|---|
| `Duration` | 行程时长（秒）—— 本项目要预测的目标 |
| `Start date` / `End date` | 起止时间 |
| `Start station` / `End station` | 起止站点 |
| `Bike number` | 车辆编号 |
| `Member type` | 会员类型 |

`Bikeshare Data Analysis.ipynb` 会在此基础上做特征工程（周次、日期、季节等）。
