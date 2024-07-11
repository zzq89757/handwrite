class Solution:
    def maxScore(self, cardpoint:list, k:int):
        n = len(cardpoint)
        total = sum(card_point)
        if n == k:return total
        # window n - k
        
        # first time count sum
        _sum = 0
        for  i in range(n - k):
            _sum += cardpoint[i]
        _max_sum = _sum
        
        # window move
        for i in range(n - k, n):
            _remove_item = cardpoint[i - (n - k) + 1]
            _append_item = cardpoint[i]
            _sum = _sum - _remove_item + _append_item
            
            if _sum < _max_sum:_max_sum = _sum
        
        return total - _max_sum
        
        
        
if __name__ == "__main__":
    card_point = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    s = Solution()
    max_score = s.maxScore(card_point, k)
    print(max_score)