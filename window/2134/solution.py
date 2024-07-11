class Solution:
    def minSwaps(self, num: list[int]) -> int:
        # 统计1的个数作为 window size，1最多的窗口中0的数目即为所求
        n = len(num)
        k = sum(num)
        # 逆向思维：统计1的个数k，n-k 为window size，找和最小的窗口
        # 需考虑0比1多时 能够交换的1 不够的问题！！
        # 第一个窗口
        _min = _current = sum(num[:n - k])
        # 后续窗口 仅考虑滑出和滑入的值
        for i in range(n - k, n):
            _current += num[i] - num[i - (n - k)]
            if _current < _min:
                _min = _current
        
        for i in range(-(n-k-1), 0, 1):
            print(i)  
        return _min





if __name__ == "__main__":
    nums = [0, 1, 0, 1, 1, 0, 0]
    # nums = [0,1,1,1,0,0,1,1,0]
    # nums = [1,1,0,0,1]
    # nums = [1,1,1,0,0,1,0,1,1,0]
    s = Solution()
    res = s.minSwaps(nums)
    print(res)