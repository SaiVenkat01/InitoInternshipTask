import os

class GrepOperation:
    def __init__(self, file_system, current_path, pattern):
        self.file_system = file_system
        self.current_path = current_path
        self.pattern = pattern

    def execute(self):
        if self.current_path not in self.file_system:
            print(f"Error: Directory '{self.current_path}' not found.")
            return

        matching_files = []
        self._grep_recursive(self.current_path, matching_files)

        if matching_files:
            print(f"Matching files for pattern '{self.pattern}':")
            for file_path in matching_files:
                print(file_path)
        else:
            print(f"No matching files found for pattern '{self.pattern}'.")

    def _grep_recursive(self, current_path, matching_files):
        if current_path not in self.file_system:
            return

        for item, item_info in self.file_system[current_path]['content'].items():
            item_path = os.path.join(current_path, item)

            if item_info['type'] == 'file':
                with open(item_path, 'r') as file:
                    content = file.read()
                    if self.pattern in content:
                        matching_files.append(item_path)
            elif item_info['type'] == 'dir':
                self._grep_recursive(item_path, matching_files)