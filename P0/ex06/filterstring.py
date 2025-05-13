import sys


def main():
    """take a string S and an integer N and output a\
 list of words from S with a length greater than N"""
    assert len(sys.argv) == 3, "the arguments are bad"
    assert isinstance(sys.argv[1], str), "the arguments are bad"
    try:
        s = sys.argv[1]
        n = int(sys.argv[2])
    except Exception:
        raise AssertionError("the arguments are bad")

    result = [word for word in s.split() if (lambda w: len(w) > n)(word)]
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
