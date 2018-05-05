### String to Integer (atoi) ###

#### 1. 问题描述

&emsp;把字符串转换为数字

&emsp;你需要注意几点：

1. 你需要丢弃开头的空格（如果有），直到遇到第一个非空格。

2. 可选的正负号

3. 若数字后面跟着非数字符号，忽略

4. 若超出了类型 int 的范围，上溢出返回 int 类型的最大值，下溢出返回 int 类型的最小值

5. 其他情况，返回 0

#### 2. 测试用例

```
In:  "42"
Out: 42
```
```
In:  "   -42"
Out: -42
```
```
In:  "42 with words"
Out: 42
```
```
In:  "words"
Out: 0
```
```
In:  "-937837953953"
Out: -2147483648
```
#### 3. 代码片段

```C++
#include<climts>
int myAtoi(string str) {
    // 输入判断1：为空即返回0
    if(str.size()==0){
        return 0;
    }
    // 记录下标
    int index = 0;
    // 跳过空格
    while(str[index]==' '){
        ++index;
    }
    // 输入判断2：开头不是合法字符返回0
    if( (str[index]<'0' && str[index]>'9') && (str[index]!='-' or str[index]!='+') ){
        return 0;
    }
    // 判断符号
    int sign = 1;    // 记录符号
    if(str[index]=='-'){
        sign = -1;
        index += 1;  // 跳过符号
    }
    else if(str[index]=='+'){
        index += 1;  // 跳过符号
    }
    // 数字转换
    long ret = 0;
    for(; str[index]>='0'&&str[index]<='9'; ++index)
    {
        ret = ret*10 + str[index]-'0';
        
        // 越界判断
        if(sign*ret > INT_MAX){
            return INT_MAX;
        }
        else if(sign*ret < INT_MIN){
            return INT_MIN;
        }
    }
    return static_cast<int>(sign*ret);
}
```

> 使用了 long 类型算不算作弊？
