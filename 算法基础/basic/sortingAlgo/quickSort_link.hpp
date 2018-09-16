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
void swap_node(linkNode* pre_a, linkNode* a, linkNode* pre_b, linkNode* b){
    if(a == b){
        return;
    }
    if(pre_b == a){
        linkNode* after_b = b->next;
        b->next = a;
        a->next = after_b;
        pre_a->next = b;
        return;
    }
    linkNode* after_b = b->next;
    b->next = a->next;
    a->next = after_b;
    pre_a->next = b;
    pre_b->next = a;
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

///////////////////
// the idea is to create two list: 
//    0.list for element which less than povit
//    1.list for element which greater than povit
// then link two list and other part of the whole list.
///////////////////
void insertList(linkNode** list, linkNode** point){
    (*point)->next = (*list)->next;
    (*list)->next = *point;
    *list = *point;
}
linkNode* partition_node(linkNode* pre_left, linkNode* left, linkNode* right){
    linkNode* point = left;
    linkNode* povit = left;
    linkNode povitHead = {0, nullptr};
    linkNode* povitList = &povitHead;
    linkNode lessHead = {0, nullptr};
    linkNode* lessList = &lessHead;
    linkNode greaterHead = {0, nullptr};
    linkNode* greaterList = &greaterHead;
    while(point != right){
        linkNode* aft = point->next;
        
        if( point->val < povit->val ){
            insertList(&lessList, &point);   // if you want to change the pointer, you should use pointer to pointer
        }
        if( point->val > povit->val ){
            insertList(&greaterList, &point);
        }
        if( point->val == povit->val){
            insertList(&povitList, &point);
        }
        
        point = aft;
    }
    greaterList->next = right;
    povitList->next = greaterHead.next;
    lessList->next = povitHead.next;
    pre_left->next = lessHead.next;
    return povit;
}

static void quickSort_link_val_(linkNode* left, linkNode* right){
    if(left == right)
        return;
    linkNode* povit = partition_val(left, right);
    std::cout<< "povit: " << povit->val << std::endl;
    quickSort_link_val_(left, povit);
    quickSort_link_val_(povit->next, right);
}

static void quickSort_link_node_(linkNode* pre_left, linkNode* left, linkNode* right){
    if(left == right)
        return;
    linkNode* povit = partition_node(pre_left, left, right);
    std::cout<< "left: " << pre_left->next->val << " povit: " << povit->val << std::endl;
    quickSort_link_node_(pre_left, pre_left->next, povit);
    quickSort_link_node_(povit, povit->next, right);
}

void quickSort_link(linkNode* head){
    if(head==nullptr || head->next==nullptr){
        return;
    }
    //quickSort_link_val_(head->next, nullptr);
    quickSort_link_node_(head, head->next, nullptr);
}
