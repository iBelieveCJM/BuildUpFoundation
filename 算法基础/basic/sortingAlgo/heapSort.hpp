#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using std::vector;
using std::multiset;

void heapSort(vector<int>& arr){
    multiset<int, std::less<int> > heap;
    for(int e: arr){
        heap.insert(e);
    }
    //multiset<int, std::less<int> >::iterator mset_it = heap.begin();
    //vector<int>::iterator vec_it = arr.begin();
    //while(mset_it != heap.end()){
    //    *vec_it = *mset_it;
    //    ++vec_it;
    //    ++mset_it;
    //}
    std::copy(heap.begin(), heap.end(), arr.begin());
}


