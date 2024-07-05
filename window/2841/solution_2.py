from collections import Counter
class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        '''
        如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
        请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
        '''
        
        k_list_sum = sum(nums[0:k])
        k_list_maxsum = 0
        cnt = Counter(nums[:k])
        if len(cnt) >= m:
            k_list_maxsum = max(k_list_maxsum, k_list_sum)
        for i in range(k,len(nums)):
            k_list_sum = k_list_sum + nums[i] - nums[i-k]
            cnt[nums[i]] += 1
            cnt[nums[i-k]] -= 1
            if cnt[nums[i-k]] == 0:
                del cnt[nums[i-k]]
            if len(cnt) >= m:
                k_list_maxsum = max(k_list_maxsum, k_list_sum)
        return k_list_maxsum

if __name__ == "__main__":
    # 193ms|击败55.43%  1949MB|击败75.65%
    # m = Solution().maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4)
    # m = Solution().maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3)
    # m = Solution().maxSum(nums = [1,2,1,2,1,2,1], m = 3, k = 3)
    # m = Solution().maxSum(nums = [1,1,1,3], m = 2, k = 2)
    m = Solution().maxSum(nums = [1,2,2], m = 2, k = 2)
    print(m)