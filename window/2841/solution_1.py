from collections import Counter
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        ans = 0
        s = sum(nums[:k - 1])  # 先统计 k-1 个数
        cnt = Counter(nums[:k - 1])
        for out, in_ in zip(nums, nums[k - 1:]):
            s += in_  # 再添加一个数就是 k 个数了
            cnt[in_] += 1
            if len(cnt) >= m:
                ans = max(ans, s)
                
            s -= out  # 下一个子数组不包含 out，移出窗口
            cnt[out] -= 1
            if cnt[out] == 0:
                del cnt[out]
        return ans



if __name__ == "__main__":
    # 207ms|击败32.61%  19.55MB|击败43.48%
    # m = Solution().maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4)
    # m = Solution().maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3)
    # m = Solution().maxSum(nums = [1,2,1,2,1,2,1], m = 3, k = 3)
    m = Solution().maxSum(nums = [1,1,1,3], m = 2, k = 2)
    print(m)