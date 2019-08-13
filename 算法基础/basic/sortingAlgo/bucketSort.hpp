// 桶排序
// 基本思想：
//  将一个数据表分割成许多 buckets，每个 bucket 有序排列，
//  把每个元素分配到其对应的 buckets，再顺序地收集回来

#include<vector>
using std::vector;

void countSort(vector<int>& arr){
    /* 计数排序
    类似于位图法，统计[min_val, max_val]区间内所有元素的出现次数
    */
    if(arr.size() < 2){
        return;
    }
    // 获取最大值max_val, 最小值min_val
    int max_val=arr[0], min_val=arr[0];
    for(const auto& x: arr){
        min_val = (x<min_val)? x: min_val;
        max_val = (x>max_val)? x: max_val;
    }
    // 创建可容纳 [min_val, max_val] 区间所有元素的桶
    int n_bucket = max_val - min_val +1;
    vector<int> buckets(n_bucket, 0);
    // 分配：统计 arr 中元素在 buckets 中的出现次数
    for(const auto& x: arr){
        ++buckets[x-min_val];
    }
    // 收集：遍历所有桶，顺序地收集分配的元素
    for(int i=0, idx=0; i<n_bucket; ++i){
        for(int j=0; j<buckets[i]; ++j){
            arr[idx++] = i+min_val;
        }
    }
}

void radixSortLSD(vector<int>& arr, int base=10){
    /* 基数排序（对整数排序）
    对正整数的每个数位进行计数排序，从低位开始(LSD)
    */
    if(arr.size() < 2){
        return;
    }
    int exp=1, max_val=0;
    for(const auto& x: arr){
        max_val = (x>max_val)? x: max_val;
    }
    vector<int> collector(arr.size());
    vector<int> buckets(base, 0);
    while(max_val/exp > 0){
        // 每次使用前，桶清零
        fill(buckets.begin(), buckets.end(), 0);
        // 分配：对数位进行计数
        for(const auto& x: arr){
            ++buckets[ (x/exp)%base ];
        }
        for(int i=1; i<buckets.size(); ++i){
            buckets[i] += buckets[i-1];
        }
        // 收集：顺序按统计次数进行排序
        for(int i=arr.size()-1; i>=0; --i){
            collector[--buckets[(arr[i]/exp)%base]] = arr[i];
        }
        arr.assign(collector.begin(), collector.end());
        // 下一个（更高的）数位
        exp *= base;
    }
}

/*
* TODO: 桶排序（动态指针版）
*/

/*
* TODO: 桶排序（静态指针版）
*/