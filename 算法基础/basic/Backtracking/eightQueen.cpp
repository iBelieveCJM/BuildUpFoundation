#include<iostream>
#include<vector>
#include<stdlib.h>
#include<algorithm>
using std::vector;
using std::for_each;

void print(int x){
    std::cout<< x << "  ";
}
void printVec(vector<int>& arr){
    for_each(arr.begin(), arr.end(), print); std::cout<<std::endl;
}
bool is_not_suit(vector<int>& pos, int step){
    bool ret = false;
    for(int i=0; i<step; ++i){
        ret = (ret || (pos[i]==pos[step]) || (abs(pos[i]-pos[step])==abs(i-step)) );
    }
    return ret;
}

void eightQueen(int num){
    vector<int> pos(num, 0);
    int step = 0;
    int count = 0;
    while(pos[0]!=num){
        if(step>0 && is_not_suit(pos, step)){
            ++pos[step];
        }
        else{
            if(step == (num-1)){
                printVec(pos);
                ++pos[step];
                ++count;
            }
            else{
                ++step;
            }
        }
        while(step>0 && pos[step]==num){
            pos[step] = 0;
            --step;
            ++pos[step];
        }
    }
    std::cout<< "total solutions: " << count << std::endl;
}

int main(){
    eightQueen(8);
    return 0;
}