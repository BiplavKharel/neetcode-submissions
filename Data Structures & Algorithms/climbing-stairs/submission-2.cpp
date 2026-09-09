class Solution {
public:
    int climbStairs(int n) {
        int ways = 0;
        if(n == 1){
            return 1;
        }
        if(n == 2){
            return 2;
        }
        ways = climbStairs(n-2) + climbStairs(n-1);


    }
};
