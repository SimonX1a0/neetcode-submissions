class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        smp = {}
        tmp = {}

        for i in range(len(s)):
            smp[s[i]] = smp.get(s[i], 0) + 1
            tmp[t[i]] = tmp.get(t[i], 0) + 1

        for key, val in smp.items():
            if tmp.get(key, 0) != val:
                return False
        return True