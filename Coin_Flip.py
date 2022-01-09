# Consider there is a set of coins placed on a board.  Some coins are placed in a way that the Head will be at the
# top and some coins are placed in an opposite way (TAIL side at the top).  HEAD facing coins can be considered as
# string "H" and TAIL facing coins can be considered as string "T".
# Example: HTHTTT
# If the coins are arranged in such a manner that all the HEAD facing coins comes first followed by the TAIL
# facing coins, then the set is called a Beautiful set.
# Beautiful set: HHHTT
# You need to write a function that takes a string as input and return the minimum number of flips need to make the
# coins as a beautiful set.
# Example:
# Input: "HTHTT"
# Output: 1

class BeautifulCoinFlips(object):
    def coin_flips(self, coin_string):
        num_flips = 0
        # get position of last H in string
        last_head_position = None
        for i, j in enumerate(coin_string):
            if j == "H":
                last_head_position = i

        # count number of T prior to that position for result
        i = 0
        while i <= last_head_position:
            if coin_string[i] == "T":
                num_flips += 1
            i += 1

        return num_flips

def main():
    bcf = BeautifulCoinFlips()
    coin_string = "THHTTTH"
    print(f'number of flips for set {coin_string} is {bcf.coin_flips(coin_string)}')


if __name__ == "__main__":
    main()