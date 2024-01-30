'''
Prompted by a lack of creativity I asked the internet for a sample project idea
Google gave me this TO-DO app
https://medium.com/@pythoncodelab/building-a-to-do-list-app-in-python-a-step-by-step-guide-ce34b9ea141a

Blurb from the post:
"Creating a To-Do List App in Python using PyQt5 is a great way to learn about GUI programming and handling user input. 
This basic version can be extended with features like task deletion, marking tasks as complete, and even persisting 
tasks to a file."
'''
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QListWidget

class ToDoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("To-Do List App")
        self.setGeometry(100, 100, 400, 300)
        
        self.tasks = []
        
        self.layout = QVBoxLayout()
        
        self.input_field = QLineEdit()
        self.add_button = QPushButton("Add Task")
        self.task_list = QListWidget()
        
        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)
        self.layout.addWidget(self.task_list)
        
        self.add_button.clicked.connect(self.add_task)
        
        self.setLayout(self.layout)
    
    def add_task(self):
        task = self.input_field.text()
        if task:
            self.tasks.append(task)
            self.task_list.addItem(task)
            self.input_field.clear()

    def remove_task(self):
        # TODO: Add a remove task function
        pass
    
    def completed_task(self):
        # TODO: create a seperate completed task list
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoApp()
    window.show()
    sys.exit(app.exec_())
