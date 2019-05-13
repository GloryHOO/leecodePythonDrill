#atoi
class Solution:
    def myAtoi(self, str: str) -> int:
        if not str:
            return 0
        char0 = 48
        char9 = 57
        intValue = 0
        mark = 1
        i = 0
        for i in range(len(str)):
            cNum = ord(str[i])
            if str[i] == ' ':
                continue
            elif str[i] == '-' and intValue == 0:
                mark = -1
                break
            elif str[i] == '+' and intValue == 0:
                break
            elif cNum >= char0 and cNum <= char9:
                intValue = cNum - char0
                break
            else:
                return 0
        i += 1
        for i in range(i,len(str)):
            cNum = ord(str[i])
            if cNum >= char0 and cNum <= char9:
                cV = cNum - char0
                if intValue > 214748364:
                    if mark == -1:
                        return -2147483648
                    else:
                        return 2147483647
                elif intValue == 214748364:
                    if mark == -1 and cV >8:
                        return -2147483648
                    elif mark == 1 and cV >7:
                        return 2147483647
                intValue = intValue*10 + cV
            else:
                break
        return intValue * mark

obj = Solution()
print(obj.myAtoi(" -42"))