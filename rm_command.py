import os

class RmOperation:
    def __init__(self, file_system, current_path, target_path):
        self.file_system = file_system
        self.current_path = current_path
        self.target_path = target_path

    def execute(self):
        path = os.path.join(self.current_path, self.target_path)
        if path in self.file_system:
            del self.file_system[path]
        else:
            print(f"Error: '{self.target_path}' not found.")
