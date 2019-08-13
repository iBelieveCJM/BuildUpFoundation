// 0-1 背包问题
// 问题描述：
//  给定 n 个重量为 w1,w2,w3...wn， 价值为 v1,v2,v3...vn 的物品，
//  和容量为 C 的背包，求满足背包容量的前提下，使得包内总价值最大
//
// 问题分析：
//  令 F(n, C) 表示将前 n 个物品放进容量为 C 的背包里，得到的最大价值
//  此时，我们有两种选择：
//      1. 不放第 n 个物品，此时总价值为 F(n-1, C)
//      2. 放置第 n 个物品，此时总价值为 vn + F(n-1, C-wn)
//  在两种选择中，选择总价值最大的方案。
//  得到状态转移方程如下：
//      F(i, C) = max( F(i-1, C), vi + F(i-1, C-wi) )

#include<bits/stdc++.h>
using namespace std;

int bag(vector<int>& w, vector<int>& v, int step, int capacity){
    /* 递归
    优点：简单，几乎就是直接套状态转移方程
    缺点：存在大量重复计算
    */
    if(step<0 || capacity <=0){
        return 0;
    }
    // 选择1.不放第 n 个物品
    int choice1 = bag(w, v, step-1, capacity), choice2=0;
    // 选择2.放置第 n 个物品
    if(w[step] <= capacity){ //判断能否放置第 n 个物品
        choice2 = bag(w, v, step-1, capacity-w[step]);
    }
    return max(choice1, choice2);
}

int bag(vector<int>& w, vector<int>& v, int step, int capacity,
        vector<vector<int>> mem){
    /* 递归+记忆
    记忆体可以用数组或字典实现，
    有限范围用数组，过大范围用字典
    */
    if(step<0 || capacity <=0){
        return 0;
    }
    // 查找记忆，若已经计算过，直接返回
    if(mem[step][capacity]!=0){
        return mem[step][capacity];
    }
    // 选择1.不放第 n 个物品
    int choice1 = bag(w, v, step-1, capacity), choice2=0;
    // 选择2.放置第 n 个物品
    if(w[step] <= capacity){ //判断能否放置第 n 个物品
        choice2 = bag(w, v, step-1, capacity-w[step]);
    }
    // 存储计算，避免重复计算
    mem[step][capacity] = max(choice1, choice2);
    return mem[step][capacity];
}

int bag1(vector<int>& w, vector<int>& v, int capacity){
    /* 动态规划1：二维数组存储结果
    */
    int n = w.size();
    vector<vector<int>> dp(n+1, vector<int>(capacity+1, 0));
    for(int i=1; i<=n; ++i){
        for(int j=1; j<=capacity; ++j){
            dp[i][j] = dp[i-1][j]; // 选择1
            if(w[i] <= j){         // 选择2
                dp[i][j] = max(dp[i][j], v[i]+dp[i-1][j-w[i]]);
            }
        }
    }
    return dp[n][capacity];
}

int bag2(vector<int>& w, vector<int>& v, int capacity){
    /* 动态规划2：一维数组存储结果
    */
    int n = w.size();
    vector<int> dp(capacity+1, 0);
    for(int i=0; i<n; ++i){
        for(int j=capacity; j>=w[i]; --j){
            if(w[i] <= j){
                dp[j] = max(dp[j], v[i]+dp[j-w[i]]);
            }
        }
    }
    return dp[capacity];
}