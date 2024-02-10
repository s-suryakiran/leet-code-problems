/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        map<Node*, Node*> m;
        Node* t = head;
        if(head == NULL){
            return NULL;
        }
        while(t!=NULL){
            m[t] = new Node(t->val);
            t= t->next;
        }
        for(auto e:m){
            if(e.first->next)
                e.second->next = m[e.first->next];
            if(e.first->random)
                e.second->random = m[e.first->random];
        }
        Node* nh = m.begin()->second;
        return nh;
    }
};