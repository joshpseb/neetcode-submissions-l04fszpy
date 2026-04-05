class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for string in strs:
             s += string + "`"
        print("s", s)
        return s


    def decode(self, s: str) -> List[str]:
        strs = []
        string = ""
        for c in s:
            if c != "`":
                string += c
            else:
                strs.append(string)
                string = ""
        return strs
