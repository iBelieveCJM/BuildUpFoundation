#include<iostream>
#include<vector>
using std::vector;

static int biSearch(vector<int>& stortedArr, int target, int low, int high);
static int seqSearchOrdered(vector<int>& stortedArr, int target, int low, int high);
typedef int (*searchAlgo)(vector<int>&, int, int, int);

#ifdef BI_SEARCH
searchAlgo search = biSearch;
#elif SEQ_SEARCH
searchAlgo search = seqSearchOrdered;
#endif
void insertSort(vector<int>& arr){
    for(int i=1; i<arr.size(); ++i){
        int cur = arr[i];
        int pos = search(arr, cur, 0, i);
        for(int j=i; j>pos; --j){
            arr[j] = arr[j-1];
        }
        arr[pos] = cur;
        //for(int e:arr) std::cout<< "  " << e ; std::cout<<std::endl; // for test
    }
}

static int biSearch(vector<int>& stortedArr, int target, int low, int high){
    while(low <= high){
        int mid = (low+high)/2;
        if(stortedArr[mid]==target){
            return mid;
        }
        else if(stortedArr[mid]<target){
            low = mid + 1;
        }
        else if(stortedArr[mid]>target){
            high = mid - 1;
        }
    }
    return low;
}

static int seqSearchOrdered(vector<int>& stortedArr, int target, int low, int high){
    int i = low;
    for(; i<high+1;++i){
        if(target<=stortedArr[i])
            break;
    }
    return i;
}

void insertSort_raw(vector<int>& arr){
    for(int i=1; i<arr.size(); ++i){
        int cur = arr[i];
        int pos = 0;
        for(; pos < i; ++pos){
            if(cur < arr[pos]){ //question: '<' or '<='
                break;
            }
        }
        for(int j=i; j>pos; --j){
            arr[j] = arr[j-1];
        }
        arr[pos] = cur;
    }
}


