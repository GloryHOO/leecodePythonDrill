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

obj = Solution()
print(obj.isPalindrome(21120))      