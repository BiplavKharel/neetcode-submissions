class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
    int n = cost.size();
    vector<int> minCosts(n+1);


    for(int i = 2; i <= n;i++){

        minCosts[i] = min(cost[i-1] + minCosts[i-1],
                        cost[i-2] + minCosts[i-2]);
    }
        return minCosts[n];
        
    }
};
