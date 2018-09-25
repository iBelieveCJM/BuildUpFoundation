#include<iostream>
#include<vector>
#include<set>
#include<algorithm>
using std::vector;
using std::multiset;

void heapSort_multiset(vector<int>& arr){
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

void swap(int &a, int &b){
    if(&a == &b){
        return ;
    }
    int temp = a;
    a = b;
    b = temp;
}
/*
 * adjust head from top to bottom
*/
void adjustMaxHeap(vector<int>& heap, int i, int len){
    int temp = heap[i];
    // left node: i*2+1; right node: i*2+2
    for(int j=i*2+1; j<len; j=j*2+1){
        // if right node exists and left node is less than right node
        if(j+1<len && heap[j]<heap[j+1]){
            ++j;
        }
        // if child is greater than father
        // pass the value from child to father
        // then go on adjusting the head.
        if(heap[j] > temp){
            heap[i] = heap[j];
            i = j;
        }
        // if father is greater
        else{
            break;
        }
    }
    heap[i] = temp;
}
void heapSort(vector<int>& arr){
    if(arr.empty()){
        return;
    }
    // make the head
    int len = arr.size();
    for(int i=len/2-1; i>=0; --i){
        adjustMaxHeap(arr, i, len);
    }
    // sorting
    for(int j=len-1; j>0; --j){
        swap(arr[0], arr[j]);
        adjustMaxHeap(arr, 0, j);
    }
}


