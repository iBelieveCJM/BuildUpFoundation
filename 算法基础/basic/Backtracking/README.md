# 回溯法

## introduction

&emsp;回溯法实际上是一个类似穷举，主要是在搜索尝试过程中寻找问题的解，当发现已不满足条件时，就“回溯”返回，尝试别的路径。

&emsp;回溯法是一种选优搜索法，按选优条件向前搜索，以达到目的。当探索到某一步并不优或达不到目的时，就回退一步重新选择，这种走不通就退回再走的技术为回溯法，而满足回溯条件的某个状态的点称为“回溯点”

&emsp;许多复杂的、规模较大的问题都可以使用回溯法，有“通用解题方法”的美称。

## basic idea

&emsp;在包含问题的所有解的解空间树中，按照**深度优先搜索**的策略，从根结点出发深度探索解空间树。当探索到某一结点时，要先判断该结点是否包含问题的解，如包含，就从该结点出发继续探索下去，若该结点不包含问题的解，则逐层向其祖先结点回溯。

&emsp;若用回溯法求问题的所有解时，要回溯到根，且根结点的所有可行的子树都要已被搜索遍才结束。

&emsp;若使用回溯法求任一个解时，只要搜索到问题的一个解就可以结束。

## workflow

1. 针对所给问题，明确定义问题的解空间，问题的解空间应至少包含问题的一个（最优）解

2. 确定节点的扩展搜索规则

3. 以深度优先方式搜索解空间，并在搜索过程中用剪枝函数避免无效搜索。

