import os 

class MkdirOperation:
    def __init__(self, file_system, current_path, directory_name):
        self.file_system = file_system
        self.current_path = current_path
        self.directory_name = directory_name
        path = os.path.join(self.current_path, self.directory_name)
        if path not in self.file_system:
            self.file_system[path] = {'type': 'dir', 'content': {}}
        else:
            print(f"Error: Directory '{self.directory_name}' already exists.")

        