"""
File: anagram.py
Name: Adam
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm

# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    to find the anagrams
    """
    print('Welcome to stanCode \"Aangram Generator \" (or -1 to quit)')
    while True:
        data = input('Find anagrams for: ')
        start = time.time()
        if data == EXIT:
            break
        else:
            find_anagrams(data)
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end - start} seconds.')


def read_dictionary():
    with open(FILE, 'r') as f:
        lst = []
        for line in f:
            tokens = line[:-1]
            lst.append(tokens)
        return lst
        # print(lst)


def find_anagrams(s):
    """
    :param s:str
    :return: anagrams
    """
    lst = read_dictionary()
    n = [0]   # number of anagrams
    anagrams = []
    index = []
    print('Searching...')
    find_anagrams_helper(s, '', len(s), lst, n, anagrams, index)
    print(str(n[0])+' anagrams: ' + str(anagrams))


def find_anagrams_helper(s, current_s, ans_len, lst, n, anagrams, index):
    if len(current_s) == ans_len:
        if current_s in lst and current_s not in anagrams:
            anagrams.append(current_s)
            n[0] += 1
            print('Found: '+current_s)
            print('Searching...')
    else:
        for i in range(len(s)):
            if i not in index:
                index.append(i)
                # Choose
                current_s += s[i]
                if has_prefix(current_s, lst):
                    # explore
                    find_anagrams_helper(s, current_s, ans_len, lst, n, anagrams, index)
                # Un-choose
                current_s = current_s[:-1]  # 字串不能用pop list才可以
                index.pop()


def has_prefix(sub_s, dictionary):
    """
    :param sub_s: str
    :param dictionary: list, dictionary
    :return: boolean
    """
    # lst = read_dictionary()
    for word in dictionary:
        if word.startswith(sub_s):
            return True
    return False


if __name__ == '__main__':
    main()
