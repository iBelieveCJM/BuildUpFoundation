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
    for_each(arr.begin(), arr.end(), print);
    std::cout<<std::endl;
}

bool is_ok(vector<int>& pos, int step){
    for(int i=0; i<step; ++i){
        if( (pos[i]==pos[step]) || (abs(pos[i]-pos[step])==abs(i-step)) ){
            return false;
        }
    }
    return true;
}

void Queen1(int num){
    vector<int> pos(num, 0);
    int step = 0;
    int count = 0;
    // if the position of first queen is out of the end, stop.
    while(pos[0]!=num){
        // if the position is not ok (need not check when step is 0, it's ok always)
        // then try next position
        if(step>0 && (!is_ok(pos, step)) ){
            ++pos[step];
        }
        // if the pos is ok
        else{
            // if all queen is all right
            // output the result and try next position
            if(step == (num-1)){
                ++count;
                printVec(pos);
                ++pos[step];
            }
            // otherwise, try next queen
            else{
                ++step;
            }
        }
        // if the position is out of the end (that is, we have tried all the position of current queen)
        // then back track to previous queen and try the it's next position
        // We skip the first queen(step>0), for we use it as final condition to stop.
        while(step>0 && pos[step]==num){
            pos[step] = 0;
            --step;
            ++pos[step];
        }
    }
    std::cout<< "total solutions: " << count << std::endl;
}


void queen_(vector<int>& pos, int col, int num, int& count){
    if(col == num){
        count++;
        printVec(pos);
    }
    else{
        for(int row=0; row!=num; ++row){
            pos[col] = row;
            if( is_ok(pos, col) ){
                queen_(pos, col+1, num, count);
            }
        }
    }
}
void Queen2(int num){
    int count = 0;
    vector<int> pos(num, 0);
    queen_(pos, 0, num, count);
    std::cout<< "total solutions: " << count << std::endl;
}

int main(){
    Queen1(8);
    Queen2(8);
    return 0;
}