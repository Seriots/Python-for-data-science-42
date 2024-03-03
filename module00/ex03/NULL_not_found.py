def NULL_not_found(object: any) -> int:
    if object is None:
        print(f"Nothing: None {object.__class__}")
    elif isinstance(object, float) and object != object:
        print(f"Cheese: nan {object.__class__}")
    elif isinstance(object, bool) and object is False:
        print(f"Fake: False {object.__class__}")
    elif object == '':
        print(f"Empty: {object.__class__}")
    elif isinstance(object, int) and object == 0:
        print(f"Zero: 0 {object.__class__}")
    else:
        print("Type not found")
        return 1
    return 0
