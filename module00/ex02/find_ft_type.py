def all_thing_is_obj(object: any) -> int:
    if isinstance(object, list):
        print(f"List : {object.__class__}")
    elif isinstance(object, tuple):
        print(f"Tuple : {object.__class__}")
    elif isinstance(object, set):
        print(f"Set : {object.__class__}")
    elif isinstance(object, dict):
        print(f"Dict : {object.__class__}")
    elif isinstance(object, str):
        print(f"{object} is in the kitchen : {object.__class__}")
    else:
        print("Type not found")
    return 42
