from collections import Counter
class Solution:
    def getSubarrayBeauty(self, num: list[int], k: int, x: int) -> list[int]:
        # 统计数组长度 window size 为 k
        beauty_list = []
        n = len(num)
        # 滑动取值
        # 第一个窗口
        ct = Counter(num[:k])
        # 判断倒数第x个元素 即正数第 k-x+1 个
        
        # 后续窗口
        for i in range(k,n + 1):
            # 逆向操作 发现一个次数减一 移除则加1 然后当k==x时用 most_common x ==1 时 则
            if k == x:
                ct
            current_sum = 0
            is_add = 0
            for val, count in sorted(ct.items(),key=lambda x:x[0], reverse=True):
                current_sum += count
                if val < 0 and current_sum >= k - x + 1:
                    beauty_list.append(val)
                    is_add = 1
                    break
            if not is_add:beauty_list.append(0)
            if i != n:
                ct[num[i]] += 1
                ct[num[i-k]] -= 1
                if ct[num[i-k]] == 0:ct.pop(num[i-k])
        
        return beauty_list 


if __name__ == "__main__":
    nums = [1,-1,-3,-2,3]
    # nums = [-1,-2,-3,-4,-5]
    nums = [-50,14]
    # nums = [1,1,1,0,0,1,0,1,1,0]
    s = Solution()
    # k = 3
    k = 2
    x = 2
    res = s.getSubarrayBeauty(nums, k, x)
    print(res)