class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the occurrence of each task using a Counter.
        # It will give a dictionary where keys are tasks and values are the number of times each task occurs.
        # collections.Counter() is a built-in function in Python's collections module.
        # It is used for counting the frequency of elements in a container.
        # collections.Counter() returns a dictionary-like object,
        # where the keys are the elements in the input iterable and the values are the counts of the corresponding elements.
        task_count = collections.Counter(tasks)

        # Find the maximum occurrence count among all tasks. This is the count of the most frequent task.
        max_count = max(task_count.values())

        # Count how many tasks have the maximum occurrence count.
        # This is needed to handle the scenario where multiple tasks have the same highest count.
        max_tasks = sum (1 for count in task_count.values() if count == max_count)

        # Calculate the total slots required to schedule the tasks without any task being executed within 'n' interval
        # of itself.
        # Each slot is a potential time unit.
        # (max_count - 1) * (n + 1) -> gives slots required for most frequent tasks excluding the last sequence
        # max_tasks -> add the slots for the last sequence of max frequent tasks.
        total_slots = (max_count - 1) * (n + 1) + max_tasks

        # We compare total_slots and len(tasks) because when there are more tasks than total_slots calculated,
        # we can always schedule the additional tasks in the idle slots,
        # hence the minimum time required will be equal to the number of tasks.
        # When the total_slots are more, some idle time needs to be inserted for which we return total_slots
        return max(total_slots, len(tasks))
