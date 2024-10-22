class Solution(object):
    def romanToInt(self, s):
        result = 0
        preVal = 0

        symList = [
            ['M', 1000],
            ['D', 500],
            ['C', 100],
            ['L', 50],
            ['X', 10],
            ['V', 5],
            ['I', 1]
        ]

        for char in s:
            for sym, val in symList:
                if char == sym:
                    if val > preVal and preVal > 0:
                        result -= preVal*2
                    result += val
                    preVal = val
                    break

        return result


solution = Solution()
print(solution.romanToInt('MCMXCIV'))
