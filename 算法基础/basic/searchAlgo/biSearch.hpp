#include<iostream>
#include<vector>
using std::vector;

int biSearch(vector<int> stortedArr, int target){
    int low = 0;
    int high = stortedArr.size()-1;
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
