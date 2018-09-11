#include<iostream>
#include<vector>
using std::vector;

int partition(vector<int>& arr, int left, int right){
    int povit = arr[left];
    //std::cout << "pos: " << left << "    povit: " << povit << std::endl;
    while(left < right){   //note. '<' less than, not less and equal(dead loop) 
        while(arr[right]>povit && left<right){ //note. if no left<right, it will out of range

            --right;
        }
        arr[left] = arr[right];
        
        while(arr[left]<povit && left<right){ 
	    ++left;
        }
        arr[right] = arr[left];
    }
    arr[left] = povit;    //note. store the povit
    return left;          //note. return the position of povit
}

static void quickSort_(vector<int>& arr, int left, int right){
    if(left>=right)
        return;
    int povit = partition(arr, left, right);
    //std::cout<< "....povit... " << povit << std::endl;
    quickSort_(arr, left, povit-1);  //note. povit-1
    quickSort_(arr, povit+1, right); //note. povit+1
}

void quickSort(vector<int>& arr){
    quickSort_(arr, 0, arr.size()-1);
}
