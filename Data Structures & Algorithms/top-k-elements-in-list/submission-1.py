class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} #第一次map,   k=数值,v=频次
        freq = [ [] for i in range(len(nums)+1)] # 创建一个二维数据

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():# 用第一次map组装二维数组
            freq[c].append(n)  # 这时候 数组下角标是频次, val是有频次的数

        res = []
        for i in range(len(freq)-1,0,-1): # freq从后往头数
            for n in freq[i]:
                res.append(n)# 把高频词数装进res里去
                if len(res) == k: # 装到要求的数量k了
                    return res