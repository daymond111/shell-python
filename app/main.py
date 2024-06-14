import sys

VALID_COMMANDS = []

def prompt_user():
    sys.stdout.write("$ ")
    sys.stdout.flush()
    return input()

def execute_command(command):
    if command not in VALID_COMMANDS:
        print(f"{command}: command not found")

def main():
    while True:
        command = prompt_user()
        execute_command(command)

if __name__ == "__main__":
    main()
