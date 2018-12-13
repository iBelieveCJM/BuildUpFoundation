#include<iostream>
#include<string>
#include<queue>

#ifndef _BI_TREE_
#define _BI_TREE_

class biTree
{
public:
    struct biTreeNode{
        char val;
        biTreeNode *left;
        biTreeNode *right;
        
        biTreeNode(int x): val(x), left(nullptr), right(nullptr){}
    };
    
private:
    biTreeNode* root;
    
public:
    biTree():root(nullptr){}
    biTree(std::string order):root(nullptr){
        orderInitial(order);
    }
    ~biTree(){
        destroyTree(root);
        root = nullptr;
    }
  
public:
    void orderInitial(std::string order);
    void print();
    biTreeNode* getRoot(){return root;}
    
private:
    void destroyTree(biTreeNode* r){
        if(r != nullptr){
            destroyTree(r->left);
            destroyTree(r->right);
            delete r;
        }
    }
};

void
biTree::orderInitial(std::string order){
    if(root!=nullptr){
        destroyTree(root);
    }
    root = nullptr;
    if(order.empty()){
        return;
    }
    std::queue<biTreeNode*> q;
    root = new biTreeNode(order[0]);
    q.push(root);
    int i=1; 
    while(i < order.size()){
        if(!q.empty()){
            biTreeNode* tmp = q.front();
            q.pop();
            //std::cout<< tmp->val << std::endl;
            if(order[i]!='#'){
                tmp->left = new biTreeNode(order[i]);
                //std::cout<< "left: " << order[i] << "i: " << i << std::endl;
                q.push(tmp->left);
            }
            ++i;
            if(order[i]!='#'){
                tmp->right = new biTreeNode(order[i]);
                //std::cout<< "right: " << order[i] << "i: " << i  << std::endl;
                q.push(tmp->right);
            }
            ++i;
        }
    }
}

void
biTree::print(){
    if(root==nullptr){
        std::cout<< "This is a empty tree." << std::endl;
        return;
    }
    std::queue<biTreeNode*> q;
    q.push(root);
    while(!q.empty()){
        biTreeNode* tmp = q.front();
        q.pop();
        if(tmp == nullptr){
            std::cout<< "#";
        }
        else{
            std::cout<< tmp->val;
            q.push(tmp->left);
            q.push(tmp->right);
        }
        std::cout<< " ";
    }
    std::cout<< std::endl;
}
#endif