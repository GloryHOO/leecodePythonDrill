#ZigZag Conversion
class Solution:
    def convert(self, s, numRows):
        slen = len(s)
        if slen <= 1 or numRows == 1:
            return s
        zigZsgStr = [""]
        step = (numRows-1)<<1
        for i in range(numRows):
            left = i
            right = step - i
            if(left == right):
                right += step
            while(left < slen):
                zigZsgStr.append(s[left])
                if(right < slen):
                    zigZsgStr.append(s[right])
                else:
                    break
                left = left + step
                if(left == right):
                    left = left + step
                    right = left + step
                else:
                    right = right + step
        return "".join(zigZsgStr)

obj = Solution()
print(obj.convert("PAYPALISHIRING",3))