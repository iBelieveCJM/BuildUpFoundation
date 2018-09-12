#include<iostream>
#include<vector>
using std::vector;

void merge(vector<int>& arr, vector<int>& temp, int left, int right, int mid){
    int first = left;
    int second = mid+1;
    int ind = left;
    while(first<=mid && second<=right && ind<=right){
        if(arr[first] <= arr[second]){
            temp[ind++] = arr[first++];
        }
        else if(arr[first] > arr[second]){
            temp[ind++] = arr[second++];
        }
    }
    while(first<=mid && ind<=right){
        temp[ind++] = arr[first++];
    }
    while(second<=right && ind<=right){
        temp[ind++] = arr[second++];
    }
    for(int i=left; i<=right; ++i){
        arr[i] = temp[i];
    }
}


static void mergeSort_(vector<int>& arr, vector<int>& temp, int left, int right){
    if(left==right)
        return;
    int mid = (left+right)/2;
    mergeSort_(arr, temp, left, mid);
    mergeSort_(arr, temp, mid+1, right);
    merge(arr, temp, left, right, mid);
    for(int e:arr) std::cout<< "  " << e; std::cout<<std::endl;
}

void mergeSort(vector<int>& arr){
    vector<int> temp(arr.size(), 0);
    mergeSort_(arr, temp, 0, arr.size()-1);
}
