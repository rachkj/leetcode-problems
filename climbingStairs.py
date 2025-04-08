class ClimbingStairs:
    def climbingstairs(self, n:int)->int:
        dp=[0]*(n+1)
        dp[0]=0
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
    
test=ClimbingStairs()
print(test.climbingstairs(3))

# Input: n = 2
# Output: 2