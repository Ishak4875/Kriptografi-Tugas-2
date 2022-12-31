from PRGAAlgorithm import PRGAAlgorithm
from KSAAlgorithm import KSAAlgorithm

chiperText = input("Masukkan ChiperText : ")
key = input("Masukkan Kunci Dekripsi : ")

S = KSAAlgorithm(key).permutation()
plainText = PRGAAlgorithm(S,chiperText).convert()
print("PlainText : %s" % plainText)