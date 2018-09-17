#include<iostream>
#include"../basicStruct/dynamicLink.hpp"

typedef dynamicLink::Node linkNode;

void simpleSelectSort_link(linkNode* head){
    if(head==nullptr || head->next==nullptr){
        return ;
    }
    linkNode* st = head;
    while(st->next != nullptr){
        linkNode* pre_max = st;
        linkNode* max = st->next;
        linkNode* pre_cur = st;
        linkNode* cur = st->next;
        while(cur != nullptr){
            if(cur->val > max->val){
                max = cur;
                pre_max = pre_cur;
            }
            pre_cur = pre_cur->next;
            cur = pre_cur->next;
        }
        // insert at head
        pre_max->next = max->next;
        max->next = head->next;
        head->next = max;
        // the start item is always the max item in the whole link
        // we just need to sort the items after the max item
        if(st == head){
            st = max;
        }
    }
}


