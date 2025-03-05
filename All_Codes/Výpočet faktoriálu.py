import scipy as sc
import timeit as ti

def faktorial_s_rekurzi():
    cislo = 800 #číslo, pro které chceme vypočítat faktoriál

    def cyklus(n):        #vytvořím funkci pro výpočet faktoriálu v pythonu
        vysledek = 1
        for i in range(2, n + 1):   
            vysledek *= i           
        return vysledek

    def rekurze(n):       #dále rekurzivní funkci pro výpočet faktoriálu v pythonu
        if n == 0 or n == 1:
            return 1
        return n * rekurze(n - 1)

    def scipy(n):         #nakonec funkci pro výpočet faktoriálu pomocí SciPy
        return sc.special.factorial(n, exact=True)


    cas_cyklus = ti.timeit(lambda: cyklus(cislo), number=10) #funkci zavoláme 10x a změříme čas
    cas_rekurze = ti.timeit(lambda: rekurze(cislo), number=10)
    cas_scipy = ti.timeit(lambda: scipy(cislo), number=10)


    print(f"Čas cyklu pro 800!: {cas_cyklus:.5f}s")
    print(f"Čas rekurze pro 800!: {cas_rekurze:.5f}s")
    print(f"Čas SciPy pro 800!: {cas_scipy:.5f}s")

faktorial_s_rekurzi()

def faktorial_bez_rekurze():
    cislo = 30000

    def cyklus(n):
        vysledek = 1
        for i in range(2, n + 1):
            vysledek *= i
        return vysledek

    def scipy(n):
        return sc.special.factorial(n, exact=True)

    cas_cyklus = ti.timeit(lambda: cyklus(cislo), number=10)
    cas_scipy = ti.timeit(lambda: scipy(cislo), number=10)

    print(f"Čas cyklu pro 30 000!: {cas_cyklus:.5f}s")
    print(f"Čas SciPy pro 30 000!: {cas_scipy:.5f}s")

faktorial_bez_rekurze()
