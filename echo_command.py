import os

class EchoOperation:
    def __init__(self, file_system, current_path, file_name, text):
        self.file_system = file_system
        self.current_path = current_path
        self.file_name = file_name
        self.text = text

    def execute(self):
        path = os.path.join(self.current_path, self.file_name)
        if path in self.file_system and self.file_system[path]['type'] == 'file':
            self.file_system[path]['content'] = self.text
        else:
            print(f"Error: File '{self.file_name}' not found.")