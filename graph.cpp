#include<iostream>
#include<vector>
using namespace std;
class Node;

class Graph{
    public:
    vector<Node> nodes;

};

class Node{
    public:
    int data;
    vector<Node*> children;
    Node(){}
    Node(int i){data = i;}
    void addchild(Node* child){
        children.push_back(child);
    }
};

int main(){
    int n,a,b;
    Graph graph = Graph();
    cin>>n;
    vector<Node> &nodes = graph.nodes;
    nodes.resize(n);
    for(int i=0;i<n;i++)nodes[i] = Node(i);
    for(int i=0;i<n;i++){
        cin>>a>>b;
        nodes[a].addchild(&nodes[b]);
    }
    for(int i=0;i<nodes.size();i++){
        cout<<nodes[i].data;
        for(int j=0;j<nodes[i].children.size();j++){
            cout<<"->"<<nodes[i].children[j]->data<<endl;
        }
    }
}