from collections import Counter
class Solution:
    def getSubarrayBeauty(self, num: list[int], k: int, x: int) -> list[int]:
        # 统计数组长度 window size 为 k
        beauty_list = []
        n = len(num)
        ct = Counter()
        # 滑动取值
        # 第一个窗口
        for i in range(k):
            ct[num[i]] += 1
            if 
        print(ct) 
        
        # return _min


if __name__ == "__main__":
    nums = [1,-1,-3,-2,3]
    # nums = [0,1,1,1,0,0,1,1,0]
    # nums = [1,1,0,0,1]
    # nums = [1,1,1,0,0,1,0,1,1,0]
    s = Solution()
    k = 3
    x = 2
    res = s.getSubarrayBeauty(nums, k, x)
    print(res)