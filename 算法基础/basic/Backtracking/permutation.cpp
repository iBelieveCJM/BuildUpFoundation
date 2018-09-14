#ifdef DEBUG
#include<iostream>
#endif

#include<vector>
#include<stdlib.h>
using std::vector;

template<typename T>
void printVec(vector<T>& arr){
    for(T e: arr) std::cout<< e << "  ";
    std::cout<<std::endl;
}

template<typename T>
void swap(T& a, T& b){
    if(&a == &b){
        return;
    }
    T temp = a;
    a = b;
    b = temp;
}

#ifdef DEBUG
int count = 0;
#endif

template<typename T>
void fullPermutation(vector<T>& arr, int pos){
    if(pos == (arr.size()-1) ){
        printVec(arr);
#ifdef DEBUG
        ++count;
#endif
        return;
    }
    for(int i=pos; i<arr.size(); ++i){
        swap(arr[pos], arr[i]);
        fullPermutation(arr, pos+1);
        swap(arr[pos], arr[i]);
    }
}

int main(){
    //vector<int> arr = {2,3,4};
    vector<char> arr = {'a', 'b', 'c', 'd'};
    fullPermutation(arr, 0);
#ifdef DEBUG
    std::cout << "total solution: " << count << std::endl;
#endif
    return 0;
}