class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # str_x = str(x)
        # y = ""
        # for i in range(len(str_x)):
        #     y = str_x[i] + y
        # if str_x == y:
        #     return True
        # else:
        #     return False

        # Runtime: 32ms, faster than 99.02% of Python online submissions for Palindrome Number.
        # Memory Usage: 13.3MB, less than 89.53% of Python online submissions for Palindrome Number.
        return str(x) == str(x)[::-1]

def main():
    input = 10
    solution = Solution()
    print(solution.isPalindrome(input))

if __name__ == "__main__":
    main()