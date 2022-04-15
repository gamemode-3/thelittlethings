from typing import Iterable, Iterator, SupportsIndex, Tuple, TypeVar


T = TypeVar("T")


class EList(list, Iterable[T]):
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and args[0] is None:
            super().__init__()
        else:
            super().__init__(*args, **kwargs)
        
        self._iterators: list[EListIterator] = []
        
    def insert(self, __index: SupportsIndex, __object: T) -> None:
        for iterator in self._iterators:
            if iterator.index >= __index:
                iterator.index += 1

        super().insert(__index, __object)
        return self
    
    def remove(self, __value: T) -> None:
        index = self.index(__value)
        self.pop(index)
        return self
    
    def pop(self, __index: SupportsIndex = ...) -> T:
        for iterator in self._iterators:
            if iterator.index >= __index:
                iterator.index -= 1

        super().pop(__index)
        return self

    def merge(self, other):
        for item in other:
            if item not in self:
                self.append(item)
        return self
    
    def merged(self, other):
        new_list = self.copy()
        new_list.merge(other)
        return new_list

    def clear_duplicates(self):
        original_list = self.copy()
        self.clear()
        for item in original_list:
            if item not in self:
                self.append(item)
        return self

    def without_duplicates(self):
        new_list = EList()
        for item in self:
            if item not in new_list:
                new_list.append(item)
        return new_list
    
    def _clear_from_single_obj(self, object):
        '''
        clear the list from the given object.
        '''
        while True:
            try:
                self.remove(object)
            except ValueError:
                return
    
    def clear_from(self, *objects):
        '''
        remove all given objects from the list.
        '''
        for object in objects:
            self._clear_from_single_obj(object)
        return self
        
    def without(self, *objects):
        '''
        return a new list without the given objects.
        '''
        new_list = self.copy()
        new_list.clear_from(*objects)
        return new_list
    
    def extend(self, __iterable: Iterable[T]) -> None:
        super().extend(__iterable)
        return self

    def extended(self, iterable):
        new_list = self.copy()
        new_list.extend(iterable)
        return new_list
        
    def __add__(self, other):
        new_list = self.copy()
        if isinstance(other, Iterable):
            new_list.extend(other)
        else:
            new_list.append(other)
        return new_list
    
    def __radd__(self, other):
        return self + other
    
    def __iadd__(self, other):
        if isinstance(other, Iterable):
            self.extend(other)
        else:
            self.append(other)
        return self
    
    def __sub__(self, other):
        if isinstance(other, Iterable):
            return self.without(*other)
        else:
            return self.without(other)

    def __rsub__(self, other):
        return EList(other) - self

    def __isub__(self, other):
        if isinstance(other, Iterable):
            self.clear_from(*other)
        else:
            self.clear_from(other)
        return self
    
    def __getitem__(self, index) -> T:
        return super().__getitem__(index)
    
    def __iter__(self) -> "EListIterator[T]":
        return EListIterator(self)
    
    def __and__(self, other):
        new_list = EList()
        for object in self:
            if object in other and object not in new_list:
                new_list.append(object)
        
        return new_list
    
    def __rand__(self, other):
        return self & other
    
    def __iand__(self, other):
        for object in self:
            if object not in other:
                self.remove(object)
        
        return self
    
    def __or__(self, other):
        return self.merged(other)
    
    def __ror__(self, other):
        return self | other
    
    def __ior__(self, other):
        self.merge(other)
        return self

    def __xor__(self, other):
        new_list = EList()
        for object in self:
            if object not in other and object not in new_list:
                new_list.append(object)
        for object in other:
            if object not in self and object not in new_list:
                new_list.append(object)
        
        return new_list
    
    def __rxor__(self, other):
        return self ^ other
    
    def __ixor__(self, other):
        self[:] = (self ^ other)[:]
    
    def enumerate(self):
        return EnumeratedEListIterator(self)

    def copy(self) -> "EList[T]":
        return EList(self)

    def join(self, sep: str = " ") -> str:
        '''
        join elements of the list together. all elements must be of type str.
        '''
        return sep.join([str(item) for item in self])


class EListIterator(Iterator[T]):
    def __init__(self, e_list: EList[T]):
        self.e_list = e_list
        self.e_list._iterators.append(self)
        self.index = 0
    
    def __iter__(self):
        return self
    
    def __next__(self) -> T:
        if self.index >= len(self.e_list):
            self.e_list._iterators.remove(self)
            raise StopIteration
        else:
            self.index += 1
            return self.e_list[self.index - 1]
    

class EnumeratedEListIterator(EListIterator, Iterator[Tuple[int, T]]):
    def __next__(self) -> T:
        if self.index >= len(self.e_list):
            self.e_list._iterators.remove(self)
            raise StopIteration
        else:
            self.index += 1
            return (self.index - 1, self.e_list[self.index - 1])
    