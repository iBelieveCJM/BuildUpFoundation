// 最大 m 段子序列和
// 问题描述：
//   给定由 n 个整数组成的序列，以及一个正整数 m，
//   要求确定序列 m 个不相交的子序列，使得这 m 个子序列的和达到最大，
//   求出最大和
//
// 问题分析：
//   令 dp[i][j] 表示为前 j 项中的 i 个不相交的子序列的最大和，序列为 arr
//   求 dp[i][j] 时，有两种情况：
//     1. 把第 j 项加入第 i 个子序列末尾
//        ==> dp[i][j-1] + arr[j]
//     2. 把第 j 项作为单独的子序列，加上前 i-1 项子序列最大和
//        ==> dp[i-1][k] + arr[j] (i-1 <= k < j)
//   dp[i][j] 为两种情况中的最大值
//   最终结果为： max{dp[m][i] | m<= i <= n}
//
// 例子：arr: -2,11,-4,13,-5,6,-2
//   n=7, m=7                   ==>     n=7, m=7                         ==>   n=7, m=5
//   arr|   -2 11 -4 13 -5  6 -2        arr|   -2 11 -4 13 -5  6 -2            arr|   -2 11 -4 13 -5  6 -2
//    dp| 0  0  0  0  0  0  0  0         dp| 0  0  0  0  0  0  0  0 |0(0)       dp| 0  0  0  0  0  0  0  0 |0(0)
//        0 -2 11  7 20 15 21 19             0 -2  0  0  0  0  0  0 |1(1)           0 -2 11  7  0  0  0  0 |1(1)
//        0  0  9  7 24 19 26 24             0  0  9  0  0  0  0  0 |2(0)           0  0  9  7 24  0  0  0 |2(0)
//        0  0  0  5 22 19 30 28             0  0  0  5  0  0  0  0 |3(1)           0  0  0  5 22 19  0  0 |3(1)
//        0  0  0  0 18 17 28 28             0  0  0  0 18  0  0  0 |4(0)           0  0  0  0 18 17 28  0 |4(0)
//        0  0  0  0  0 13 24 26             0  0  0  0  0 13  0  0 |5(1)           0  0  0  0  0 13 24 26 |5(1)
//        0  0  0  0  0  0 19 22             0  0  0  0  0  0 19  0 |6(0)
//        0  0  0  0  0  0  0 17             0  0  0  0  0  0  0 17 |7(1)

#include <bits/stdc++.h>
using namespace std;

int max_m_subsum1(vector<int> arr, int m){
    int n = arr.size();
    if(m > n){     // m > n 时没有意义
        return -1; // 应该抛出异常
    }
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    for(int i=1; i<=m; ++i){
        for(int j=i; j<=n; ++j){
            if(i == j){ // 对角线为积累和
                dp[i][j] = dp[i-1][j-1] + arr[i-1];
            }else{
                // 情况1：加入第 i 个子序列
                int tmp = dp[i][j-1] + arr[j];
                // 情况2：单独作为第 i 个子序列
                for(int k=i-1; k<j; ++k){
                    tmp = max(dp[i-1][k]+arr[j], tmp);
                }
                // 两种情况中的最大值
                dp[i][j] = tmp;
            }
        }
    }
    // max{dp[m][i] | m<= i <= n}
    int ret = dp[m][m];
    for(int i=m+1; i<=n; ++i){
        ret = max(ret, dp[m][i]);
    }
    return ret;
}

int max_m_subsum2(vector<int> arr, int m){
    /* 事实上并不需要计算整个 dp，只需要计算一个平行四边形区域
    */
    int n = arr.size();
    if(m > n){      // m > n 时没有意义
        return -1;  // 应该抛出异常
    }
    vector<vector<int>> dp(m+1, vector<int>(n+1, 0));
    int step = n-m; // 平行四边形的底边长-1，高为 m
    for(int i=1; i<=m; ++i){
        for(int j=i; j<=i+step; ++j){
            if(i == j){ // 对角线为积累和
                dp[i][j] = dp[i-1][j-1] + arr[i-1];
            }else{
                // 情况1：加入第 i 个子序列
                int tmp = dp[i][j-1] + arr[j];
                // 情况2：单独作为第 i 个子序列
                for(int k=i-1; k<j; ++k){
                    tmp = max(dp[i-1][k]+arr[j], tmp);
                }
                // 两种情况中的最大值
                dp[i][j] = tmp;
            }
        }
    }
    // max{dp[m][i] | m<= i <= n}
    int ret = dp[m][m];
    for(int i=m+1; i<=n; ++i){
        ret = max(ret, dp[m][i]);
    }
    return ret;
}

int max_m_subsum2(vector<int> arr, int m){
    /* 
    1. 事实上并不需要存储整个 dp，只需用两个一维数组滚动存储即可
    2. 情况2中，并不需要反复计算最大值，只需要一个变量保存以前的最大值，和当前值作比较即可
    */
    int n = arr.size();
    if(m > n){      // m > n 时没有意义
        return -1;  // 应该抛出异常
    }
    vector<vector<int>> dp(2, vector<int>(n+1, 0));
    int step = n-m, pre_max=0; // 平行四边形的底边长-1，高为 m
    for(int i=1; i<=m; ++i){
        for(int j=i; j<=i+step; ++j){
            if(i == j){ // 对角线为积累和
                dp[i%2][j] = dp[(i-1)%2][j-1] + arr[i-1];
                pre_max = dp[(i-1)%2][j-1];
            }else{
                // 情况1：加入第 i 个子序列
                int tmp = dp[i%2][j-1] + arr[j];
                // 情况2：单独作为第 i 个子序列
                pre_max = max(pre_max, dp[(i-1)%2][j-1]);
                // 两种情况中的最大值
                dp[i%2][j] = max(tmp, pre_max+arr[j]);
            }
        }
    }
    // max{dp[m][i] | m<= i <= n}
    int ret = dp[m%2][m];
    for(int i=m+1; i<=n; ++i){
        ret = max(ret, dp[m%2][i]);
    }
    return ret;
}