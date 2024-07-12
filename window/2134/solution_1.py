class Solution:
    def minSwaps(self, num: list[int]) -> int:
        n = len(num)
        k = sum(num)
        # 第一个窗口中1的数目
        _max = _ones = sum(num[:k])
        
        # 后续窗口       
        for i in range(0, n - 1):
            _ones += num[(i + k) % n] - num[i]
            print(_ones)
            if _ones > _max:
                _max = _ones       
        return k - _max





if __name__ == "__main__":
    nums = [0, 1, 0, 1, 1, 0, 0]
    # nums = [0,1,1,1,0,0,1,1,0]
    # nums = [1,1,0,0,1]
    # nums = [1,1,1,0,0,1,0,1,1,0]
    s = Solution()
    res = s.minSwaps(nums)
    # print(res)