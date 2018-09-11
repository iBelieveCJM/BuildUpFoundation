#include<iostream>
#include<vector>
using std::vector;

void simpleSelectSort(vector<int>& arr){
    int arr_size = arr.size();
    for(int i=0; i<arr_size; ++i){
        int min_index = i;
        for(int j=i+1; j<arr_size; ++j){
            if(arr[min_index] > arr[j]){
                min_index = j;
            }
        }
        if(min_index != i){
            int temp = arr[min_index];
            arr[min_index] = arr[i];
            arr[i] = temp;
        }
    }
}


