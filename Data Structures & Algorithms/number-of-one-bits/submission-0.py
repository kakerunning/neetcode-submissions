class Solution:
    def hammingWeight(self, n: int) -> int:
        num_str = bin(n)[2:]
        ans = 0

        for i in num_str:
            ans += int(i)
        
        return ans