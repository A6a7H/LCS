struct TreeNode {
	int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

class Solution {
    TreeNode* sortedArrayToBST(vector<int>& nums, int l, int r){
        if(r <= l) return NULL; 
        int midIdx = (l + r)/2;
        TreeNode* root = new TreeNode(nums[midIdx]);
        root->left = sortedArrayToBST(nums, l, midIdx);
        root->right = sortedArrayToBST(nums, midIdx+1, r);
        return root;
    }
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        return sortedArrayToBST(nums, 0, nums.size());
    }
};