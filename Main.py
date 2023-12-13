import os
import json
from cat_command import CatOperation
from cd_command import CdOperation
from cp_command import CpOperation
from echo_command import EchoOperation
from grep_command import GrepOperation
from ls_command import LsOperation
from mkdir_command import MkdirOperation
from mv_command import MvOperation
from rm_command import RmOperation
from touch_command import TouchOperation

def run_filesystem():
    global current_path,file_system_path,file_system
    current_path = '/'
    file_system_path = 'filesystem_state.json'
    file_system = {'/': {'type': 'dir', 'content': {}}}

    while True:
        print("Enter the command\n")
        command = input(f"{current_path}> ").strip().split()
        if not command:
            continue

        operation = command[0]
        args = command[1:]

        if operation == 'exit':
            with open(file_system_path, 'w') as file:
                json.dump(file_system, file)
            break
        elif operation == 'mkdir':
            MkdirOperation(file_system, current_path, *args)
            #mkdir_operation.execute()
        elif operation == 'cd':
            cd_operation = CdOperation(file_system, current_path, *args)
            current_path = cd_operation.execute()
        elif operation == 'ls':
            ls_operation = LsOperation(file_system, current_path)
            ls_operation.execute()
        elif operation == 'grep':
            grep_operation = GrepOperation(file_system, current_path, *args)
            grep_operation.execute()
        elif operation == 'cat':
            cat_operation = CatOperation(file_system, current_path, *args)
            cat_operation.execute()
        elif operation == 'touch':
            touch_operation = TouchOperation(file_system, current_path, *args)
            touch_operation.execute()
        elif operation == 'echo':
            echo_operation = EchoOperation(file_system, current_path, args[0], ' '.join(args[1:]))
            echo_operation.execute()
        elif operation == 'mv':
            mv_operation = MvOperation(file_system, current_path, *args)
            mv_operation.execute()
        elif operation == 'cp':
            cp_operation = CpOperation(file_system, current_path, *args)
            cp_operation.execute()
        elif operation == 'rm':
            rm_operation = RmOperation(file_system, current_path, *args)
            rm_operation.execute()
        else:
            print("Error: Invalid command.")

if __name__ == "__main__":
    run_filesystem()




