import argparse
from argparse import ArgumentParser
from importlib.metadata import distributions


def main():
    parser = ArgumentParser()
    parser.add_argument(
        "-s",
        "--solution",
        type=argparse.FileType("r"),
        help="requirements.txt without annotations with the solution",
        required=False,
    )
    args = parser.parse_args()

    queens = {}

    if not args.solution:
        for dist in distributions():
            name = dist.metadata["Name"]
            if name.startswith("queen"):
                queens[name[6:]] = int(dist.version)
    else:
        for line in args.solution.read().splitlines():
            if line.startswith("queen"):
                col, row = line.split("==")
                queens[col[6:]] = int(row)

    print("   a b c d e f g h")
    print(" ┌─────────────────┐")
    for row in range(8, 0, -1):
        print(f"{row}│", end="")
        for col in "abcdefgh":
            if queens.get(col) == row:
                print(" Q", end="")
            else:
                print(" ·", end="")
        print(f" │{row}")
    print(" └─────────────────┘")
    print("   a b c d e f g h")


if __name__ == "__main__":
    main()
