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
bool is_ok(vector<int>& pos, int step, bool is_permutation){
    for(int i=0; i<step; ++i){
        if(is_permutation){
            if(is_permutation && pos[i] == pos[step]){
                return false;
            }
        }
        else{
            if(is_permutation || pos[i] >= pos[step]){
                return false;
            }
        }
    }
    return true;
}
template<typename T>
void combination_permutation_(vector<T>& arr, vector<int>& pos, int step, bool is_permutation){
    if(step == pos.size() ){
        printPartialVec(arr, pos);
#ifdef DEBUG
        ++count;
#endif
    }
    else{
        for(int i=0; i!=arr.size(); ++i){ //note. i starts from 0.
            pos[step] = i;
            if( is_ok(pos, step, is_permutation) ){
                combination_permutation_(arr, pos, step+1, is_permutation);
            }
        }
    }
}
template<typename T>
void combination_permutation(vector<T>& arr, int n, bool is_permutation){
    if(n >= arr.size()){
        return; // error, should throw exceptions.
    }
    vector<int> pos(n, 0);
    combination_permutation_(arr, pos, 0, is_permutation);
}

template<typename T>
void combination(vector<T>& arr, int n){
#ifdef DEBUG
    std::cout << "combination!" << std::endl;
#endif
    combination_permutation(arr, n, false);
}

template<typename T>
void permutation(vector<T>& arr, int n){
#ifdef DEBUG
    std::cout << "permutation!" << std::endl;
#endif
    combination_permutation(arr, n, true);
}

int main(){
    //vector<int> arr = {1,2,3};
    vector<char> arr = {'a', 'b', 'c', 'd'};
    combination(arr, 2);
    //permutation(arr, 2);
#ifdef DEBUG
    std::cout << "total solution: " << count << std::endl;
#endif
    return 0;
}