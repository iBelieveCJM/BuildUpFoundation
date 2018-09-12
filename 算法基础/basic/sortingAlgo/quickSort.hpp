#include<iostream>
#include<vector>
using std::vector;

int partition0(vector<int>& arr, int left, int right){
    int povit = arr[left];
    std::cout << "pos: " << left << "    povit: " << povit << std::endl;
    while(left < right){   //note. '<' less than, not less and equal(dead loop)
        //note. if no left<right, it will out of range
        //note. there '>=' and next '<', it must have '=' in one condition
        //      or '>' and '<='
        //note. you must start from right side
        while(arr[right]>=povit && left<right){
            --right;
        }
        arr[left] = arr[right];
        
        while(arr[left]<=povit && left<right){ 
            ++left;
        }
        arr[right] = arr[left];
    }
    arr[left] = povit;    //note. store the povit
    return left;          //note. return the position of povit
}

int partition1(vector<int>& arr, int left, int right){
    int left_pre = left;   //note. keep the previous left postion
    int povit = arr[left_pre];
    while(left < right){   //note. '<' less than, not less and equal(dead loop)
        while(arr[right]>povit && left<right){  // note. here, the compare operator can be '>' or '>='
            --right;
        }
        while(arr[left]<=povit && left<right){  // note. here, the compare operator must be '<='
            ++left;
        }
        if(left < right){
            int temp = arr[left];
            arr[left] = arr[right];
            arr[right] = temp;
        }
    }
    //note. should put the povit in right place.
    arr[left_pre] = arr[left];
    arr[left] = povit;
    return left;
}


static void quickSort_(vector<int>& arr, int left, int right){
    if(left>=right)
        return;
    int povit = partition0(arr, left, right);
    //std::cout<< "....povit... " << povit << std::endl;
    quickSort_(arr, left, povit-1);  //note. povit-1
    quickSort_(arr, povit+1, right); //note. povit+1
}

void quickSort(vector<int>& arr){
    quickSort_(arr, 0, arr.size()-1);
}
