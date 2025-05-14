def slice_me(family: list, start: int, end: int) -> list:
    """take a list and slice it"""
    if not isinstance(family, list) or not all(isinstance(row, list) for row in family):
        TypeError("must be a list.")
    if len(set(len(row) for row in family)) != 1:
        raise AssertionError("all the list must be the same size.")
    
    print(f"My shape is : ({len(family)}, {len(family[0])})")
    sliced = family[start:end]
    if sliced:
        print(f"My new shape is : ({len(sliced)}, {len(sliced[0])})")
    else:
        print("My new shape is : (0, 0)")
    return sliced
    