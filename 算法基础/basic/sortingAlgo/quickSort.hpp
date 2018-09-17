#include<iostream>
#include<vector>
using std::vector;

int partition0(vector<int>& arr, int left, int right){
    int pivot = arr[left];
    std::cout << "pos: " << left << "    pivot: " << pivot << std::endl;
    while(left < right){   //note. '<' less than, not less and equal(dead loop)
        //note. if no left<right, it will out of range
        //note. there '>=' and next '<', it must have '=' in one condition
        //      or '>' and '<='
        //note. you must start from right side
        while(arr[right]>=pivot && left<right){
            --right;
        }
        arr[left] = arr[right];
        
        while(arr[left]<=pivot && left<right){ 
            ++left;
        }
        arr[right] = arr[left];
    }
    arr[left] = pivot;    //note. store the pivot
    return left;          //note. return the position of pivot
}

void swap(int& a, int& b){
    if(&a == &b){
        return ;
    }
    int temp = a;
    a = b;
    b = temp;
}
int partition1(vector<int>& arr, int left, int right){
    int left_pre = left;   //note. keep the previous left postion
    int pivot = arr[left_pre];
    std::cout << "pos: " << left << "    pivot: " << pivot << std::endl;
    while(left < right){   //note. '<' less than, not less and equal(dead loop)
        while(arr[right]>pivot && left<right){  // note. here, the compare operator can be '>' or '>='
            --right;
        }
        while(arr[left]<=pivot && left<right){  // note. here, the compare operator must be '<='
            ++left;
        }
        if(left < right){
            swap(arr[left], arr[right]);
        }
    }
    //note. should put the pivot in right place. swap(arr[left_pre], arr[left])
    arr[left_pre] = arr[left];
    arr[left] = pivot;
    return left;
}

int partition2(vector<int>& arr, int left, int right){
    int pivot = arr[left];
    std::cout << "pos: " << left << "    pivot: " << pivot << std::endl;
    int greater_index = left;
    int less_index = left;
    while(greater_index <= right){
        if(arr[greater_index] < pivot){
            swap(arr[++less_index], arr[greater_index]);
        }
        ++greater_index;
    }
    swap(arr[left], arr[less_index]);
    return less_index;
}

static void quickSort_(vector<int>& arr, int left, int right){
    if(left>=right)
        return;
    int pivot = partition2(arr, left, right);
    //std::cout<< "....pivot... " << pivot << std::endl;
    quickSort_(arr, left, pivot-1);  //note. pivot-1
    quickSort_(arr, pivot+1, right); //note. pivot+1
}

void quickSort(vector<int>& arr){
    quickSort_(arr, 0, arr.size()-1);
}

// using a stack to keep the bound
void quickSort_unrecursion(vector<int>& arr){
    if(arr.size()==0 || arr.size()==1){
        return;
    }
    int stack[2000];
    int top = -1;
    stack[++top] = 0;
    stack[++top] = arr.size()-1;
    // if stack is not empty
    while(top>0){
        //note. stack is first in last out
        //      so we get right first then left
        int right = stack[top--];
        int left = stack[top--];
        int pivot = partition0(arr, left, right);
        //if the right sub array has element
        if(pivot+1 < right){
            stack[++top] = pivot+1;
            stack[++top] = right;
        }
        //if the left sub array has element
        if(left < pivot-1){
            stack[++top] = left;
            stack[++top] = pivot-1;
        }
    }
}