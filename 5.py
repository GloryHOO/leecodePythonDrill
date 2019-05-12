# Longest Palindromic Substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        i = 0
        head = 0
        tail = 0
        while i < length and length - i > (tail-head)//2:
            len1 = self.findLongestByCenter(s,i,i)
            len2 = self.findLongestByCenter(s,i,i+1)
            longest = len1 if len1 > len2 else len2
            if longest > tail - head:
                head = i - (longest-1)//2
                tail = i + longest//2
            i +=1
        return s[head:tail+1]

    def findLongestByCenter(self,s,h:int,t:int):
        length = len(s)
        while h>=0 and t<length and s[h] == s[t]:
            h -= 1
            t += 1
        return t - h - 1

s = Solution()
print(s.longestPalindrome('ababababa'))



