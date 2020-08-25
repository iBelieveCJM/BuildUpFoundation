#include<string>
#include<stack>
#include<algorithm>
#include "../basicStruct/biTree.hpp"
typedef biTree::biTreeNode TreeNode;

static void _postOrder_recursive(TreeNode* root, std::string& ret);
std::string postOrder_recursive(TreeNode* root){
    std::string ret;
    if(root==nullptr){
        return ret;
    }
    _postOrder_recursive(root, ret);
    return ret;
}

static void _postOrder_recursive(TreeNode* root, std::string& ret){
    if(root!=nullptr){
        if(root->left != nullptr){
            _postOrder_recursive(root->left, ret);
        }
        if(root->right != nullptr){
            _postOrder_recursive(root->right, ret);
        }
        ret += root->val;
    }
}

std::string postOrder(TreeNode* root){
    std::string ret;
    std::stack<TreeNode*> st;
    // 1. conduct the preorder visit in root->right->left order
    st.push(root);
    while(!st.empty()){
        root = st.top(); st.pop();
        if(root!=nullptr){
            ret += root->val;
            st.push(root->left);
            st.push(root->right);
        }
    }
    // 1. reverse (root->right->left) order to (left->right->root)
    std::reverse(ret.begin(), ret.end());
    return ret;
}

std::string postOrder2(TreeNode* root){
    std::string ret;
    if(root==nullptr){
        return ret;
    }
    std::stack<TreeNode*> st;
    st.push(root);
    TreeNode* last = root; // keep the last visited node
    while(!st.empty()){
        root = st.top();
        if((root->left==nullptr && root->right==nullptr)\
           ||(root->right==nullptr && last==root->left)\
           ||(last==root->right))
        {
            ret += root->val;
            last = root;
            st.pop();
        }
        else{
            if(root->right!=nullptr){
                st.push(root->right);
            }
            if(root->left!=nullptr){
                st.push(root->left);
            }
        }
    }
    return ret;
}

std::string postOrder3(TreeNode* root){
    std::string ret;
    if(root==nullptr){
        return ret;
    }
    std::stack<TreeNode*> st;
    st.push(root);
    while(!st.empty()){
        root = st.top();
        if(root->left==nullptr && root->right==nullptr){
            ret += root->val;
            st.pop();
        }
        if(root->right!=nullptr){
            st.push(root->right);
            root->right = nullptr;
        }
        if(root->left!=nullptr){
            st.push(root->left);
            root->left = nullptr;
        }
    }
    return ret;
}