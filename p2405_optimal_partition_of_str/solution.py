class Solution:
    def partitionString(self, s: str) -> int:
        curr = set()
        result = 1
        for c in s:
            if c in curr:
                result += 1
                curr = set()
            curr.add(c)
        return result        