#include<iostream>
#include"../basicStruct/dynamicLink.hpp"

typedef dynamicLink::Node linkNode;

void printList(linkNode* first){
    std::cout<< "----------------------------" << std::endl;
    while(first != nullptr){
        std::cout<< " " << first->val;
        first = first->next;
    }
    std::cout<< std::endl;
}
linkNode* merge(linkNode* first, linkNode* second){
    if(first == nullptr){
        return second;
    }
    if(second == nullptr){
        return first;
    }
    linkNode ret(0);
    linkNode* ret_p = &ret;
    while(first != nullptr && second != nullptr){
        if(first->val <= second->val){
            ret_p->next = first;
            first = first->next;
        }
        else{
            ret_p->next = second;
            second = second->next;
        }
        ret_p = ret_p->next;
    }
    if(first != nullptr){
        ret_p->next = first;
    }
    if(second != nullptr){
        ret_p->next = second;
    }
    return ret.next;
}

void testMerge(){
    std::cout<< "test merge function" << std::endl;
    dynamicLink first = {0,1,2,3,4};
    first.printLink();
    dynamicLink second = {0,1,2,3,4};
    second.printLink();
    linkNode* ret = merge(first.getHead()->next, second.getHead()->next);
    printList(ret);
}

static linkNode* mergeSort_(linkNode* first){
    if(first==nullptr || first->next==nullptr){//note. if first is nullptr(exception) or first has noly one element
        return first;
    }
    linkNode* fast = first;
    linkNode* slow = first;
    while(fast->next!=nullptr && fast->next->next!=nullptr){ //note. this condition should be rethink carefully
        fast = fast->next->next;
        slow = slow->next;
    }
    linkNode* second = slow->next;
    slow->next = nullptr;  // process the end of first link list
    //printList(first);
    //printList(second);
    first = mergeSort_(first);
    second = mergeSort_(second);
    //printList(first);
    //printList(second);
    return merge(first, second);
}

void mergeSort_link(linkNode* head){
    if(head==nullptr || head->next==nullptr){
        return ;
    }
    head->next = mergeSort_(head->next);
}
