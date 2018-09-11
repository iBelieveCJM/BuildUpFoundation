#include<iostream>
#include<vector>
using std::vector;

int seqSearchOrdered(vector<int>& stortedArr, int target){
    int i = 0;
    for(; i<stortedArr.size();++i){
        //std::cout<< "target: " << target << "   element: " << stortedArr[i] << std::endl;
        if(target<=stortedArr[i])
            break;
    }
    return i;
}

int seqSearch(vector<int>& stortedArr, int target){
    int i = 0;
    for(; i<stortedArr.size();++i){
        if(stortedArr[i]==target)
            break;
    }
    return i;
}