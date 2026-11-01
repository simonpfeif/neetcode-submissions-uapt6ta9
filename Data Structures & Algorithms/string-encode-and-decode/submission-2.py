class Solution:
    def __init__(self):
        self.codes = {}
        self.count = 0

    def getCode(self) -> str:
        self.count += 1
        return str(self.count)
        
    def encode(self, strs: List[str]) -> str:
        key = self.getCode()
        self.codes[key] = strs
        return key


    def decode(self, s: str) -> List[str]:
        return self.codes[s]