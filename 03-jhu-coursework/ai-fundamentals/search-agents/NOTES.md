# 原理讲解：搜索算法

> 这个作业在教**「怎么在解空间里找路」** —— 整个 AI 最基础的一块。
> 它把抽象的搜索算法跑在**真实的校园地图**上（JHU Homewood 校区），
> 让你直观看到不同策略的区别。

---

## 一、问题：怎么从 A 走到 B？

把地图抽象成**图（Graph）**：

- **节点（Node）** —— 路口
- **边（Edge）** —— 道路
- **权重（Weight）** —— 距离或耗时

作业里用的是 `networkx` 加载的真实校园路网：

```python
with open('hopkins_homewood_graph.graph', 'rb') as f:
    graph = pickle.load(f)
plot_graph(graph, fig_height=14, dpi=700, node_size=35)
```

> ⚠️ 这个 `.graph` 文件是从 Dropbox 下载的，链接早就失效了。
> 想跑通的话，用 `networkx` 自己造一个图，或者换成公开的路网数据（如 OpenStreetMap）。

---

## 二、搜索树：算法在维护什么

搜索算法需要一张「已经探索过的地图」——叫做**搜索树**。每个节点记：

| 字段 | 含义 |
|:---|:---|
| **State** | 当前在地图的哪个节点 |
| **Parent** | 从哪来的（用来回溯路径） |
| **Action** | 走的哪条边 |
| **Path cost** | 走到这里累计花了多少 |

有了 `Parent`，到达终点后就能**一路回溯还原出完整路径**。

---

## 三、三种搜索策略

### BFS — 广度优先

**用队列（FIFO）**，一层一层往外扩。

```python
from collections import deque

def bfs(graph, start, goal):
    frontier = deque([start])       # 队列
    came_from = {start: None}

    while frontier:
        node = frontier.popleft()   # ← 从队首取
        if node == goal:
            return reconstruct(came_from, goal)

        for neighbor in graph[node]:
            if neighbor not in came_from:
                came_from[neighbor] = node
                frontier.append(neighbor)   # ← 加到队尾
    return None
```

**特点：**

| ✅ | ❌ |
|---|---|
| **保证最短路径**（边权相同时） | 内存爆炸（要存整层） |
| 完备（有解就一定找得到） | 不看边权，只数步数 |

### DFS — 深度优先

**用栈（LIFO）**，一条道走到黑。

```python
frontier = [start]
node = frontier.pop()        # ← 从栈顶取
```

**特点：**

| ✅ | ❌ |
|---|---|
| 内存省（只存一条路径） | **不保证最短** |
| 适合深而窄的解空间 | 可能掉进无限深的坑 |

### Uniform-Cost Search — 一致代价

**用优先队列**，每次扩展**累计代价最小**的节点。

```python
import heapq
frontier = [(0, start)]                    # (累计代价, 节点)
cost, node = heapq.heappop(frontier)       # ← 取代价最小的
```

**这是 BFS 的推广** —— BFS 相当于「所有边权都等于 1」的特例。

**特点：** 边权不同时**依然保证最优**。这是 Dijkstra 算法的核心思想。

---

## 四、三者的本质区别

**关键在于「从 frontier 里取哪个节点」：**

| 算法 | 数据结构 | 取哪个 | 保证最优？ |
|:---|:---|:---|:---:|
| **BFS** | 队列 Queue | 最早进来的 | ✅（边权相同） |
| **DFS** | 栈 Stack | 最晚进来的 | ❌ |
| **UCS** | 优先队列 Heap | 累计代价最小的 | ✅ |

**这个「取舍顺序」的选择，就是搜索算法的全部。**

---

## 五、A\*：加上启发式（下一步）

UCS 只看着**已经走过的代价** `g(n)`，盲目地往四周扩。

**A\*** 再加一个**对未来的估计** `h(n)`：

```
f(n) = g(n) + h(n)
     ↑        ↑
  已走代价   到终点的估计距离
```

**`h(n)` 是关键** —— 如果它**从不高估**真实距离（叫做"可采纳性"），
A\* 就保证找到最优解，而且**扩展的节点数远少于 UCS**。

常用的启发式：
- **欧氏距离** —— 直线距离，永远不会高估
- **曼哈顿距离** —— 网格地图用

---

## 六、自己动手

```python
# 1. 造一个小图替代失效的 Dropbox 数据
import networkx as nx
G = nx.grid_2d_graph(10, 10)     # 10×10 网格

# 2. 分别跑 BFS / DFS / UCS，对比：
#    - 找到路径的长度
#    - 扩展了多少个节点
#    - 走过的路线形状（BFS 是同心圆扩散，DFS 是蛇形）

# 3. 加边权，看 UCS 和 BFS 的差异
```

**建议的改进方向：**
- **双向搜索** —— 从起点和终点同时搜，相遇即停（能大幅减少扩展节点）
- **迭代加深（IDA\*）** —— 兼顾 DFS 的省内存和 BFS 的最优性
- **加权 A\*** —— 故意让 `h(n)` 高估一点，换更快的速度（不保证最优）

> 📚 **深入方向**：A\*、Dijkstra、启发式搜索、规划（Planning）
