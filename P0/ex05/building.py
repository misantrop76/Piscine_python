import sys


def main():
    """
    characters counter
    """
    if (len(sys.argv) > 2):
        raise AssertionError("more than one argument is provided")
    elif (len(sys.argv) == 2):
        text = sys.argv[1]
    else:
        text = input("What is the text to count?\n")
    punctuation_str = '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punctuation = sum(1 for c in text if c in punctuation_str)
    space = sum(1 for c in text if c.isspace())
    digit = sum(1 for c in text if c.isdigit())
    print(f"The test contains {len(text)} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punctuation} punctuation marks")
    print(f"{space} spaces")
    print(f"{digit} digits")


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
