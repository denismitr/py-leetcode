from dataclasses import dataclass
import unittest
import problem

class TestSolution(unittest.TestCase):
    def test_remore_stars(self):
        @dataclass
        class TestCase:
            input: str
            expected: str

        testcases = [
            TestCase(input="leet**co*de*", expected="lecd"),
            TestCase(input="leet**code*", expected="lecod"),
            TestCase(input="**leet**code*", expected="lecod"),
        ]

        sl = problem.Solution()

        for testcase in testcases:
            got = sl.removeStars(testcase.input)
            self.assertEqual(
                testcase.expected, 
                got, 
                "expected {}, got {}".format(testcase.expected, got),
            )