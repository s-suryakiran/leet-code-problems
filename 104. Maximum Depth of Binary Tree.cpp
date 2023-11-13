/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int m = -1;
    int maxDepth(TreeNode* root) {
        if (root == NULL){
            return 0;
        }
        int rightDepth = maxDepth(root->right);
        int leftDepth = maxDepth(root->left);
        this->m = max(rightDepth, leftDepth) + 1;
        return this->m;
    }
};