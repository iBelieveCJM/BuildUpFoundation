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

void bubbleSort_link(linkNode* head){
    if(head==nullptr || head->next==nullptr){
        return;
    }
    linkNode* end = nullptr;
    linkNode* cur = nullptr;
    bool isChange = true;
    while(end != head->next && isChange){
        isChange = false;
        cur = head->next;
        for(; cur->next!=end; cur=cur->next){
            if(cur->val > cur->next->val){
                swap_val(cur, cur->next);
                isChange = true;
            }
        }
        end = cur;  //note. nice trick, record the next end;
    }
}


