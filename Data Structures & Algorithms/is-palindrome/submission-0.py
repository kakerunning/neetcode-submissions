class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for i in range(len(s)):
            if('a' <= s[i] <='z' or 'A' <= s[i] <='Z' or '0' <= s[i] <='9'):
                s_new += s[i].lower()

        return s_new == s_new[::-1]