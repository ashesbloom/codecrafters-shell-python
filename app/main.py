import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()

        # Wait for user input
        userInput = input()

        sys.stdout.write(f'{userInput}: command not found\n')

        if userInput == 'exit':
            break

if __name__ == "__main__":
    main()
