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
    
    #10.Regular Expression Matching
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

    def maxArea(self, height: List[int]) -> int: 
        l = 0
        r = len(height) - 1
        maxArea = 0
        while l < r:
            maxArea = max(maxArea,(r-l) * min(height[l],height[r]))
            if height[l] > height[r]:
                 r-=1 
            else: 
                l +=1
        return maxArea

    def intToRoman(self, num: int) -> str:
        romanNum = ["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        numeral =  [1,4,5,9,10,40,50,90,100,400,500,900,1000]
        roman = ""
        i = len(numeral) - 1
        while(num > 0):
            if (num >= numeral[i]):
                num -= numeral[i]
                roman += romanNum[i]
            else:
                i -= 1
        return roman

    def romanToInt(self, s: str) -> int:
        romanMap = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100, 'CD':400, 'D':500,'CM':900, 'M':1000}
        pre = 0
        num = 0
        for ch in s :
            i = romanMap[ch]
            if(i>pre):
                num = num+i-(pre<<1)
            else:
                num += i
            pre = i
        return num

    #3Sum
    #n2  排序，遍历 + 双指针
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        i = 0
        while(i<len(nums)-2):
            if(i>0 and nums[i]==nums[i-1]):
                i+=1
                continue
            l ,r = i + 1 ,len(nums)-1
            while(l < r):
                threeSum = nums[i] + nums[l] + nums[r]
                if(threeSum > 0):
                    r-=1
                elif(threeSum < 0):
                    l+=1
                else:
                    result.append([nums[i], nums[l] ,nums[r]])
                    while(l < r and nums[l] == nums[l+1]):
                        l+=1
                    while(l < r and nums[r] == nums[r-1]):
                        r-=1
                    
            i+=1
        return result






obj = Solution()
print(obj.intToRoman(1992))      