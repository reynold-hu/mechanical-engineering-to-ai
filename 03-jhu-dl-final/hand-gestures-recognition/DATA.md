# 数据集说明

本仓库**不包含数据集和模型权重**。运行代码前请自行采集。

## 需要的数据

| 文件 | 说明 |
|---|---|
| `Train dataset.zip` / `Test dataset.zip` | 手势图像数据集（自采） |
| `landmarks.csv` / `images.csv` | 手部关键点与图像路径索引 |
| `landmarks_rand.csv` / `images_rand.csv` | 打乱后的版本 |
| `landmarkstest*.csv` / `imagestest*.csv` | 测试集索引 |
| `DL_model.pt` | 训练好的模型权重 |
| `model/keypoint_classifier/keypoint.csv` | 关键点分类器训练数据 |
| `model/point_history_classifier/point_history.csv` | 轨迹分类器训练数据 |

## 数据是**自采**的 —— 用仓库里的脚本重新生成

这个项目的数据不是公开数据集，而是**用摄像头现场采集**的。仓库里保留了完整的采集脚本：

```bash
# 1. 启动摄像头采集并标注手势
python "Hand Gesture Detection.py"

# 2. 从采集结果导出关键点 / 图像索引
python "Get Train Dataset.py"
python "Get Test Dataset.py"

# 3. 按列打乱（对应 Shuffle Dataset by columns.ipynb）
python "Shuffle Dataset by columns.ipynb"

# 4. 训练
python "Train.py"
```

> 脚本里的数据路径已改为占位符 `<DATA_DIR>`，**跑之前需要按你本机的情况改回真实路径**。

## 识别的手势类别

写在 `model/keypoint_classifier/keypoint_classifier_label.csv` 里：

```
Open / Close / Pointer / OK
```

## 模型权重

`DL_model.pt` 是训练产物，仓库里没有保留。按上面步骤重新训练即可生成。
