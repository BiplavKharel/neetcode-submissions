class Solution {
public:
    int rob(vector<int>& nums) {
        
        vector<int> memo(nums.size());
        memo[0] = nums[0];
        memo[1] = max(nums[0],nums[1]);
        for(int i = 2;i<memo.size();i++){

            memo[i] = max(nums[i]+memo[i-2],memo[i-1]);
        }

        return memo[nums.size()-1];
    }
};


/*

goal: rob the most amount of money
constraint: cant go i-1,i+1, so if Im at i, i need to decided if robbing the one before or robbing the now would be better
reccurance:
memo[i] = max(memo[i],nums[i] + memo[i-2])


*/