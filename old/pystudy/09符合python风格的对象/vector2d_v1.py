@classmethod
def frombytes(cls, octets):
    typecode = chr(octets[0])
    memv = memoryview(octets[:]).cast(typecode)
    return cls(*memv)