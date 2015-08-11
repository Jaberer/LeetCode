class Solution:
    # @param {string} s
    # @param {string} t
    # sorts s and t then compares the two
    # @return {boolean}
    def isAnagram(self, s, t):
        s = ''.join(sorted(s))
        t = ''.join(sorted(t))
        return (t == s)

# main.py

s = Solution()
s.isAnagram("123", "32a1")