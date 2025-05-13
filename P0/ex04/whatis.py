import sys


def main():
    """print Even or Odd"""
    if (len(sys.argv) == 1):
        return
    try:
        assert len(sys.argv) == 2, "more than one argument is provided"
        try:
            number = int(sys.argv[1])
        except ValueError:
            raise AssertionError("argument is not an integer")
        if number % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")
    except AssertionError as error:
        print(f"AssertionError: {error}")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
