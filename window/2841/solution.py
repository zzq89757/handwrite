class Solution:
    def maxSum(self, nums: list[int], m: int, k: int) -> int:
        '''
        如果 nums 的一个子数组有至少 m 个互不相同的元素，我们称它是 几乎唯一 子数组。
        请你返回 nums 中长度为 k 的 几乎唯一 子数组的 最大和 ，如果不存在几乎唯一子数组，请你返回 0 。
        '''
        k_list = []
        k_list_sum = 0
        k_list_maxsum = 0
        # 第一个窗口
        for i in range(k):
            k_list.append(nums[i])
            k_list_sum += nums[i]
        if len(set(k_list)) >= m:
                k_list_maxsum = k_list_sum
        for i in range(k,len(nums)):
            k_list_sum = k_list_sum + nums[i] - nums[i-k]
            # 操作列表性能差 只要求互不相同的元素个数 用Count
            del(k_list[0])
            k_list.append(nums[i])
            if len(set(k_list)) >= m:
                k_list_maxsum = max(k_list_maxsum, k_list_sum)
                # print(k_list_maxsum)
        return k_list_maxsum

if __name__ == "__main__":
    # 6075ms|击败13.48%  21.22MB|击败7.83%
    # m = Solution().maxSum(nums = [2,6,7,3,1,7], m = 3, k = 4)
    # m = Solution().maxSum(nums = [5,9,9,2,4,5,4], m = 1, k = 3)
    # m = Solution().maxSum(nums = [1,2,1,2,1,2,1], m = 3, k = 3)
    m = Solution().maxSum(nums = [1,1,1,3], m = 2, k = 2)
    # print(m)