import os

class LsOperation:
    def __init__(self, file_system, current_path):
        self.file_system = file_system
        self.current_path = current_path

    def execute(self):
        if self.current_path not in self.file_system:
            print(f"Error: Directory '{self.current_path}' not found.")
            return
        for item in self.file_system[self.current_path]['content']:
            print(item)
