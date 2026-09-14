class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i,val in enumerate(strs):
            sortVal = sorted(val)
            if tuple(sortVal) not in res:
                res[tuple(sortVal)] = [val]
            else:
                res[tuple(sortVal)].append(val)
        return list(res.values())