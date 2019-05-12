#Reverse Integer
class Solution:
    def reverse(self, x):
        reverseX = 0
        flag = 1
        if x < 0:
            flag = -1
            x = abs(x)
        while x > 0:
            if(reverseX > 214748364):
                return 0
            remainder= x%10
            if reverseX == 214748364:
                if (flag == 1 and remainder > 7):
                    return 0
                if (flag == -1 and remainder > 8):
                    return 0
            reverseX = reverseX * 10  + remainder
            x = x//10
        if (reverseX > 2147483648):
            return 0
        if (flag == 1 and reverseX > 2147483647):
            return 0
        return reverseX * flag

obj = Solution()
print(obj.reverse(-123))