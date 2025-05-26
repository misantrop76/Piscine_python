import pandas as p


def load(path: str) -> p:
    """
Takes a path as argument, writes the dimensions of the data set
and returns it
    """
    try:
        df = p.read_csv(path)
        print(f"Loading dataset of dimensions ({df.shape[0]}, {df.shape[1]})")
        return df
    except PermissionError:
        print("Can't open the file (permission).")
    except FileNotFoundError:
        print("File not found.")
    except p.errors.EmptyDataError:
        print("The file is empty.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")
