from main import Person, Task

user1 = Person("Bruce","Wayne")
task1 = Task("become the Batman", "7 years", "2005")
task2 = Task("defeat the Joker", "1 month", "2008")
task3 = Task("to retire", "1 year", "2012")

# add all tasks:
user1.add(task1.all_info)
user1.add(task2.all_info)
user1.add(task3.all_info)
print(user1.task_list)

#finish task1:
user1.complete(task1.all_info)
print(user1.task_list)
user1.show_completes_numbers()


user1.clear()
