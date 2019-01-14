# 1. 线性模型

## 1.1 基本形式

&emsp; 给定由 d 个属性描述的样本 **x**=(x1,x2,...,xd)，线性模型（*linear model*）试图学习一个通过属性的线性组合来进行预测的函数
```python
f(x) = w1*x1 + w2*x2 + ... + wd*xd + b
```

一般用向量表达：
```python
f(x) = x * w + b
```
其中参数 **w** 是一个 d 维的向量，当 **w** 和 b 学得之后，模型就得以确定

&emsp; 线性模型形式简单，易于建模，但却蕴含机器学习中一些重要的基本思想，许多功能更为强大的非线性模型（*nonlinear model*）可在线性模型的基础上通过引入层级结构或高维映射而得。

&emsp; 此外，由于 **w** 直观表达了各属性在预测中的重要性，因此线性模型有很好的可解释性（*comprehensibility*）

## 1.2 线性回归

**输入：** 数据矩阵 **x**.shape(n_sample, dim)，预测值向量 **y**.shape(n_sample)，则线性回归的向量矩阵表达为
```python
f(x) = x*w + b
```
其中，**w**.shape(dim,1)为参数向量，b为偏置(值)。

&emsp;令**W**=[**w**;b]，**X=[x,1]**（**1**是 n_sample 维向量），则线性模型可以写成
```python
f(X) = X*W
```

&emsp;线性模型的求解通过最小化目标函数学习参数
```python
J(W, X, y) = mean(sum( norm( f(X)-y ,2) ))
           = mean(sum( norm( X*W-Y， 2) ))
```

&emsp;求解上述目标函数对参数**W**的偏导
```python
partial(J(W,X,y), W) = X.T *(X*W - y)
```

&emsp;令上述偏导为0，可求得参数W的解析解
```python
partial(J(W,X,y), W) = 0
      X.T *(X*W - y) = 0
     X.T*X*W - X.T*y = 0
             X.T*X*W = X.T*y
                   W = inv(X.T*X) *X.T*y
```
**注：** 仅当 **X.T\*X** 可逆时，上述解析解有解。

> 优点：简单快速，可解释性强

> 缺点：对异常值敏感

## 1.3 岭回归

岭回归的表达式如下：
```python
f(x) = x*w + b + lam*norm(w,2)
```

&emsp;同理，令**W**=[**w**;b]，**X=[x,1]**（**1**是 n_sample 维向量），则岭回归可以写成
```python
f(X) = X*W + lam*norm(W,2)
```
其中，**W**为需要学习的参数，lam 为l2正则项系数

&emsp;线性模型的求解通过最小化目标函数学习参数
```python
J(W, X, y) = mean(sum( norm(f(X)-y, 2) )) + lam*norm(W,2)
           = mean(sum( norm(X*W-Y， 2) )) + lam*norm(W,2)
```

&emsp;求解上述目标函数对参数**W**的偏导
```python
partial(J(W,X,y), W) = X.T *(X*W - y) + 2*lam*W
                     = X.T *(X*W - y) + lam*W (for lam is a constant)
```

&emsp;令上述偏导为0，可求得参数W的解析解
```python
   partial(J(W,X,y), W) = 0
 X.T *(X*W - y) + lam*W = 0
X.T*X*W - X.T*y + lam*W = 0
        X.T*X*W + lam*W = X.T*y
      (X.T*X + lam*I)*W = X.T*y
                      W = inv(X.T*X + lam*I) *X.T*y
```
**注1：** 仅当 (**X.T\*X** + lam\***I**) 可逆时，上述解析解有解。但只要系数 lam 足够大，(**X.T\*X** + lam\***I**) 就可逆。

**注2：** 岭回归是对参数 **w** 作l2正则, 因此上述公式中的 **I** 并不是一个真正的单位矩阵，I 在对应偏置 b 的位置应置为 0

&emsp;岭回归是对参数 **w** 作l2正则，以防止线性模型产生过拟合问题。岭回归还有两种解释：

1. 岭回归是对参数 **w** 进行约束。其约束参数 **w** 的l2范数小于预设常数。

2. 岭回归是认为参数 **w** 服从高斯分布（先验信息），在最大化后验概率估计中，将权重 **w** 看做随机变量，服从均值为 0 高斯分布。

## 1.3 LASSO

LASSO 回归可以写成
```python
f(x) = x*w + b + lam*norm(w,1)
```
&emsp;同理，令**W**=[**w**;b]，**X=[x,1]**（**1**是 n_sample 维向量），则 LASSO 回归可以写成
```python
f(X) = X*W + lam*norm(W,1)
```
其中，**W**为需要学习的参数，lam 为l1正则项系数

&emsp;则其目标函数学习参数
```python
J(W, X, y) = mean(sum( norm(f(X)-y, 2) )) + lam*norm(W,1)
           = mean(sum( norm(X*W-Y， 2) )) + lam*norm(W,1)
```
注意到 LASSO 的目标函数是凸的，根据 KKT 条件，在最优解的地方要求梯度为0，但这里有一个小问题：l1-norm 不是光滑的，需要使用 *subgradient*。

&emsp;Subgradient：凸函数 f 在点 x0 的 subgradient，是实数 c 使得：`f(x)-f(x0) >= c(x-x0)`。在点 x0 的 subgradient 的集合是一个非空闭区间 [a,b]，其中 a 和 b 是单侧极限。
```python
partial(norm(w,1), w_j) = 
 - lam       if w_j < 0
 [-lam, lam] if w_j==0
 lam         if w_j > 0
```

&emsp;最小化目标函数, 令 `partial(J(W,x,y), w) = 0`， 解得
```python
w_j = 
(rho_j + lam/2) / z_j if rho_j < -lam/2
0                     if rho_j in [-lam/2, lam/2]
(rho_j - lam/2) / z_j if rho_j > -lam/2
```
其中
```python
rho_j = X[:,j].dot(y - X.dot(W)) where w_j = 0
    z = sum(X * X, axis=0)

Note: * means element-wise multiply and z_j = z[j]
```

L1 正则是拉普拉斯先验

## 1.4 L1 vs. L2

- L1 正则的约束域和 L2 正则的不同，区别在于 L2 的约束域比较"平滑"，而 L1 正则的约束域与每个坐标轴有角，而且目标函数的测地线除非位置摆的很好，大部分时候都会在角的地方相交，在角的地方产生稀疏性。

- 岭回归对参数 **w** 做了一个全局缩放，而 LASSO 回归则是做了一个 soft thresholding：将绝对值小于 lam/2 的那些系数直接表成零，这也解释了 LASSO 为何能产生稀疏解。

- 在最大后验概率估计中，L2 正则等价于参数 **w** 先验服从均值为 0 的高斯分布，L1 正则等价于参数先验服从均值为 0 的拉普拉斯分布。

## Logistic Regression

> 优点：计算代价不高，易于理解和实现

> 缺点：容易欠拟合（多项式特征，l1、l2正则）

逻辑回归模型如下：
```python
f(w,x) = sigmoid(w*x + b)
```
其中，**w**,b 是需要学习的参数。

&emsp;Sigmoid 函数将线性回归的预测转化为一个接近 0 或者 1 的值，得到近似概率预测。Sigmoid 函数定义为
```python
sigmoid(z) = 1 / (1+ exp(-z))
```
Sigmoid 函数具有很好的数学性质，sigmoid 函数是任意阶可导的凸函数，单调递增。

&emsp;一个事件的几率(*odds*)是指该事件发生的概率与该事件不发生的概率的比值，对逻辑回归而言
```python
odds = P(Y=1|x) / P(Y=0|x) 
     = f(w,x)/ (1-f(w,x))
     = exp(w*x +b)
```
则目标事件的对数几率(*log odds*)或 logit 函数为
```python
log odds = w*x + b
```
因此，逻辑回归实际上是在用线性回归模型的预测结果去逼近真实标记的对数几率。

&emsp;可以通过极大似然法来估计模型参数，目标事件服从伯努利分布，其对数似然函数为：
```python
J(w, x, y) = sum( y*log(f(w,x)) + (1-y)log(1-f(w,x)) )
```
上式成为**交叉熵代价函数**，是关于参数的高阶可导连续**凸函数**，可以使用经典的数据优化算法（如梯度下降法，牛顿法等）求得其**最优解**。