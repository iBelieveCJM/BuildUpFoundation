#include<iostream>
#include<vector>
using std::vector;

typedef int (*searchAlgo)(vector<int>&, int);
#include"biSearch.hpp"
#include"seqSearch.hpp"

#ifdef BI_SEARCH
searchAlgo search = biSearch;
#elif SEQ_SEARCH
searchAlgo search = seqSearchOrdered;
#endif

void testValidTargetOnMid();
void testValidTargetOnMid2();
void testValidTargetOnLow();
void testValidTargetOnUp();
void testValidTargetNotOnMid();
void testValidTargetNotOnLow();
void testValidTargetNotOnUp();


int main(){
	testValidTargetOnMid();
	testValidTargetOnMid2();
	testValidTargetOnLow();
	testValidTargetOnUp();
	testValidTargetNotOnMid();
	testValidTargetNotOnLow();
	testValidTargetNotOnUp();
	return 0;
}

void testValidTargetOnMid(){
	std::cout<< "test valid target on the mid pos" << std::endl;
	int target = 5;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,9,10};
	int pos = search(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetOnMid2(){
	std::cout<< "test valid target on the array with repeated element" << std::endl;
	int target = 5;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,8,8,9,10};
	int pos = search(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetOnLow(){
	std::cout<< "test valid target on the low pos" << std::endl;
	int target = -1;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,9,10};
	int pos = search(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetOnUp(){
	std::cout<< "test valid target on the up pos" << std::endl;
	int target = 10;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,9,10};
	int pos = search(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetNotOnMid(){
	int target = 5;
	vector<int> stortedArr = {-1,2,3,4,6,7,8,9,10};
	int pos = search(stortedArr, target);
	if(pos == 4){
		std::cout<< "find the pos " << pos << " successfully " << std::endl;
	}
	else{
		std::cout<< "falied,  the finded pos is " << pos  << std::endl;
	}
}

void testValidTargetNotOnLow(){
	int target = -2;
	vector<int> stortedArr = {-1,2,3,4,6,7,8,9,10};
	int pos = search(stortedArr, target);
	if(pos == 0){
		std::cout<< "find the pos " << pos << " successfully " << std::endl;
	}
	else{
		std::cout<< "falied,  the finded pos is " << pos  << std::endl;
	}
}

void testValidTargetNotOnUp(){
	int target = 11;
	vector<int> stortedArr = {-1,2,3,4,6,7,8,9,10};
	int pos = search(stortedArr, target);
	if(pos == 9){
		std::cout<< "find the pos " << pos << " successfully " << std::endl;
	}
	else{
		std::cout<< "falied,  the finded pos is " << pos  << std::endl;
	}
}
