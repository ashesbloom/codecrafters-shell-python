import sys

def echo(cmd):
    sys.stdout.write(cmd.split('echo ')[1] + '\n')


def exiting(cmd):
    return exit(0)


commands = {'echo': echo, 'exit 0': exiting}


def execute(cmd):
    for extract in commands:
        if cmd.startswith(extract):
            commands[extract](cmd)
            return

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        cmd = input()

        if any(cmd.startswith(x)for x in commands.keys()):
            execute(cmd)
        else:
            sys.stdout.write(f'{cmd}: command not found\n')


if __name__ == "__main__":
    main()
