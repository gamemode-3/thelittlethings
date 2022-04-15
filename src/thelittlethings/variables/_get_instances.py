import gc
from typing import List, TypeVar, Type

T = TypeVar('T')

def get_instances(cls: Type[T]) -> List[T]:
    """
    get all instances of a class.
    """
    return [
        object 
        for object in gc.get_objects()
        if isinstance(object, cls)
    ]