class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_count = collections.Counter(tasks)
        max_count = max(task_count.values())
        max_value = sum(1 for count in task_count.values() if count == max_count)
        total_length = (max_count - 1) * (n + 1) + max_value
        return max(total_length, len(tasks))