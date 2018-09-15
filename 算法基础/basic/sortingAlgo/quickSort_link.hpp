#include<iostream>
#include"../basicStruct/dynamicLink.hpp"

typedef dynamicLink::Node linkNode;

void swap_val(linkNode* a, linkNode* b){
    if(a == b){
        return;
    }
    int temp = a->val;
    a->val = b->val;
    b->val = temp;
}
///////////////////
// the idea seems like remove the repeated elements in a ordered array
///////////////////
linkNode* partition_val(linkNode* left, linkNode* right){
    linkNode* povit = left;
    linkNode* lessNode = left;
    linkNode* greaterNode = left;
    while(greaterNode != right){
        if( greaterNode->val < povit->val ){
            lessNode = lessNode->next;
            swap_val(lessNode, greaterNode);
        }
        greaterNode = greaterNode->next;
    }
    swap_val(lessNode, povit);
    return povit;
}

static void quickSort_link_(linkNode* left, linkNode* right){
    if(left == right)
        return;
    linkNode* povit = partition_val(left, right);
    quickSort_link_(left, povit);
    quickSort_link_(povit->next, right);
}

void quickSort_link(linkNode* head){
    quickSort_link_(head->next, nullptr);
}
