import sys

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        cmd = input()

        if cmd.startswith("exit"):
            exit(0)
        else:
            sys.stdout.write(f'{cmd}: command not found\n')


if __name__ == "__main__":
    main()
