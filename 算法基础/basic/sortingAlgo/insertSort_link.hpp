#include<iostream>
#include"../basicStruct/dynamicLink.hpp"

typedef dynamicLink::Node linkNode;

void insertSort_link(linkNode* head){
    if(head==nullptr || head->next==nullptr){
        return ;
    }
    linkNode* cur = head->next->next;
    linkNode* pre_cur = head->next;
    while(cur != nullptr){
        linkNode* cmp = head->next;
        linkNode* pre_cmp = head;
        while(cmp->val < cur->val && cmp!=cur){
            pre_cmp = pre_cmp->next;
            cmp = pre_cmp->next;
        }
        if(cmp != cur){
            pre_cur->next = cur->next;
            cur->next = cmp;
            pre_cmp->next = cur;
        }
        else{
            pre_cur = pre_cur->next;
        }
        cur = pre_cur->next;
    }
}


