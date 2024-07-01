import sys
import os

paths = os.environ.get('PATH').split(':')

def type(cmd):
    command = cmd.split('type ')[1]
    if command in commands:
        sys.stdout.write(f'{command} is a shell builtin\n')
        return
    for path in paths:
        full_path = os.path.join(path, command)
        if os.path.isfile(full_path):
            sys.stdout.write(full_path + '\n')
            return
    sys.stdout.write(f'{command}: not found\n')


def echo(cmd):
    sys.stdout.write(cmd.split('echo ')[1] + '\n')


def exiting(cmd):
    return exit(0)


commands = {'echo': echo, 'exit': exiting, 'type': type}


def execute(cmd):
    for extract in commands:
        if cmd.startswith(extract):
            commands[extract](cmd)
            return
    if cmd and ' ' in cmd:
        for path in paths:
            full_path = os.path.join(path, cmd.split(' ')[1])
            if os.path.isfile(full_path):
                os.system(full_path)
                return
    sys.stdout.write(f'{cmd}: command not found\n')

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        cmd = input()

        # if any(cmd.startswith(x)for x in commands.keys()):
        execute(cmd)

if __name__ == "__main__":
    main()
