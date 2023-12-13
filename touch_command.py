import os

class TouchOperation:
    def __init__(self, file_system, current_path, file_name):
        self.file_system = file_system
        self.current_path = current_path
        self.file_name = file_name

    def execute(self):
        path = os.path.join(self.current_path, self.file_name)
        if path not in self.file_system:
            self.file_system[path] = {'type': 'file', 'content': ''}
        else:
            print(f"Error: File '{self.file_name}' already exists.")