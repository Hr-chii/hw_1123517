#Your Name:Callie
#Student ID:1123517
#Date of Submission:2024/11/28

import heapq

def manage_tasks(operations):
    max_heap = []
    result = []

    for operation in operations:
        if operation.startswith("ADD"):
            _, task_name, priority = operation.split()
            heapq.heappush(max_heap, (-int(priority), task_name))
        elif operation == "GET":
            if max_heap:
                result.append(heapq.heappop(max_heap)[1])
    
    remaining_tasks = [(-p, t) for p, t in max_heap]
    remaining_tasks.sort(reverse=True)
    return result, remaining_tasks

# Example Input
operations = [
    "ADD Task1 10",
    "ADD Task2 15",
    "ADD Task3 5",
    "GET",
    "ADD Task4 20",
    "GET"
]

output, remaining = manage_tasks(operations)
print("\n".join(output))  # Output: Task2, Task4
print(f"Remaining tasks: {remaining}")  # Output: Remaining tasks: [('Task1', 10), ('Task3', 5)]
