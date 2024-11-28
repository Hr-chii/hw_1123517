#Your Name:Callie
#Student ID:1123517
#Date of Submission:2024/11/28

import heapq

def schedule_tasks(tasks):
    tasks.sort(key=lambda x: -x[0])
    max_profit = 0
    max_deadline = max(task[1] for task in tasks)
    time_slots = [-1] * max_deadline

    for profit, deadline in tasks:
        for i in range(min(deadline, max_deadline) - 1, -1, -1):
            if time_slots[i] == -1:
                time_slots[i] = profit
                max_profit += profit
                break

    scheduled_tasks = [p for p in time_slots if p != -1]
    return max_profit, scheduled_tasks

# Example Input
tasks = [(100, 2), (19, 1), (27, 2), (25, 1)]
profit, schedule = schedule_tasks(tasks)
print("Maximum Profit:", profit)  # Output: Maximum Profit: 127
print("Scheduled Tasks:", schedule)  # Output: Scheduled Tasks: [100, 27]
