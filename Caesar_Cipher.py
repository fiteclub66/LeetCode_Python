# You are given a list of string, group them if they are same after using Caeser Cipher Encryption.
# Definition of "same", "abc" can right shift 1, get "bcd", here you can shift as many time as you want,
# the string will be considered as same.

from collections import defaultdict

alphabet = 'abcdefghijklmnopqrstuvwxyz'

class CaesarCipher(object):

    def group_caesar(self, los):
        storage = defaultdict(list)

        for i, string in enumerate(los):
            position = [alphabet.index(c) for c in string]
            minPosition = min(position)
            position = [num - minPosition for num in position]
            storage[tuple(position)].append(string)

        return storage.values()

def main():
    caesarCipher = CaesarCipher()
    args = ["abc", "bcd", "acd", "dfg", "ace", "bdf", "random"]
    print(caesarCipher.group_caesar(args))


if __name__ == "__main__":
    main()