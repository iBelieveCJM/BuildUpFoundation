[TOC]

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

&emsp; C++版
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

&emsp;Java版
```Java
public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
    // 创建头文件
    ListNode dummyHead = new ListNode(0);

    ListNode p = l1, q = l2, curr = dummyHead;
    int carry = 0;  // 记录进位

    while (p != null || q != null) {
        int x = (p != null) ? p.val : 0;
        int y = (q != null) ? q.val : 0;
        int sum = carry + x + y;

        carry = sum / 10;
        curr.next = new ListNode(sum % 10);

        curr = curr.next;
        if (p != null) {
            p = p.next;
        }
        if (q != null) {
            q = q.next;
        }
    }
    if (carry > 0) {
        curr.next = new ListNode(carry);
    }
    return dummyHead.next;
}
```

### Add Two Number ####

#### 1. 问题描述

&emsp;把两个非负整数相加，整数的每一位被逆序存储在链表中，结果返回一个列表

&emsp;你需要注意

1. 非法输入检测

2. 注意相加时产生的进位

3. 注意整数的位数不同

#### 2. 测试用例

```
In:  (2 -> 4 -> 3) + (5 -> 6 -> 4)
Out: 7 -> 0 -> 8
```
```
In:  (NULL) + (NULL)
Out: NULL
```
```
In:  (NULL) + (1 -> 2 -> 3)
Out: 1 -> 2 -> 3
```

#### 3. 代码片段

```C++
//////////////////////////////////////////////
// 定义结点结构
//////////////////////////////////////////////
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

//////////////////////////////////////////////
// 处理进位并创建结点
//////////////////////////////////////////////
ListNode* calculate(int value, int& in){
    ListNode* ret = NULL;
    if(value/10 == 0){
        in = 0;
        ret = new ListNode(value);
    }
    else{
        in = 1;
        ret = new ListNode(value - 10);
    }
    return ret;
}
ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
    // 输入检测        
    if(l1 == NULL || l2 == NULL)
        return NULL;
    // 创建头结点 
    ListNode head(0);
    ListNode* cur = &head;
    
    int in = 0;    // 记录进位
    int value = 0; // 记录每位相加的和

    while(l1!=NULL && l2!=NULL)
    {
        value = l1->val + l2->val + in;
        cur->next = calculate(value, in);
        
        l1 = l1->next;
        l2 = l2->next;
        cur = cur->next;
    }
    // 处理较长链剩下的位数
    while(l1!=NULL){
        value = l1->val + in;
        cur->next = calculate(value, in);
        
        l1 = l1->next;
        cur = cur->next;
    }
    while(l2!=NULL){
        value = l2->val + in;
        cur->next = calculate(value, in);
        
        l2 = l2->next;
        cur = cur->next;
    }
    // 处理最后的进位
    if(in == 1){
        cur->next = new ListNode(in);
    }
    
    return head.next;
}
```