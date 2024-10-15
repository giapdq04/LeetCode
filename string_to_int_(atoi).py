class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        createdNumber = ""
        try:
            createdNumber = int(s)
        except ValueError:
            for char in s:
                if char.isdigit():
                    createdNumber += char
                elif char in ['-', '+'] and not createdNumber:
                    createdNumber += char
                elif createdNumber:
                    break
                else:
                    return 0
            if createdNumber in ['','+','-']:
                return 0

        int_min = -2**31  # -2147483648
        int_max = 2**31 - 1  # 2147483647

        createdNumber = int(createdNumber)

        if createdNumber < int_min:
            return int_min
        elif createdNumber > int_max:
            return int_max

        return createdNumber


solution = Solution()

print(solution.myAtoi("  +  413"))
