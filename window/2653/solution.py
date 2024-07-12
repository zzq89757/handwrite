from collections import Counter
class Solution:
    def getSubarrayBeauty(self, num: list[int], k: int, x: int) -> list[int]:
        # 统计数组长度 window size 为 k
        beauty_list = []
        n = len(num)
        # 滑动取值
        # 第一个窗口
        # ct = Counter(num[:k])
        # 判断倒数第x个元素 即正数第 k-x+1 个
        
        # 后续窗口
        for i in range(n -k):
            if i == 0:ct = Counter(num[:k])
            current_sum = 0
            is_add = 0
            for val, count in ct.items():
                current_sum += count
                if val < 0 and current_sum >= k - x + 1:
                    beauty_list.append(val)
                    is_add = 1
                    break
            if not is_add:beauty_list.append(0)
            ct[num[i-1]] += 1
            ct[num[i + k]] -= 1
            if ct[num[i-1]] == 0:ct.pop(num[i-1])
            print(ct)
        
        print(beauty_list) 
        
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