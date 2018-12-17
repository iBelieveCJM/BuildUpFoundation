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

## 1.3 岭回归

同理，令**W**=[**w**;b]，**X=[x,1]**（**1**是 n_sample 维向量），则岭回归可以写成
```python
f(X) = X*W + lam*norm(W,2)
```
其中，**W**为需要学习的参数，lam 为l2正则项系数

&emsp;线性模型的求解通过最小化目标函数学习参数
```python
J(W, X, y) = mean(sum( norm( f(X)-y ,2) ))
           = mean(sum( norm( X*W-Y + lam*norm(W,2)， 2) ))
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
**注：** 仅当 (**X.T\*X** + lam\***I**) 可逆时，上述解析解有解。但只要系数 lam 足够大，(**X.T\*X** + lam\***I**) 就可逆。

&emsp;岭回归是对参数**W**作l2正则，以防止线性模型产生过拟合问题。岭回归还有两种解释：

1. 岭回归是对参数**W**进行约束。其约束参数**W**的l2范数小于预设常数。

2. 岭回归是认为参数**W**服从高斯分布（先验信息）