# 原理讲解：博弈树搜索

> 这个作业在教你**怎么让机器「想几步之后的事」**。
> 它是最经典的 AI 入门题，也是后来 AlphaGo 那套东西的祖先。

---

## 一、问题：怎么选一步好棋？

假设你和一个**完美对手**下棋。轮到你走，你有若干合法着法，选哪个？

关键洞察：**棋类是完全信息、确定性、零和的博弈。**

- **完全信息** —— 双方都能看到整个棋盘，没有隐藏信息
- **确定性** —— 走一步的结果是确定的，没有随机
- **零和** —— 你赢就是我输，利益总量不变

这三个性质加起来，意味着**你可以把未来「推演」出来** —— 这就是博弈树搜索的前提。

---

## 二、Minimax：核心思想

把棋局看成一棵树：

```
                当前局面（轮到你）
          ┌────────┼────────┐
        走法A    走法B     走法C        ← 你的选择层（MAX）
        /│\      /│\       /│\
      ...                                     ← 对手的应对层（MIN）
```

**两个角色轮流决策：**

| 层 | 角色 | 目标 |
|:---|:---|:---|
| **MAX 层** | 你 | 让分数**最大** |
| **MIN 层** | 对手 | 让分数**最小**（因为他想让局面对你最不利） |

递归定义：

```python
def minimax(board, depth, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board)          # 到叶子节点，用评估函数打分

    if is_maximizing:
        best = -inf
        for move in legal_moves:
            best = max(best, minimax(apply(move), depth-1, False))
        return best
    else:
        best = +inf
        for move in legal_moves:
            best = min(best, minimax(apply(move), depth-1, True))
        return best
```

**要点：** MAX 层取「子节点的最大值」，MIN 层取「子节点的最小值」——
因为**双方都假设对方会走最优的那一步**。

---

## 三、评估函数：机器怎么「看懂」局面

搜索到叶子节点时，棋局可能还没结束，没法直接判断输赢。这时需要一个
**启发式评估函数**，给当前局面打个分。

这个作业用的是最经典的**子力价值**：

```python
def evaluate_board(board):
    # 兵 10 / 马 30 / 象 30 / 车 50 / 后 90 / 将死 9000
    wp = len(board.pieces(chess.PAWN,   chess.WHITE))
    bp = len(board.pieces(chess.PAWN,   chess.BLACK))
    # ... 各类棋子分别统计，加权求差
```

**返回值 > 0 表示白方占优。**

> 💡 **这个函数的好坏直接决定棋力。** 这里只算了子力，没考虑：
> 位置（马在中心比在边角强）、兵型、王的安全、机动性……
> 真正的国际象棋引擎（Stockfish）的评估函数有几十项。

**这也解释了 notebook 里的那个观察：**

> *"Not a really good move because our horse will be captured by enemy's bishop
> and our agent can not see this since it only looks one step ahead."*

只看一步（depth=1）时，机器看不到「我走了之后对手能吃我子」—— 这就是**搜索深度的重要性**。

---

## 四、Alpha-Beta 剪枝：让它快起来

Minimax 有个致命问题：**分支因子 ^ 深度**。国际象棋平均每步约 35 种走法，
搜 5 层就是 35⁵ ≈ 5000 万——太慢。

**Alpha-Beta 剪枝**的核心洞察：

> 如果我已经知道某条路走不通，**就没必要把它算完**。

```python
def alphabeta(board, depth, alpha, beta, is_maximizing):
    if depth == 0 or board.is_game_over():
        return evaluate(board)

    if is_maximizing:
        for move in legal_moves:
            alpha = max(alpha, alphabeta(..., alpha, beta, False))
            if alpha >= beta:
                break        # ← β 剪枝：MIN 层已经找到更差的选择，不用再算
        return alpha
    else:
        for move in legal_moves:
            beta = min(beta, alphabeta(..., alpha, beta, True))
            if beta <= alpha:
                break        # ← α 剪枝：MAX 层已经找到更好的选择，不用再算
        return beta
```

**`alpha`** = MAX 已知能保证的最好分数
**`beta`** = MIN 已知能保证的最好分数（对 MAX 而言的最差）

当 `alpha >= beta`，说明这个分支对双方都没有意义了，**剪掉**。

**效果：** 理论最优情况下，同样时间可以**搜两倍深度**（因为剪枝把复杂度从
O(b^d) 降到 O(b^(d/2))）。

---

## 五、这个作业做了什么

1. **实现 minimax** —— 基础版，能选棋但很慢
2. **实现 alpha-beta 剪枝** —— 加剪枝，同深度下快得多
3. **求解将死谜题** —— 给定残局，找出强制将死的最短路径
4. **两个 agent 对战** —— 让不同深度/配置的 agent 互相下

---

## 六、延伸：从这里到 AlphaGo

| 年代 | 方法 | 突破 |
|:---|:---|:---|
| 1950s | Minimax | 博弈树搜索的起点 |
| 1956 | Alpha-Beta | 把搜索深度翻倍 |
| 1997 | Deep Blue 胜卡斯帕罗夫 | 暴力搜索 + 专用硬件 |
| 2016 | **AlphaGo** 胜李世石 | **用神经网络替代评估函数** + 蒙特卡洛树搜索 |
| 2017 | AlphaZero | 连人类棋谱都不需要，纯自我对弈 |

**关键转折：** 评估函数从「人手写规则」变成「神经网络自己学」。
但**搜索的骨架（Minimax / MCTS）没变** —— 这正是这个作业在打的底子。

---

## 七、自己动手

```python
# 1. 先跑通看效果
python -c "import chess; b = chess.Board(); print(b)"

# 2. 试试改评估函数
#    加上位置权重（比如马在中心的加分），看看棋力变化

# 3. 对比搜索深度
#    depth=1 / 2 / 3 各跑一局，看耗时和走法质量
```

**建议的改进方向：**
- **走法排序** —— 先搜「吃子」的走法，能让 alpha-beta 剪掉更多分支
- **迭代加深** —— 先搜浅层，用结果指导深层搜索的顺序
- **置换表** —— 缓存已搜索过的局面（不同路径可能到达同一局面）
- **更好的评估** —— 加位置、兵型、王安全

> 📚 **深入方向**：蒙特卡洛树搜索（MCTS）、强化学习（AlphaZero 论文）
