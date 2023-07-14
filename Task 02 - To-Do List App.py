from google.colab import files

class Task:
    number = 0

    def __init__(self, title, description, status):
        Task.number += 1
        self.task_number = Task.number
        self.title = title
        self.description = description
        self.status = status

    def __str__(self):
        return f"\nTask Number: {self.task_number} \nTitle: {self.title} \nDescription: {self.description} \nStatus: {self.status}"

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, status):
        task = Task(title, description, status)
        self.tasks.append(task)
        print(f"\nNew task has been added to the To-Do List:\n{task}")

    def delete_task(self, task_number):
        for task in self.tasks:
            if task.task_number == task_number:
                self.tasks.remove(task)
                print(f"\nTask {task_number} has been removed from the To-Do List.")
                return
        print(f"\nTask {task_number} was not found in the To-Do List.")

    def view_tasks(self):
        if self.tasks:
            print("\nTo-Do List:")
            for task in self.tasks:
                print(task)
        else:
            print("\nYour To-Do List is empty.")

    def save_tasks(self, file_name):
        try:
            with open(file_name, "w") as file:
                for task in self.tasks:
                    file.write(f"{task.task_number}|{task.title}|{task.description}|{task.status}\n")
            print(f"\nTo-Do List saved to '{file_name}' successfully.")
        except Exception as e:
            print(f"\nError occurred while saving the To-Do List: {str(e)}")

    def load_tasks(self, file_name):
        try:
            with open(file_name, "r") as file:
                self.tasks = []
                for line in file:
                    task_data = line.strip().split("|")
                    task_number = int(task_data[0])
                    title = task_data[1]
                    description = task_data[2]
                    status = task_data[3]
                    task = Task(title, description, status)
                    task.task_number = task_number
                    self.tasks.append(task)
            print(f"\nTo-Do List loaded from '{file_name}' successfully.")
        except FileNotFoundError:
            print(f"\nFile '{file_name}' not found.")
        except Exception as e:
            print(f"\nError occurred while loading the To-Do List: {str(e)}")


# Creating an instance of ToDoList
my_list = ToDoList()
print("Welcome to Your To-Do List. Hope you have a Good Day...")

while True:
    print("\nChoose an option:")
    print("1. Add a New Task")
    print("2. Delete a Task")
    print("3. View Your To-Do List")
    print("4. Save Your To-Do List to a File")
    print("5. Load Your To-Do List from a File")
    print("6. Exit and Download Your To-Do List")
    print("7. Exit without Downloading Your To-Do List")

    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("\nEnter the title: ")
        description = input("Enter task description: ")
        status = input("Enter task status: ")
        my_list.add_task(title, description, status)

    elif choice == "2":
        number = int(input("Enter the task number you want to delete: "))
        my_list.delete_task(number)

    elif choice == "3":
        my_list.view_tasks()

    elif choice == "4":
        my_list.save_tasks("To-Do List.txt")

    elif choice == "5":
        my_list.load_tasks("To-Do List.txt")

    elif choice == "6":
        print("\nYour file is being downloaded...")
        print("Exiting...\nHave a good day...\n")
        files.download("To-Do List.txt")
        break

    elif choice == "7":
        print("\nExiting...\nHave a good day...")
        break

    else:
        print("\nInvalid input. Please enter a correct choice.")
