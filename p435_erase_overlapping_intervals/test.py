from dataclasses import dataclass
from typing import List
import unittest
import solution

class TestSolution(unittest.TestCase):
    def test_erase_overlap_intervals(self):
        @dataclass
        class TestCase:
            intervals: List[List[int]]
            expected: int

        testcases = [
            TestCase(intervals=[[1,2],[2,3],[3,4],[1,3]], expected=1),
            TestCase(intervals=[[1,2],[1,2],[1,2]], expected=2),
            TestCase(intervals=[[1,2],[2,3]], expected=0),
        ]

        sl = solution.Solution()
        for testcase in testcases:
            want, got = testcase.expected, sl.eraseOverlapIntervals(testcase.intervals)
            self.assertEqual(
                    want, 
                    got, 
                    "expected {}, got {}".format(testcase.expected, got),
                )