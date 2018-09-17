#include<iostream>
#include"../basicStruct/dynamicLink.hpp"

typedef dynamicLink::Node linkNode;
typedef void (*sortingAlgo)(linkNode*);

#ifdef QUICK_SORT
#include"quickSort_link.hpp"
sortingAlgo sort = quickSort_link;
#elif BUBBLE_SORT
#include"bubbleSort_link.hpp"
sortingAlgo sort = bubbleSort_link;
#elif INSERT_SORT
#include"insertSort_link.hpp"
sortingAlgo sort = insertSort_link;
#endif

void testUnorderedOdd();
void testUnorderedEven();
void testInvOdd();
void testInvEven();
void testRepetitionOdd();
void testRepetitionEven();

int main(){
    testUnorderedOdd();
    testUnorderedEven();
    testInvOdd();
    testInvEven();
    testRepetitionOdd();
    testRepetitionEven();
    return 0;
}

void testUnorderedOdd(){
    dynamicLink testlink = {9, 4, 111, 0, -4, 12, -8};
    //testlink.printLink();
    dynamicLink verlink = {-8, -4, 0, 4, 9, 12, 111};
    sort(testlink.getHead());
    if(verlink.equals(testlink)){
        std::cout<< "sorted the unordered and odd link successfully" << std::endl;
    }
    testlink.printLink();
}

void testUnorderedEven(){
    dynamicLink testlink = {9, 4, 111, 0, -4, 12};
    dynamicLink verlink = {-4, 0, 4, 9, 12, 111};
    sort(testlink.getHead());
    if(verlink.equals(testlink)){
        std::cout<< "sorted the unordered and even link successfully" << std::endl;
    }
    testlink.printLink();
}

void testUnorderedEven();

void testInvOdd(){
    dynamicLink testlink = {5, 4, 1, 0, -4};
    dynamicLink verlink = {-4, 0, 1, 4, 5};
    sort(testlink.getHead());
    if(verlink.equals(testlink)){
        std::cout<< "sorted the inv and odd link successfully" << std::endl;
    }
    testlink.printLink();
}

void testInvEven(){
    dynamicLink testlink = {5, 4, 1, 0, -4, -7};
    dynamicLink verlink = {-7, -4, 0, 1, 4, 5};
    sort(testlink.getHead());
    if(verlink.equals(testlink)){
        std::cout<< "sorted the inv and even link successfully" << std::endl;
    }
    testlink.printLink();
}

void testRepetitionOdd(){
    dynamicLink testlink = {9, 4, 111, 0, 0, -4, 12};
    dynamicLink verlink = {-4, 0, 0, 4, 9, 12, 111};
    sort(testlink.getHead());
    if(verlink.equals(testlink)){
        std::cout<< "sorted the odd link which has repeated elements successfully" << std::endl;
    }
    testlink.printLink();
}

void testRepetitionEven(){
    dynamicLink testlink = {9, 4, 111, 0, 0, -4, 12, 0};
    dynamicLink verlink = {-4, 0, 0, 0, 4, 9, 12, 111};
    sort(testlink.getHead());
    if(verlink.equals(testlink)){
        std::cout<< "sorted the even link which has repeated elements successfully" << std::endl;
    }
    testlink.printLink();
}