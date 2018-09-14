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
        if(pos[i] == pos[step]){
            return false;
        }
    }
    return true;
}
template<typename T>
void permutation_(vector<T>& arr, vector<int>& pos, int step){
    if(step == pos.size() ){
        printPartialVec(arr, pos);
#ifdef DEBUG
        ++count;
#endif
    }
    else{
        for(int i=0; i!=arr.size(); ++i){
            pos[step] = i;
            if( is_ok(pos, step) ){
                permutation_(arr, pos, step+1);
            }
        }
    }
}
template<typename T>
void permutation(vector<T>& arr, int n){
    if(n >= arr.size()){
        return; // error, should throw exception.
    }
    vector<int> pos(n, 0);
    permutation_(arr, pos, 0);
}

int main(){
    //vector<int> arr = {2,3,4};
    vector<char> arr = {'a', 'b', 'c', 'd'};
    permutation(arr, 1);
#ifdef DEBUG
    std::cout << "total solution: " << count << std::endl;
#endif
    return 0;
}