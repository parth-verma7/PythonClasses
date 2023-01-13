class Reader:
    def __init__(self, path: str):
        try:
            self.file = open(path, 'rb')
        except FileNotFoundError:
            raise ValueError("Invalid file path")
        
    def __len__(self):
        current = self.file.tell()
        self.file.seek(0, 2)
        length = self.file.tell()
        self.file.seek(current)
        return length
    
    def __getitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Indexing expects 'int', not 'str'")
        
        if key < 0:
            key = len(self) + key
            
        if ((key >= len(self)) or (key < 0)):
            raise IndexError("Reader index out of range")
            
        self.file.seek(key)
        
        return self.file.read(1)
    
    def close(self):
        self.file.close()
        self.file = None


r=Reader("filename.txt")
print(r[0])
print(r[1])
print(r[-1])
try:
    r["hi"]
except TypeError as e:
    print(f"{type(e).__name__}: {e}")
try:
    r[100]
except IndexError as e:
    print(f"{type(e).__name__}: {e}")