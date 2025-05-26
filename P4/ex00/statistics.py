
def ft_statistics(*args: any, **kwargs: any) -> None:
    """
Take in *args a quantity of unknown number and make the Mean, Median,
Quartile (25% and 75%), Standard Deviation and Variance according to the **kwargs
ask
    """
    if not len(args) or not len(kwargs):
        ValueError("ValueError: args or kwargs can't be None.")
        print("ERROR")
        return
    if not all(isinstance(arg, (int | float)) for arg in args):
        TypeError("TypeError: all args must be float or int.")
        print("ERROR")
        return
    Wkwargs = [
        "mean",
        "median",
        "quartile",
        "std",
        "var"
    ]
    if not all (kwarg in Wkwargs for kwarg in kwargs.values()):
        ValueError("ValueError: kwarg not found.")
        print("ERROR")
        return

    mean = sum(args) / len(args)
    print(f"mean = {mean}")
