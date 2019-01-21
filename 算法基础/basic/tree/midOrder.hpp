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
    if(root!=nullptr){
        if(root->left != nullptr){
            _midOrder_recursive(root->left, ret);
        }
        ret += root->val;
        if(root->right != nullptr){
            _midOrder_recursive(root->right, ret);
        }
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

/*
 * Morris middle order travel using Threaded BinaryTree which
 * treats the empty right pointer as a cue to find the next in mid order.
*/
std::string midOrderMorris(TreeNode *root){
    std::string ret;
    while(root != nullptr){
        // if it is leftest node, then visit it
        if(root->left == nullptr){
            ret += root->val;    // visit it
            root = root->right;  // ture to its right node or next node.
        }
        else{
            // find front node of the current node
            // front node is left child or the rightest node of left subtree
            TreeNode *pre = root->left;    // root->left is not nullptr
            while(pre->right!=nullptr && pre->right!=root){ //Note: pre->right!=root
                pre = pre->right;
            }
            // if it is first time to visit this node
            // the make the cue
            if(pre->right == nullptr){
                pre->right = root;
                root = root->left;
            }
            // if this node had been maked the cue
            else{
                pre->right = nullptr; // delete the cue
                ret += root->val;     // visit it
                root = root->right;   // ture to its right or next node.
            }
        }
    }
    return ret;
}