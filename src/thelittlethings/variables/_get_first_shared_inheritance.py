def get_first_shared_inheritance(classes: list):
    """
    returns the type all classes inherit from.
    supports multiple inheritance.
    """

    if len(classes) == 0:
        return None

    if len(classes) == 1:
        return classes[0]

    first_shared_inheritance = classes[0]

    for cls in classes[1:]:
        first_shared_inheritance = _get_first_shared_inheritance_recursive(
            cls, first_shared_inheritance
        )

    return first_shared_inheritance


def _get_first_shared_inheritance_recursive(class_a, class_b):
    """
    returns the type both classes inherit from.
    """

    if class_a == class_b:
        return class_a

    if class_a in class_b.__bases__:
        return class_a

    if class_b in class_a.__bases__:
        return class_b

    for base_type in class_a.__bases__:
        result = _get_first_shared_inheritance_recursive(base_type, class_b)

        if result is not None:
            return result

    for base_type in class_b.__bases__:
        result = _get_first_shared_inheritance_recursive(class_a, base_type)

        if result is not None:
            return result

    return None