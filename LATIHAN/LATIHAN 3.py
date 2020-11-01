def faktorial(n):
    hasil = n
    while(n > 1):
        n -= 1
        hasil *= n
    return hasil

def permutasi(a, b):
    hasil = faktorial(a)/faktorial(a-b)
    return hasil

def kombinasi(a, b):
    hasil = faktorial(a)/(faktorial(a-b)*faktorial(b))
    return hasil


