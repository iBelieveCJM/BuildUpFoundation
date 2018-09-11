#include<iostream>
#include<vector>
using std::vector;

typedef void (*sortingAlgo)(vector<int>&);
#include"quickSort.hpp"
#include"insertSort.hpp"

#ifdef QUICK_SORT
sortingAlgo sort = quickSort;
#elif INSERT_SORT
sortingAlgo sort = insertSort;
#endif

bool is_equal(const vector<int>& source, const vector<int>& target);
void testOrdered();
void testInv();
void testRepition();


int main(){
    testOrdered();
    testInv();
    testRepition();
	return 0;
}

bool is_equal(const vector<int>& source, const vector<int>& target){
    if(source.size() != target.size()){
        return false;
    }
    bool ret = true;
    for(int i=0; ret&&i<source.size(); ++i){
        if(source[i] != target[i])
            ret = false;
    }
    return ret;
}

void testOrdered(){
	std::cout<< "test ordered array" << std::endl;
    vector<int> source = {-1,0,11,-3,10,3,6,7,9};
	vector<int> target = {-3,-1,0,3,6,7,9,10,11};
	sort(source);
    //partition(source, 0, source.size()-1);
	if(is_equal(source, target)){
		std::cout<< "sorting successfully!" << std::endl;
	}
    else{
        std::cout<< "sorting faild!, arr is " << std::endl;
        for(int e:source) std::cout<< "  " << e ;
        std::cout<<std::endl;
    }
}

void testInv(){
	std::cout<< "test inv array" << std::endl;
    vector<int> source = {11,10,9,7,6,3,0,-1,-3};
	vector<int> target = {-3,-1,0,3,6,7,9,10,11};
	sort(source);
    //partition(source, 0, source.size()-1);
	if(is_equal(source, target)){
		std::cout<< "sorting successfully!" << std::endl;
	}
    else{
        std::cout<< "sorting faild!, arr is " << std::endl;
        for(int e:source) std::cout<< "  " << e ;
        std::cout<<std::endl;
    }
}

void testRepition(){
	std::cout<< "test repition array" << std::endl;
    vector<int> source = {11,10,7,7,3,0,-1,-3,7};
	vector<int> target = {-3,-1,0,3,7,7,7,10,11};
	sort(source);
    //partition(source, 0, source.size()-1);
	if(is_equal(source, target)){
		std::cout<< "sorting successfully!" << std::endl;
	}
    else{
        std::cout<< "sorting faild!, arr is " << std::endl;
        for(int e:source) std::cout<< "  " << e ;
        std::cout<<std::endl;
    }
}
