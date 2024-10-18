class Solution(object):
    def isMatch(self, s, p):
        if "*" in p:

            for x in range(len(p)):
                if p[x] == "*":
                    return x



            if "." in p:
                return True
            for char in s:
                if char != p[0]:
                    return False
            return True

        if len(s) > len(p):
            return False

        for char in s:
            if char != p[0]:
                return False
        return True

solution = Solution()

print(solution.isMatch("aab","c*a*b"))
