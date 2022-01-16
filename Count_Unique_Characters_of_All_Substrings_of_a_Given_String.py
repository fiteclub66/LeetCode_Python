class Solution(object):
    def uniqueLetterString(self, s):
        if s is None:
            raise RuntimeError("Bad input; s cannot be None")
        last_seen = {}
        return_value = 0
        last_step_count = 0
        for i in range(len(s)):
            last_two_seen_indices = last_seen.get(s[i], None)
            if not last_two_seen_indices:
                current_step_count = last_step_count + i + 1
                last_seen[s[i]] = (-1, i)
            else:
                second_last_seen_index, last_seen_index = last_two_seen_indices
                num_of_suffixes_without_curr_char = i - 1 - last_seen_index
                num_of_suffixes_with_just_one_occurrence_of_curr_char = last_seen_index - second_last_seen_index
                current_step_count = last_step_count + 1 + num_of_suffixes_without_curr_char - num_of_suffixes_with_just_one_occurrence_of_curr_char
                last_seen[s[i]] = (last_seen_index, i)

            return_value += current_step_count
            last_step_count = current_step_count

        return return_value


def main():
    solution = Solution()
    s = "ABC"
    x = "ABA"
    y = "LEETCODE"
    print(f'Expected output for {s} is 10.  Actual output is {solution.uniqueLetterString(s)}')
    print(f'Expected output for {x} is 8.  Actual output is {solution.uniqueLetterString(x)}')
    print(f'Expected output for {y} is 92.  Actual output is {solution.uniqueLetterString(y)}')

if __name__ == "__main__":
    main()


# It is trivial to solve this question with brute force;
#
# generate all the substrings
# for each substring count the number of unique characters
# keep accumulating the result in a counter
# The complexity of brute force will be O(n^3); there are n^2 substrings and getting count of each takes O(n) time. The fact that this question is being asked tells us that brute force is not good enough! So, let's try to find a better one
#
# Taking an example; eacdaba
#
# Some substrings are ['eacd', 'eacda', 'eacdab', 'eacdaba']. The brute force solution will be counting the number of unique characters across all the substrings. Do we need to? The substrings illustrated above share common prefix(es). By calculating the count of unique characters for all the substrings we are doing wasterful computations.
#
# i	s[i]	substrings added at this step
# 0	e	['e']
# 1	a	['ea', 'a']
# 2	c	['eac', 'ac', 'c']
# 3	d	['eacd', 'acd', 'cd', 'd']
# 4	a	['eacda', 'acda', 'cda', 'da', 'a']
# 5	b	['eacdab', 'acdab', 'cdab', 'dab', 'ab', 'b']
# 6	a	['eacdaba', 'acdaba', 'cdaba', 'daba', 'aba', 'ba', 'a']
# Observation As we scan the string from left to right, at each step i (0 indexed), there will be i + 1 new substrings ending at s[i]. Out of these
#
# i substrings are formed by appending s[i] to the substrings from the previous step, and
# One single character substring is formed by s[i]
# Few interesting cases arise for the i substrings that are formed by appending s[i] to the substrings from the previous step. We can classify them into the following categories
#
# Do not contain s[i]. For each of them, the count of unique characters will increase by 1. e.g., In step(i=1), substrings ['ea', 'a'] have 2 and 1 unique characters respectively. In step(i=2), the count for strings ['eac', 'ac'] is 3 and 2 ('c' is not present in s[:2]). Let's say there are Q such substrings.
# Contain s[i] exactly once. For them the count of unqiue characters will decrease by 1. e.g., in step(i=3), 'eacd' has 4 unique characters, and in step(i=4), 'eacda' (formed by appending 'a' to 'eacd') has 3 unique characters. Let's say there are R such substrings.
# Contain s[i] more than once. The count of unique characters stays the same for such substrings. e.g., in step(i=5), 'acdab' has 3 unique characters, and in step(i=6), 'acdaba' (formed by appending 'a' to the 'acdab'`) still has 3 unique characters. As the count of unique characters doesn't change for these substrings, we do not need to worry about them.
# So, we arrive at - if the count of unique characters of substrings from the previous steps is P, then the count of unique characters for the current step will be P + Q - R + 1. The trailing 1 is for the single character substring formed by s[i].
#
# Now the problem is reduced to finding
#
# Q; num of suffixes of the slice s[:i] which do not contain s[i], and
# R; num of suffixes of the slice s[:i] which contain s[i] exactly once
# Note that if s[i] is not present in the slice s[:i], then Q=i and R=0.
#
# To find Q and R more generally, let's consider step(i=4) from the above example. ['eacd', 'acd', 'cd', 'd'] are the subtrings from step(i=3). In step(i=4), we will append 'a' to these substrings to get new ones. To find Q we need to find number of substrings from step(i=3) which do not contain 'a'. There are 2 ('cd' and 'd') such substrings. So, Q=2. If we think about it this is nothing but the number of characters between the current character (a at index i=4) and its last occurence (at i=1) in the string.
#
# More generally speaking, if the current character (i.e., s[i]) was last seen at index j in the string, we can represent the string s as
#
# s_0,s_1,s_2,...,s_j,s_j+1,...,s_i-1,s_i,...
# All the suffixes of the slice s[j+1:i] (or the substring s_j+1,...,s_i-1) will not contain s[i]. There will be (i-1) - (j+1) + 1 or i-1-j such suffixes. So, we have
#
# Q = i-1-j, where j is the index of the last occurrence of s[i].
#
# Extending the logic, R, i.e., number of substrings from the previous step which have the current character (s[i]) exactly once is nothing but the number of characters between the last and the second last occurence of s[i] in the string. If k is the index of the second last occurrence of s[i], then we can represent s as
#
# s_0,s_1,s_2,...,s_k,s_k+1,...,s_j,s_j+1,...,s_i-1,s_i,...
# The suffixes of the slice s[k+1:j+1] will contain s[i] exactly once. There are j - (k+1) + 1 or j-k such suffixes. So, we have
#
# R = j-k, where k is the index of the second last occurrence of s[i].
#
# This completes our algorithm - while scanning the string from left to right, at step i (0 <= i < len(s))
#
# Find (k, j) which are the indices of the last two occurences of s[i]
# Count of the current step is P + Q - R + 1, where P is the count from the previous step and Q and R are defined in terms of j and k by the formulas defined above
# Update total count with the count from current step
# Count of the current step becomes P
# Update the last two occurences of s[i] as (j, i).
# Time complexity = O(n) as we do a single scan of s.
# Space complexity = O(1) for we are dealing with constant (26) number of alphabets and for each alphabet we need constant (2) space to keep track of its last two occurrences in s.

