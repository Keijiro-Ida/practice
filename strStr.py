class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_len = len(needle)

        haystack_len = len(haystack)

        if needle_len > haystack_len:
            return 0

        for i in range(haystack_len - needle_len + 1):
            if(haystack[i:i+needle_len] == needle):
                return i

        return -1
