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
    inputTextFile = open(inputTextFileName,"r")
    outputTextFile = open(outputTextFileName,"w")
    inputText = inputTextFile.read()

    key = input("Masukkan Kunci Dekripsi : ")
    S = KSAAlgorithm(key).permutation()
    outputText = PRGAAlgorithm(S,inputText).convert()
    outputTextFile.write(outputText)

    inputTextFile.close()
    outputTextFile.close()
else:
    print("Berkas File PlainText atau ChiperText Tidak Ditemukan")