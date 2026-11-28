class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            res = res + str(len(s)) + '#'
            res = res + s 
        return res

    def decode(self, s: str) -> List[str]:
        if s == '':
            return []
        res = []
        temp = ""
        p = 0
        while p < len(s):
            num = ''
            while s[p] != '#':
                num += s[p]
                p += 1
            num = int(num)
            p += 1
            if num > 0:
                res.append(s[p:p+num])
                p += num
            else:
                res.append('')
        return res
            

