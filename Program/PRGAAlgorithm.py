class PRGAAlgorithm:
    def __init__(self,array: list,inputText):
        self.array = array
        self.inputText = inputText

    def convert(self):
        S = self.array
        inputText = self.inputText
        i = 0
        j = 0 

        outputText = ""
        for index in range(0,len(inputText)):
            i = (i + 1) % 256
            j = (j + S[i]) % 256
            S[i], S[j] = S[j], S[i]
            t = (S[i] + S[j]) % 256
            u: int = S[t]
            c = chr(u ^ ord(inputText[index]))
            outputText = outputText + c
        return outputText