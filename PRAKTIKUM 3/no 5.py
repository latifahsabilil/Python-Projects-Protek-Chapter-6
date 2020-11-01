from Operation import*

print('1. ', end = '')
a = 2
b = 4
c = 6
print(a, '+', b, 'x', c, '-', b, '=', kurang(jumlah(a, kali(b, c)), b))

print('2. ', end = '')
a = 4
b = 7
c = 6
d = 9
print(a, '+', b, 'x', c, '-', d, '=', kali(jumlah(a, b), kurang(c, d)))


print('3. ', end = '')
a = 10
b = 2
c = 7
d = 5
e = 12
f = 34
print(a, '+', b, '/', c, '+', d, '/', e, '-', f, '=', bagi((bagi(jumlah(a, b), jumlah(c, d))), kurang(e, f)))
