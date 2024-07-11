class Solution:
    def maxScore(self, cardpoint:list, k:int):
        n = len(cardpoint)
        # window n - k
        
        # first time count sum
        _sum = 0
        for  i in range(n - k):
            _sum += cardpoint[i]
        
        # window 