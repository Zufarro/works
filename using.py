from main import Person, Task

user1 = Person("Bruce","Wayne")
task1 = Task("become the Batman", "7 years", "2005")
task2 = Task("defeat the Joker", "1 month", "2008")
task3 = Task("to retire", "1 year", "2012")

# add all tasks:
user1.add(task1.choose)
user1.add(task2.choose)
user1.add(task3.choose)
print(user1.all_task_list)

#finish task1:
user1.complete(task1.choose)
print(user1.all_task_list)
user1.show_uncompletes()
user1.show_uncompletes_numbers()
user1.show_completes_numbers()

#cler uncomplete task
user1.clear("uncomplete_task_list")
user1.show_uncompletes()
print(user1.all_task_list)
