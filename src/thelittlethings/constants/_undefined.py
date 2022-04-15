class NoneType:
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.UNDEFINED = super(NoneType, cls).__new__(cls)
        return cls.UNDEFINED

    def __repr__(self) -> str:
        return "UNDEFINED"
    
    def __bool__(self) -> bool:
        return False
    
    def __eq__(self, other: object) -> bool:
        return other is self

UNDEFINED = NoneType()
'''
Use this instead of None if you are using None as a value.
'''