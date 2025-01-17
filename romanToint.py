class Solution():
    def romanToInt(self, s):

        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and roman[s[i]] < roman[s[i + 1]]:
                num -= roman[s[i]]
            else:
                # print(i)
                num += roman[s[i]]
        return num


ob1 = Solution()
print(ob1.romanToInt("III"))
print(ob1.romanToInt("CDXLIII"))
