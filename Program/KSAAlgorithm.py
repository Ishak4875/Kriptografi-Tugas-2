class KSAAlgorithm:
    def __init__(self,key: str):
        self.key = key
    
    def permutation(self):
        key = self.key
        S = [i for i in range(256)]

        j = 0
        for i in range(0,256):
            j = (j + S[i] + ord(key[i % len(key)])) % 256
            S[i], S[j] = S[j], S[i]
        return S