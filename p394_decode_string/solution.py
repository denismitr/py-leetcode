from dataclasses import dataclass
import unittest

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop() # remove the [

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * substr)

        return "".join(stack)



class TestSolution(unittest.TestCase):
    def test_decode_string(self):
        @dataclass
        class TestCase:
            input: str
            expected: str

        testcases = [
            TestCase(input="3[a]2[bc]", expected="aaabcbc"),
            TestCase(input="3[a2[c]]", expected="accaccacc"),
            TestCase(input="2[abc]3[cd]ef", expected="abcabccdcdcdef"),
        ]

        sl = Solution()
        for testcase in testcases:
            want, got = testcase.expected, sl.decodeString(testcase.input)
            self.assertEqual(want, got, "want {}, got {}".format(want, got))

if __name__ == "__main__":
    unittest.main()
