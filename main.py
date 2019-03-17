class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.task_list = []
        self.complete_tasks_list = []

    def add_new_task(self,Task):
        t = [Task.task_name, Task.duration, Task.start_time, Task.status]
        if t not in self.task_list:
            self.task_list.append(t)
        else:
            print ("the task is already on the task list")

    def complete_current_task(self, Task):
        if Task.task_name == (self.task_list[0])[0]:
            del self.task_list[0]
            self.status = "complete"
            t = [Task.task_name, Task.duration, Task.start_time, Task.status]
            self.complete_tasks_list.append(t)
        else:
            print("Task \""+str(Task.task_name)+"\" is not current")

    def clear_tasks(self):
        self.task_list.clear()

    def completes_numbers(self):
        return len(self.complete_tasks_list)

    def uncompletes_tasks(self):
        uncompletes_tasks_list = []
        for i in self.task_list:
            uncompletes_tasks_list.append(i[0])
        return uncompletes_tasks_list

    def uncompletes_numbers(self):
        return len(self.task_list)


class Task():
    def __init__(self, task_name, duration, start_time):
        self.task_name = task_name
        self.duration = duration
        self.start_time = start_time
        self.status = "new"
