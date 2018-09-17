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
    linkNode* pivot = left;
    linkNode* lessNode = left;
    linkNode* greaterNode = left;
    while(greaterNode != right){
        if( greaterNode->val < pivot->val ){
            lessNode = lessNode->next;
            swap_val(lessNode, greaterNode);
        }
        greaterNode = greaterNode->next;
    }
    swap_val(lessNode, pivot);
    return pivot;
}

///////////////////
// the idea is to create two list: 
//    0.list for element which less than pivot
//    1.list for element which greater than pivot
// then link two list and other part of the whole list.
///////////////////
linkNode* partition_node(linkNode* pre_left, linkNode* left, linkNode* right){
    int pivot = left->val;
    linkNode lessHead(0);
    linkNode* lessList = &lessHead;
    linkNode greaterHead(0);
    linkNode* greaterList = &greaterHead;
    for(linkNode* i=left->next; i!=right; i=i->next){ //note. i must start from left->next, skip the pivot
        if( i->val < pivot ){
            lessList->next = i;
            lessList = i;
        }
        else{
            greaterList->next = i;
            greaterList = i;
        }
    }
    greaterList->next = right;
    left->next = greaterHead.next;
    lessList->next = left;
    pre_left->next = lessHead.next;
    return left;
}

static void quickSort_link_val_(linkNode* left, linkNode* right){
    if(left == right)
        return;
    linkNode* pivot = partition_val(left, right);
    std::cout<< "pivot: " << pivot->val << std::endl;
    quickSort_link_val_(left, pivot);
    quickSort_link_val_(pivot->next, right);
}

static void quickSort_link_node_(linkNode* pre_left, linkNode* left, linkNode* right){
    if(left == right)
        return;
    linkNode* pivot = partition_node(pre_left, left, right);
    std::cout<< "left: " << pre_left->next->val << " pivot: " << pivot->val << std::endl;
    quickSort_link_node_(pre_left, pre_left->next, pivot); //note. the second arg must use pre_left->next for left==pivot
    quickSort_link_node_(pivot, pivot->next, right);
}

void quickSort_link(linkNode* head){
    if(head==nullptr || head->next==nullptr){
        return;
    }
    //quickSort_link_val_(head->next, nullptr);
    quickSort_link_node_(head, head->next, nullptr);
}
