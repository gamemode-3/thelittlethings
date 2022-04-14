class NoneType:
    def __repr__(self) -> str:
        return "UNDEFINED"

UNDEFINED = NoneType()
'''
Use this instead of None if you are using None as a value.
'''