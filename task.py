#IMPORT PyTest Library in Python

import pytest

class Solution:
    def longestPalindrome(self, s):
        candidate = ""
        longest = ""
        contains_palindrome = False
        for i, char in enumerate(s):
            if i == 0:
                candidate = char
            elif i == 1:
                if s[1] == s[0]:
                    candidate = self.get_palindrome(s, start=0, end=1)
            elif i >= 2:
                if char == s[i-1]:
                    candidate = self.get_palindrome(s, start=i-1, end=i)
                elif char == s[i-2]:
                    candidate = self.get_palindrome(s, start=i-2, end=i)
            if len(candidate) > len(longest):
                longest = candidate
        return longest

    @staticmethod
    def get_palindrome(s, start, end):
        palindrome = s[start:end+1]
        while end < len(s) - 1:
            if s[end+1] == s[start] and Solution.all_same(palindrome):
                end += 1
                palindrome += s[end]
            else:
                break
        while (start > 0) and (end < len(s) - 1):
            start -= 1
            end += 1
            if s[start] == s[end]:
                palindrome = s[start] + palindrome + s[end]
            else:
                break
        return palindrome

    @staticmethod
    def all_same(items):
        return all(item == items[0] for item in items)

#test the code :

def test_1():
    assert Solution().longestPalindrome("babad") == "bab"

def test_2():
    assert Solution().longestPalindrome("cbbd") == "bb"

def test_3():
    assert Solution().longestPalindrome("a") == "a"

def test_4():
    assert Solution().longestPalindrome("ac") == "a"

if __name__ == "__main__":
    pytest.main([__file__])
