#include<iostream>

#ifndef _DYNAMIC_LINK_
#define _DYNAMIC_LINK_
class dynamicLink
{
public:
    typedef struct Node_{
        int val;
        struct Node_* next;
    } Node;
    
    dynamicLink(const std::initializer_list<int> args){
        Node* tail = &head;
        for(const int a : args){
            Node* temp = new Node{a, nullptr};
            tail->next = temp;
            tail = temp;
        }
    }
    
    Node* getHead(){
        return &head;
    }
    
    void insertAtHead(int value){
        Node* temp = new Node{value, nullptr};
        temp->next = head.next;
        head.next = temp;
        //if(tail == nullptr){
        //    tail = temp;
        //}
    }
    
    //void insertAtTail(int value){
    //    Node* temp = new Node{value, nullptr};
    //    if(head.next == nullptr){
    //        head.next = temp;
    //        tail = temp;
    //        return;
    //    }
    //    tail->next = temp;
    //    tail = temp;
    //}
    
    void printLink(){
        for(Node* i=head.next; i!=nullptr; i=i->next){
            std::cout<< i->val << "  ";
        }
        std::cout<< std::endl;
    }
    
    bool equals(dynamicLink& target){
        Node* targetHead = target.getHead();
        Node* self = head.next;
        Node* other = targetHead->next;
        while(self!=nullptr && other!=nullptr){
            if(self->val != other->val){
                return false;
            }
            self = self->next;
            other = other->next;
        }
        if(self!=nullptr || other!=nullptr){
            return false;
        }
        return true;
    }
private:
    Node head = {0, nullptr};
    //Node* tail = nullptr;
};

#endif