#include<string>
#include<stack>
#include "../basicStruct/biTree.hpp"
typedef biTree::biTreeNode TreeNode;

static void _preOrder_recursive(TreeNode* root, std::string& ret);
std::string preOrder_recursive(TreeNode* root){
    std::string ret;
    if(root==nullptr){
        return ret;
    }
    _preOrder_recursive(root, ret);
    return ret;
}

static void _preOrder_recursive(TreeNode* root, std::string& ret){
    if(root!=nullptr){
        ret += root->val;
        if(root->left != nullptr){
            _preOrder_recursive(root->left, ret);
        }
        if(root->right != nullptr){
            _preOrder_recursive(root->right, ret);
        }
    }    
}

std::string preOrder2(TreeNode* root){
    std::string ret;
    std::stack<TreeNode*> st;
    st.push(root);
    while(!st.empty()){
        root = st.top(); st.pop();
        while(root!=nullptr){
            ret += root->val;
            if(root->right!=nullptr){
                st.push(root->right);
            }
            root = root->left;
        }
    }
    return ret;
}

std::string preOrder(TreeNode* root){
    std::string ret;
    std::stack<TreeNode*> st;
    st.push(root);
    while(!st.empty()){
        root = st.top(); st.pop();
        if(root!=nullptr){
            ret += root->val;
            st.push(root->right);
            st.push(root->left);
        }
    }
    return ret;
}