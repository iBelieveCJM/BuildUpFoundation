#include<string>
#include<stack>
#include "../basicStruct/biTree.hpp"
typedef biTree::biTreeNode TreeNode;

static void _midOrder_recursive(TreeNode* root, std::string& ret);
std::string midOrder_recursive(TreeNode* root){
    std::string ret;
    if(root==nullptr){
        return ret;
    }
    _midOrder_recursive(root, ret);
    return ret;
}

static void _midOrder_recursive(TreeNode* root, std::string& ret){
    if(root->left != nullptr){
        _midOrder_recursive(root->left, ret);
    }
    if(root!=nullptr){
        ret += root->val;
    }
    if(root->right != nullptr){
        _midOrder_recursive(root->right, ret);
    }
}

std::string midOrder(TreeNode* root){
    std::string ret;
    std::stack<TreeNode*> st;
    while(root!=nullptr || !st.empty()){
        while(root!=nullptr){
            st.push(root);
            root = root->left;
        }
        if(!st.empty()){
            root = st.top(); st.pop();
            ret += root->val;
            root = root->right;
        }
    }
    return ret;
}