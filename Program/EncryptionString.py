from PRGAAlgorithm import PRGAAlgorithm
from KSAAlgorithm import KSAAlgorithm

plainText = input("Masukkan PlainText : ")
key = input("Masukkan Kunci Enkripsi : ")

S = KSAAlgorithm(key).permutation()
chiperText = PRGAAlgorithm(S,plainText).convert()
print("ChiperText : %s" % chiperText)