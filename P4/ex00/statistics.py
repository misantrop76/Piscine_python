
def ft_statistics(*args: any, **kwargs: any) -> None:
    """
Take in *args a quantity of unknown number and make the Mean, Median,
Quartile (25% and 75%), Standard Deviation and
Variance according to the **kwargs ask
    """
    if not all(isinstance(arg, (int | float)) for arg in args):
        print("ERROR")
        return
    data = sorted(args)

    def mean():
        return sum(data) / len(data)

    def median():
        mid = len(data) // 2
        if (len(data) % 2 == 0):
            return (data[mid - 1] + data[mid]) / 2
        return (data[mid])

    def quartile():
        def percentile(p):
            pos = (len(data) - 1) * p
            lower = int(pos)
            upper = lower + 1
            if upper >= len(data):
                return data[lower]
            weight = pos - lower
            return data[lower] * (1 - weight) + data[upper] * weight
        return [percentile(0.25), percentile(0.75)]

    def std():
        m = mean()
        return (sum((x - m) ** 2 for x in data) / len(data)) ** 0.5

    def var():
        m = mean()
        return sum((x - m) ** 2 for x in data) / len(data)

    stat_foncs = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var,
    }
    for value in kwargs.values():
        func = stat_foncs.get(value)
        if func:
            if (not args):
                result = "ERROR"
            else:
                result = f"{value} : {func()}"
            print(result)
