def all_thing_is_obj(object: any) -> int:
    try:
        obj_type = type(object)
        if (obj_type.__name__ == "str"):
            print(f"{object} is in the kitchen : {obj_type}")
        elif (obj_type.__name__ == "int"):
            print("Type not found")
        else:
            print(f"{obj_type.__name__.capitalize()} {obj_type}")
    except Exception:
        print("Type not found")

    return 42
