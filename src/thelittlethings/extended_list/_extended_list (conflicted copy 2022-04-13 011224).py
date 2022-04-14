from typing import Iterable


class EList(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
    def merge(self, other):
        for item in other:
            if item not in self:
                self.append(item)
    
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

    def without_duplicates(self):
        new_list = EList()
        for item in self:
            if item not in new_list:
                new_list.append(item)
        return new_list
    
    def clear_from(self, object):
        '''
        Clear the list from the given object.
        '''
        while object in self:
            self.remove(object)
        
    def clear_from_all(self, iterable):
        '''
        Remove all items from the list that are in the iterable.
        '''
        for item in iterable:
            self.clear_from(item)
        
    def without(self, object):
        '''
        Return a new list without the given object.
        '''
        new_list = self.copy()
        new_list.clear_from(object)
        return new_list
    
    def without_all(self, iterable):
        '''
        Return a new list without any of the items in the iterable.
        '''
        new_list = self.copy()
        new_list.clear_from_all(iterable)
        return new_list
    
    def extended(self, iterable):
        new_list = self.copy()
        new_list.extend(iterable)
        return new_list
    
    def join(self, sep: str):
        '''
        Join elements of the list together. All elements must be of type str.
        '''
        return sep.join(self)
        
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
        new_list = self.copy()
        if isinstance(other, Iterable):
            new_list.clear_from_all(other)
        else:
            new_list.clear_from(other)
        return new_list

    def __rsub__(self, other):
        return EList(other) - self

    def __isub__(self, other):
        if isinstance(other, Iterable):
            self.clear_from_all(other)
        else:
            self.clear_from(other)
        return self
    
    def copy(self) -> "EList":
        return EList(self)