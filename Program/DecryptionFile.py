from PRGAAlgorithm import PRGAAlgorithm
from KSAAlgorithm import KSAAlgorithm
import os
import pathlib

inputTextFileName = input("Masukkan Nama File ChiperText : ")
outputTextFileName = input("Masukkan Nama File PlainText : ")

path = str(pathlib.Path().resolve())
inputTextFileNamePath = path + "\\" + inputTextFileName
outputTextFileNamePath = path + "\\" + outputTextFileName

if(os.path.exists(inputTextFileNamePath) and os.path.exists(outputTextFileNamePath)):
    key = input("Masukkan Kunci Dekripsi : ")
    
    with open(inputTextFileName,"r",encoding="utf8") as inputTextFile:
        S = KSAAlgorithm(key).permutation()
        inputText = inputTextFile.read()
        outputText = PRGAAlgorithm(S,inputText).convert()

    with open(outputTextFileName,"w") as outputTextFile:
        outputTextFile.write(outputText)

else:
    print("Berkas File PlainText atau ChiperText Tidak Ditemukan")