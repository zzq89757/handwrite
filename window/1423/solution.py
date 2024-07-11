class Solution:
    def maxScore(self, cardpoint:list, k:int):
        n = len(cardpoint)
        total = sum(cardpoint)
        if n == k:return total
        # window n - k
        
        # first time count sum
        _sum = 0
        for  i in range(n - k):
            _sum += cardpoint[i]
        _max_sum = _sum
        # window move
        for i in range(n - k, n):
            _remove_item = cardpoint[i - (n - k)]
            _append_item = cardpoint[i]
            _sum = _sum - _remove_item + _append_item
            if _sum < _max_sum:_max_sum = _sum
        
        return total - _max_sum
        
        
        
if __name__ == "__main__":
    card_point = [96,90,41,82,39,74,64,50,30]
    k = 8
    s = Solution()
    max_score = s.maxScore(card_point, k)
    print(max_score)