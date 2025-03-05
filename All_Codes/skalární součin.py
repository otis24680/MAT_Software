import numpy as np
import timeit as ti

velikost = 1234567
vektor1 = np.random.rand(velikost) #vytvořím dva náhodné vektory
vektor2 = np.random.rand(velikost)

def skal_python(v1, v2):            #vytvořím funkci pro skalární součin v Pythonu
    součet = 0
    for i in range(len(v1)):
        součet += v1[i] * v2[i]     #sečtení součinů prvků
    return součet

def skal_np(v1, v2):                #samozřejmě i funkci pro skalární součin pomocí NumPy
    return np.dot(v1, v2)

čas_python = ti.timeit(lambda: skal_python(vektor1, vektor2), number=10)    #měření času pro obě funkce
čas_numpy = ti.timeit(lambda: skal_np(vektor1, vektor2), number=10)

print(f"Čas Python: {čas_python:.5f}s")
print(f"Čas NumPy: {čas_numpy:.5f}s")
