class Person():
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.all_task_list = {}
        self.complete_task_list = {}
        self.uncomplete_task_list = {}

    @classmethod
    def get_key(cls,d):
        for k in d.keys():
            return(k)

    def add(self,task):
        if self.get_key(task) not in self.all_task_list:
            print ("added new task: " + str(self.get_key(task)))
        else:
            print ("changed task:" + str(self.get_key(task)))
        self.all_task_list.update(task)
        self.uncomplete_task_list.update(task)

    def complete(self,task):
        comp_task = self.get_key(task)
        if comp_task in self.uncomplete_task_list:
            self.all_task_list.get(comp_task)[2] = "complete"
            del self.uncomplete_task_list[comp_task]
            self.complete_task_list.update(task)
            print("task "+str(comp_task)+" complete")
        else:
            print("error")

    def clear(self, list):
        if list == "all":
            self.uncomplete_task_list.clear()
            self.complete_task_list.clear()
            self.all_task_list.clear()
            print("all your liust of tasks cleared")
        elif list == "uncomplete_task_list":
            for i in self.uncomplete_task_list:
                del self.all_task_list[i]
            self.uncomplete_task_list.clear()
            print("your uncomplete tasks cleared")
        elif list == "complete_task_list":
            self.uncomplete_task_list.clear()
            print("your list of complete tasks cleared")
        else:
            print("error")

    def show_completes_numbers(self):
        i = 0
        for k in self.complete_task_list:
            i += 1
        print("Number of completed tasks: "+str(i))

    def show_uncompletes(self):
        if self.uncomplete_task_list:
            print("uncompletes task:")
            for k in self.uncomplete_task_list:
                print(k)
        else:
            print("uncompletes did not find")
    def show_uncompletes_numbers(self):
        i = 0
        for k in self.uncomplete_task_list:
            i += 1
        print("Number of uncompleted tasks: "+str(i))

class Task():
    def __init__(self, task_name, duration, start_time):
        self.task_name = task_name
        self.duration = duration
        self.start_time = start_time
        self.status = "new"

    @property
    def choose(self):
        d = {self.task_name : [self.duration, self.start_time, self.status]}
        return d
