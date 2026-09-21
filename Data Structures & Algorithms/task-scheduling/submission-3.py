class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        maxf = max(count)
        maxCount = 0
        for cnt in count:
            if cnt == maxf:
                maxCount += 1
        time = ((maxf - 1) * n) + maxf + maxCount - 1
        return max(len(tasks), time)