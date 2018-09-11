#include<iostream>
#include<vector>
using std::vector;

void bubbleSort(vector<int>& arr){
    for(int i=0; i<arr.size(); ++i){
        bool flag = false;
        for(int j=0; j<arr.size()-i-1; ++j){
            if(arr[j]>arr[j+1]){   //note. '>' make it stable 
                int temp = arr[j];
                arr[j] = arr[j+1];
                arr[j+1] = temp;
                flag = true;
            }
        }
        //for(int e:arr) std::cout<< "  " << e ; std::cout<<std::endl; // for tests
        if(flag == false){
            break;  // return;
        }
    }
}


