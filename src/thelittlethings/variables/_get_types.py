def get_types(*objects):
    """
    returns the types of all objects.
    """

    return (*(type(obj) for obj in objects),)