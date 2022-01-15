class Solution(object):
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        unique_letters_counter = len(s)
        unique_letters_per_substring = []

        





def main():
    solution = Solution()
    s = "ABC"
    x = "ABA"
    y = "LEETCODE"
    print(f'Expected output for {s} is 10.  Actual outpus is {solution.uniqueLetterString(s)}')
    print(f'Expected output for {x} is 8.  Actual outpus is {solution.uniqueLetterString(x)}')
    print(f'Expected output for {y} is 3.  Actual outpus is {solution.uniqueLetterString(y)}')

if __name__ == "__main__":
    main()

