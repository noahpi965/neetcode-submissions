class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        back = set()
        for i in nums:
            if i in back:
                return True
            back.add(i)
        return False