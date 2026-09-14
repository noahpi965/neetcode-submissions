class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # first val-freq map
        freq = [ [] for i in range(len(nums) + 1) ] # set buckets all freqs 
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        for num, cunt in count.items():
            freq[cunt].append(num)

        res = []
        for i in range(len(freq) -1, 0, -1): # from the end of freq to start
            for num in freq[i]: # every index arr of freq,foreach its int
                res.append(num) # res insert most freq int
                if len(res) == k: # res enough
                    return res

