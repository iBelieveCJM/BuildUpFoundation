#include<iostream>
#include<vector>
using std::vector;

void testValidTargetOnMid();
void testValidTargetOnMid2();
void testValidTargetOnLow();
void testValidTargetOnUp();
void testValidTargetNotOnMid();
void testValidTargetNotOnLow();
void testValidTargetNotOnUp();
int biSearch(vector<int>& stortedArr, int target);
static int biSearch_find_rec(vector<int>& stortedArr, int target, int low, int high);
static int biSearch_find_loop(vector<int>& stortedArr, int target, int low, int high);
int biSearch1(vector<int>& stortedArr, int target);
static int biSearch_find1(vector<int>& stortedArr, int target, int low, int high);

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

int biSearch(vector<int>& stortedArr, int target){
	int arrSize = stortedArr.size();
	int low = 0;
	int high = arrSize-1;
	return biSearch_find_loop(stortedArr, target, low, high);
}
static int biSearch_find_rec(vector<int>& stortedArr, int target, int low, int high){
	if(low <= high){
		int mid = (low+high)/2;
		if(stortedArr[mid] == target){
			return mid;
		}
		else if(stortedArr[mid] > target){
			return biSearch_find_rec(stortedArr, target, low, mid-1);
		}
		else if(stortedArr[mid] < target){
			return biSearch_find_rec(stortedArr, target, mid+1, high);
		}
	}
	return low;
}
static int biSearch_find_loop(vector<int>& stortedArr, int target, int low, int high){
	while(low <= high){
		int mid = (low+high)/2;
		if(stortedArr[mid] == target){
			return mid;
		}
		else if(stortedArr[mid] > target){
			high = mid-1;
		}
		else if(stortedArr[mid] < target){
			low = mid+1;
		}
	}
	
	return low;
}

int biSearch1(vector<int>& stortedArr, int target){
	int arrSize = stortedArr.size();
	if(arrSize==0 || stortedArr[0]>target){
		return 0;
	}
	if(stortedArr[arrSize-1]<target){
		return arrSize;
	}
	int low = 0;
	int high = arrSize-1;
	return biSearch_find1(stortedArr, target, low, high);
}
static int biSearch_find1(vector<int>& stortedArr, int target, int low, int high){
	int mid = (low+high)/2;
	if(stortedArr[mid] == target){
		return mid;
	}
	else if(low==high){
		return low+1;
	}
	else if(stortedArr[mid] > target){
		return biSearch_find1(stortedArr, target, low, mid-1);
	}
	else if(stortedArr[mid] < target){
		return biSearch_find1(stortedArr, target, mid+1, high);
	}
}

void testValidTargetOnMid(){
	std::cout<< "test valid target on the mid pos" << std::endl;
	int target = 5;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,9,10};
	int pos = biSearch(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetOnMid2(){
	std::cout<< "test valid target on the array with repeated element" << std::endl;
	int target = 5;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,8,8,9,10};
	int pos = biSearch(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetOnLow(){
	std::cout<< "test valid target on the low pos" << std::endl;
	int target = -1;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,9,10};
	int pos = biSearch(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetOnUp(){
	std::cout<< "test valid target on the up pos" << std::endl;
	int target = 10;
	vector<int> stortedArr = {-1,2,3,4,5,6,7,8,9,10};
	int pos = biSearch(stortedArr, target);
	if(stortedArr[pos]==target){
		std::cout<< "find the target " << target << " successfully in " << pos << std::endl;
	}
}

void testValidTargetNotOnMid(){
	int target = 5;
	vector<int> stortedArr = {-1,2,3,4,6,7,8,9,10};
	int pos = biSearch(stortedArr, target);
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
	int pos = biSearch(stortedArr, target);
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
	int pos = biSearch(stortedArr, target);
	if(pos == 9){
		std::cout<< "find the pos " << pos << " successfully " << std::endl;
	}
	else{
		std::cout<< "falied,  the finded pos is " << pos  << std::endl;
	}
}
