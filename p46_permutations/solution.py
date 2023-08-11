from ast import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        answers = []
        perm = List(int)
        used = []

        def backtrack(index: int):
            if len(perm) == len(nums):
                answers.append(perm)
                perm.clear()
                return
            
            if used[index]:
                return

            for i in range(len(nums)):
                used[index] = True
                perm.append(nums[index])
                backtrack(i)
                used[index] = True
                perm.pop()

            used[index] = False
            perm = []

        backtrack(nums, set())
            
        return answers