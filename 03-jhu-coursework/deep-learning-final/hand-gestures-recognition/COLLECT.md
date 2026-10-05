# 数据采集指南

这个项目的数据**不是公开数据集，是用摄像头现场采集的**，所以仓库里没有。
本文档说明怎么重新采一份。

> 采集本身不难，**一个下午能搞定** —— 真正的坑在最后一步「打标签」（见下）。

---

## 一、需要什么

| | |
|---|---|
| **硬件** | 一个摄像头（笔记本自带就行） |
| **环境** | 光线均匀、背景干净（MediaPipe 对光照敏感） |
| **依赖** | `opencv-python`、`mediapipe`、`numpy`、`pandas` |

```bash
pip install opencv-python mediapipe numpy pandas
```

---

## 二、识别哪几种手势 ⚠️

**项目实际做的是 8 种手势**（见本目录 `README.md`），8000+ 训练样本：

| # | 手势 |
|:---:|:---|
| 1 | `Stop` |
| 2 | `Good` |
| 3 | `Yes` |
| 4 | `Love you` |
| 5 | `No way` |
| 6 | `Okay` |
| 7 | `Gimme a second` |
| 8 | `Call me later` |

### 两套分类器

采集时**每一帧同时产出两种特征**，喂给两个不同的分类器：

| 分类器 | 看什么 | 标签文件 |
|:---|:---|:---|
| **keypoint** | 手的**形状**（21 个关键点坐标） | `model/keypoint_classifier/keypoint_classifier_label.csv` |
| **point_history** | 手的**运动轨迹**（关键点随时间的变化） | `model/point_history_classifier/point_history_classifier_label.csv` |

> ⚠️ **注意**：仓库里这两个标签文件是 **4 个标签的早期版本**
> （`Open/Close/Pointer/OK` 和 `Stop/Clockwise/Counter Clockwise/Move`），
> **不是最终 8 手势版的**。重新采集时**用上面那 8 个**，并把标签文件一起更新。

**采集时每个手势多换几个角度**（正对、倾斜、远一点近一点），否则模型泛化会很差。

---

## 三、采集流程

### 步骤 1 · 改路径

`Get Train Dataset.py` 和 `Get Test Dataset.py` 里有两处路径要改（现在都是 `<DATA_DIR>` 占位符）：

```python
landmarkpath = r"<你的路径>\excel\landmarks.csv"
imagepath    = r"<你的路径>\excel\images.csv"
```

**测试集脚本**指向另一个目录（`exceltest\`），别搞混。

### 步骤 2 · 跑采集脚本

```bash
python "Get Train Dataset.py"
```

会弹出摄像头画面。**把手举到镜头前**，脚本会：

| 每帧做两件事 | 写到 |
|:---|:---|
| 用 MediaPipe 提 21 个手部关键点（42 个坐标值） | `landmarks.csv` |
| 抠出手部包围盒 → **缩放到 28×28**（2352 个像素值） | `images.csv` |

> ⚠️ 是**逐帧连续写**的（`append` 模式）—— 你举着手不放，它就一直在存。
> 所以**每个手势举 3~5 秒**就够了，举太久会存出几万行垃圾。

**按 `q` 退出。**

测试集同理：

```bash
python "Get Test Dataset.py"
```

### 步骤 3 · 打乱

跑 `Shuffle Dataset by columns.ipynb`，把采集顺序打散（否则同类样本全挤在一起，训练会废）。

---

## 四、⚠️ 这一步脚本里没有 —— 你得补上

**采集脚本只写图像和关键点，不写标签。** 但 `Train.py` 读的是：

```python
df_train["label"]        # ← 这一列采集脚本没生成
```

我当时是**手工加的标签列**，所以代码里没有这一步。重新采集的话，选一种：

### 做法 A · 分次采集，事后打标（简单粗暴）

一个手势采一次，采完立刻改名：

```bash
python "Get Train Dataset.py"     # 只举 Open → 退出
mv images.csv images_open.csv     # 用完再清空原文件继续下一个
```

四个手势采完后，用 pandas 拼起来加标签：

```python
import pandas as pd
frames = []
for label, f in [('Open','images_open.csv'), ('Close','images_close.csv'),
                 ('Pointer','images_pointer.csv'), ('OK','images_ok.csv')]:
    d = pd.read_csv(f, header=None)
    d['label'] = label
    frames.append(d)
pd.concat(frames).to_csv('images.csv', index=False)
```

`landmarks.csv` 同理。

### 做法 B · 改采集脚本，实时打标（推荐）

在 `Get Train Dataset.py` 里加一个当前标签变量，采的时候按数字键切换：

```python
from itertools import count
current = 0                          # 当前手势下标
LABELS = ['Open', 'Close', 'Pointer', 'OK']

while True:
    # ... 原有逻辑 ...
    np.savetxt(lmhandle,  np.append(flatten,     current).reshape(1, -1), delimiter=',')
    np.savetxt(imghandle, np.append(img_flatten, current).reshape(1, -1), delimiter=',')

    key = cv2.waitKey(1)
    if key == ord('q'): break
    elif key in (ord('0'), ord('1'), ord('2'), ord('3')):
        current = int(chr(key))      # 按 0-3 切换手势
```

**做法 B 一次采完，不用手工拼。** 建议用这个。

---

## 五、训练

采完 + 打乱 + 有标签列之后：

```bash
python Train.py
```

产出 `DL_model.pt`（本仓库不含，训练产物不入库）。

想跑实时演示（加载模型识别手势）：

```bash
python "Hand Gesture Detection.py"
```

---

## 六、为什么仓库里没有这份数据

1. **是个人采集的图像** —— 涉及出镜者的肖像，不适合公开
2. **主仓库的原则是不含数据集** —— 只开源技术方案
3. **但它可再生** —— 按上面流程自己采一份就行，所以不构成障碍

各个项目的数据策略详见同目录的 [`DATA.md`](DATA.md)。
