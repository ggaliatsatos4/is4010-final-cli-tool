import argparse
from utils import greet

def main():
    parser = argparse.ArgumentParser(description="Simple CLI tool example")
    parser.add_argument("--name", "-n", help="Your name", required=False)
    args = parser.parse_args()

    if args.name:
        greet(args.name)
    else:
        print("Hello! Use --name to provide your name.")

if __name__ == "__main__":
    main()
