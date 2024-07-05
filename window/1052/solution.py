class Solution():
    def maxSatisfied(self, customers: list[int], grumpy: list[int], minutes: int) -> int:
        n = len(customers) - minutes
        if n <= 0:return sum(customers)
        # 计算不抑制时的客流量（原始客流量）
        raw_total_customer = sum([customers[i] for i, x in enumerate(grumpy) if x - 1])
        # 计算每个窗口抑制与不抑制的差值 找到差值最大的窗口 最大差值与原始客流量之和即为所求
        max_diff = 0 
        for i in range(n + 1):
            customers_kmer = customers[i:i + minutes]
            grumpy_kmer = grumpy[i:i + minutes]
            diff = sum(customers_kmer) - sum([customers_kmer[i] for i, x in enumerate(grumpy_kmer) if x - 1])
            if diff > max_diff: max_diff  = diff
        return raw_total_customer + max_diff


if __name__ == "__main__":
    # 8278ms|击败5.01%  18.57MB|击败7.58%
    s = Solution().maxSatisfied(customers = [1,0,1,2,1,1,7,5], grumpy = [0,1,0,1,0,1,0,1], minutes = 3)
    print(s)
    s = Solution().maxSatisfied(customers = [1], grumpy = [0], minutes = 1)
    print(s)