class Solution(object):
    def intToRoman(self, num):
        result = ""

        symList = [
            ['M', 1000],
            ['CM', 900],
            ['D', 500],
            ['CD', 400],
            ['C', 100],
            ['XC', 90],
            ['L', 50],
            ['XL', 40],
            ['X', 10],
            ['IX', 9],
            ['V', 5],
            ['IV', 4],
            ['I', 1]
        ]

        for sym, val in symList:
            if num // val:
                count = num // val
                result += sym * count
                num = num % val
        return result


solution = Solution()
print(solution.intToRoman(3749))
