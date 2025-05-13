import sys

NESTED_MORSE = {
    "A": ".-",    "B": "-...",  "C": "-.-.",  "D": "-..",   "E": ".",
    "F": "..-.",  "G": "--.",   "H": "....",  "I": "..",    "J": ".---",
    "K": "-.-",   "L": ".-..",  "M": "--",    "N": "-.",    "O": "---",
    "P": ".--.",  "Q": "--.-",  "R": ".-.",   "S": "...",   "T": "-",
    "U": "..-",   "V": "...-",  "W": ".--",   "X": "-..-",  "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    " ": "/"
}


def main():
    """print an alphanumeric string in Morse"""
    assert len(sys.argv) == 2, "the arguments are bad"

    input_str = sys.argv[1].upper()
    if not all(c in NESTED_MORSE for c in input_str):
        raise AssertionError("the arguments are bad")
    result = ' '.join(NESTED_MORSE[c] for c in input_str)
    print(result)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
