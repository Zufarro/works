class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.task_list = []
        self.complete_tasks_list = []

    def add(self,task):
        if task not in self.task_list:
            print ("added new task: " + task[0])
            self.task_list.append(task)
        else:
            print ("the task is already on the task list")

    def complete(self,task):
        if task in self.task_list:
            self.task_list.remove(task)
            task[3] = "complete"
            self.complete_tasks_list.append(task)
            print("task "+task[0]+" complete")
        else:
            print("error")

    def clear(self):
        self.task_list.clear()
        print("task list cleared")

    def show_completes_numbers(self):
        print(self.complete_tasks_list)

    def show_uncompletes(self):
        print(self.tasks_list)

    def show_uncompletes_numbers(self):
        print(len(self.tasks_list))


class Task():
    def __init__(self, task_name, duration, start_time):
        self.task_name = task_name
        self.duration = duration
        self.start_time = start_time
        self.status = "new"
        self.all_info = [self.task_name, self.duration, self.start_time, self.status]
