lst = [1, 2, 3, 4, 5, 6, "a", "b", "c", "d"]

task_nr_1 = lst[:6]
task_nr_2 = lst[6:]
task_nr_3 = lst[::3]

print(f"Select numbers only: {task_nr_1}")
print(f"Select letters only: {task_nr_2}")
print(f"Select every third element: {task_nr_3}")
