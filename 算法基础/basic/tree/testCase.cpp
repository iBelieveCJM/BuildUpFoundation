#include<iostream>
#include<string>
using namespace std;
#include "../basicStruct/biTree.hpp"
typedef biTree::biTreeNode TreeNode;

typedef string(*treeAlgo)(TreeNode*);

#ifdef PRE_ORDER
#include"preOrder.hpp"
treeAlgo algo_recursive = preOrder_recursive;
treeAlgo algo = preOrder;
#elif MID_ORDER
#include"midOrder.hpp"
treeAlgo algo_recursive = midOrder_recursive;
treeAlgo algo = midOrder;
#elif POST_ORDER
#include"postOrder.hpp"
treeAlgo algo_recursive = postOrder_recursive;
treeAlgo algo = postOrder2;
#endif

void emptyTree(){
    cout<< "-------- emptyTree --------" << endl;
    biTree t;
    cout<< "recuresive: " << algo_recursive(t.getRoot()) << endl;
    cout<< "non-recuresive: " << algo(t.getRoot()) << endl;
    t.print();
}

void oneNodeTree(){
    cout<< "-------- oneNodeTree --------" << endl;
    biTree t("A");
    cout<< "recuresive: " << algo_recursive(t.getRoot()) << endl;
    cout<< "non-recuresive: " << algo(t.getRoot()) << endl;
    t.print();
}

void leftOnlyTree(){
    cout<< "-------- leftOnlyTree --------" << endl;
    biTree t("AB#C#D###");
    cout<< "recuresive: " << algo_recursive(t.getRoot()) << endl;
    cout<< "non-recuresive: " << algo(t.getRoot()) << endl;
    t.print();
}

void rightOnlyTree(){
    cout<< "-------- rightOnlyTree --------" << endl;
    biTree t("A#B#C#D##");
    cout<< "recuresive: " << algo_recursive(t.getRoot()) << endl;
    cout<< "non-recuresive: " << algo(t.getRoot()) << endl;
    t.print();
}

void tree0(){
    cout<< "-------- tree0 --------" << endl;
    biTree t("A#BC###");
    cout<< "recuresive: " << algo_recursive(t.getRoot()) << endl;
    cout<< "non-recuresive: " << algo(t.getRoot()) << endl;
    t.print();
}

void tree1(){
    cout<< "-------- tree1 --------" << endl;
    biTree t("ABCDEFG########");
    cout<< "recuresive: " << algo_recursive(t.getRoot()) << endl;
    cout<< "non-recuresive: " << algo(t.getRoot()) << endl;
    t.print();
}

int main(){
    emptyTree();
    oneNodeTree();
    leftOnlyTree();
    rightOnlyTree();
    tree0();
    tree1();
    return 0;
}