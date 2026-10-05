# 数据集说明

本仓库**不包含数据集**。运行代码前请自行获取。

## 需要的数据

| 文件 | 说明 |
|---|---|
| `YaleB_32x32.mat` | Extended Yale Face Database B（32×32 灰度版本） |

## 获取方式

Extended Yale Face Database B 由耶鲁大学公开发布，用于人脸识别研究：

- 官方页面：<http://vision.ucsd.edu/content/extended-yale-face-database-b-b>
- 该数据集需向发布方申请/下载，**请遵守其原始许可，勿再分发**

## 代码期望的路径

`Face_Recognition_Zhijing_Hu.ipynb` 会从当前目录读取 `YaleB_32x32.mat`。
把下载到的文件放到本项目根目录即可，或修改 notebook 里的加载路径。

## 数据结构

MATLAB `.mat` 文件，包含：

- `fea` — 特征矩阵，每行一个样本，1024 维（32×32 展平）
- `gnd` — 标签向量，对应每个人的类别编号
