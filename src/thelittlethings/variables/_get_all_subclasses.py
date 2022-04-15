from typing import List, TypeVar, Type
from ..extended_list import EList

T = TypeVar('T')

def get_all_subclasses(cls: Type[T]) -> List[Type[T]]:
    """
    get all subclasses and subclasses of subclasses of a class.
    """

    all_subclasses = EList([])

    for subclass in cls.__subclasses__():
        all_subclasses.merge([subclass])
        all_subclasses.merge(get_all_subclasses(subclass))

    return all_subclasses