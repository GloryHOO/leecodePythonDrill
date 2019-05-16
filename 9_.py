class Solution:
    #9. Palindrome Number
    def isPalindrome(self, x: int) -> bool:
        if (x < 0):
            return False
        if (x < 10):
            return True
        if (x%10 == 0):
            return False
        half = 0
        while(x > half and x > 9):
            half = half*10 + x%10 
            x = x//10
        if(half == x or half//10 == x):
            return True
        return False
    
    #Regular Expression Matching
    def isMatch(self, s: str, p: str) -> bool:
        results = {}
        def dp(i,j):
            if (i,j) not in results:
                if j == len(p):
                    result = i == len(s)
                else:
                    firstMatch = i < len(s) and p[j] in {s[i],'.'}
                    if(j+1 < len(p) and p[j+1]=='*'):
                        result = dp(i,j+2) or (firstMatch and dp(i+1,j))
                    else:
                        result = firstMatch and dp(i+1,j+1)
                results[i,j] = result
            return results[i,j]
        return dp(0,0)

        
            



obj = Solution()
print(obj.isMatch("mississippi","mis*is*p*."))      