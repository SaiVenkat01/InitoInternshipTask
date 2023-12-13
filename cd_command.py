import os

class CdOperation:
    def __init__(self, file_system, current_path, target_path):
        self.file_system = file_system
        self.current_path = current_path
        self.target_path = target_path

    def execute(self):
        if self.target_path == '/':
            return '/'
        elif self.target_path.startswith('/'):
            return self.target_path
        else:
            new_path = os.path.join(self.current_path, self.target_path)
            if new_path in self.file_system and self.file_system[new_path]['type'] == 'dir':
                return new_path
            else:
                print(f"Error: Directory '{self.target_path}' not found.")
                return self.current_path
