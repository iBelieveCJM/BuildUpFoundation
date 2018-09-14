#ifdef DEBUG
#include<iostream>
#endif

#include<vector>
#include<stdlib.h>
using std::vector;

#ifdef DEBUG
int count = 0;
#endif

template<typename T>
void printPartialVec(vector<T>& arr, vector<int>& pos){
    for(int i=0; i<pos.size(); ++i){
        std::cout<< arr[pos[i]] << "  ";
    }        
    std::cout<<std::endl;
}
bool is_ok(vector<int>& pos, int step){
    for(int i=0; i<step; ++i){
        if(pos[i] >= pos[step]){ //note. here must be '>='. Actually, it is the only diffenence from permutation
            return false;
        }
    }
    return true;
}
template<typename T>
void combination_(vector<T>& arr, vector<int>& pos, int step){
    if(step == pos.size() ){
        printPartialVec(arr, pos);
#ifdef DEBUG
        ++count;
#endif
    }
    else{
        for(int i=step; i!=arr.size(); ++i){ //note. i starts from step for optimition. It can start from 0.
            pos[step] = i;
            if( is_ok(pos, step) ){
                combination_(arr, pos, step+1);
            }
        }
    }
}
template<typename T>
void combination(vector<T>& arr, int n){
    if(n >= arr.size()){
        return; // error, should throw exceptions.
    }
    vector<int> pos(n, 0);
    combination_(arr, pos, 0);
}

int main(){
    //vector<int> arr = {1,2,3};
    vector<char> arr = {'a', 'b', 'c', 'd'};
    combination(arr, 2);
#ifdef DEBUG
    std::cout << "total solution: " << count << std::endl;
#endif
    return 0;
}