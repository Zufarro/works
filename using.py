from main import Person, Task

user1 = Person("Bruce","Wayne")
task1 = Task("become the Batman", "7 years", "2005")
task2 = Task("defeat the Joker", "1 month", "2008")
task3 = Task("to retire", "1 year", "2012")

# add all tasks:
user1.add_new_task(task1)
user1.add_new_task(task2)
user1.add_new_task(task3)
print(user1.task_list)

#finish task1:
user1.complete_current_task(task1)
print(user1.task_list)

print(user1.completes_numbers())

print(user1.uncompletes_tasks())
user1.clear_tasks()
