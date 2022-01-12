# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
# https://leetcode.com/problems/zigzag-conversion/

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        solution = {}
        line = 1
        step = 1
        if numRows < 2:
            return s
        for letter in s:
            if line not in solution:
                solution[line] = letter
            else:
                solution[line] += letter

            line += step

            if line == numRows or line == 1:
                step *= -1

        final_string = ''.join(solution.values())
        return(final_string)

def main():
    solution = Solution()
    input = "PAYPALISHIRING"
    print(solution.convert(input, 3))

if __name__ == "__main__":
    main()