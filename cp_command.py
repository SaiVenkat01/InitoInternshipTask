import os

class CpOperation:
    def __init__(self, file_system, current_path, source_path, target_path):
        self.file_system = file_system
        self.current_path = current_path
        self.source_path = source_path
        self.target_path = target_path

    def execute(self):
        source = os.path.join(self.current_path, self.source_path)
        target = os.path.join(self.current_path, self.target_path)
        if source in self.file_system:
            self.file_system[target] = self.file_system[source].copy()
        else:
            print(f"Error: Source '{self.source_path}' not found.")
