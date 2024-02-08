import math

import numpy as np
import matplotlib.pyplot as plt

L = 5
l_el = 10
d = 0.175
F = 1800
le = L/l_el
I = (math.pi * pow(d,4))/64
E = 2.0e11
A = (math.pi * (pow(d/2,2)))
a1 = E*(A/le)
a2 = E*(I/pow(le,3))
l_wiezow = l_el + 1
l_skladowych = l_wiezow * 3
print(l_skladowych)

ke = np.matrix([[a1,0,0,-a1,0,0],
                     [0,12*a2,6*a2,0,-12*a2,6*a2],
                     [0,6*a2,4*a2,0,-6*a2,2*a2],
                     [-a1,0,0,a1,0,0],
                     [0,-12*a2,-6*a2,0,12*a2,-6*a2],
                     [0,6*a2,2*a2,0,-6*a2,4*a2]])
print("MACIERZ ke:")
print(ke)
print("______________________________________________________________________________")

K = np.zeros((l_skladowych, l_skladowych))
for i in range(0,l_el):
    K[0+(3*i):6+(3*i),0+(3*i):6+(3*i)]+=ke
print("MACIERZ GLOBALNA (przed wycinaniem): ")
print(K)
print("______________________________________________________________________________")

print("MACIERZ GLOBALNA (po wycieciu): ")
K = np.delete(K, [0, 1, 16], axis=0)
K = np.delete(K, [0, 1, 16], axis=1)
print(K)
print("______________________________________________________________________________")

wektor_obciazen = np.zeros(len(K))
wektor_obciazen[len(wektor_obciazen)-2] = -F

print("WEKTOR OBCIAZEN: ")
print(wektor_obciazen)
print("______________________________________________________________________________")

wektor_przemieszczen = np.linalg.solve(K,wektor_obciazen)
print("WEKTOR PRZEMIESZCZEN: ")
print(wektor_przemieszczen)
print("______________________________________________________________________________")

f = (F*pow(L,3))/(12*E*I)
print("Analitycznie: ")
print(f)
print("MES: ")
print(wektor_przemieszczen[len(wektor_przemieszczen)-2])
print("Błąd dokładności pomiaru: ")
print(abs(abs(wektor_przemieszczen[len(wektor_przemieszczen)-2]) - f))
print("______________________________________________________________________________")
x = np.zeros(11)
for i in range(1,11):
    x[i] = i * le
y = np.zeros(11)
for i in range(0,10):
    y[i+1] = wektor_przemieszczen[1 + (i*3)]

plt.plot(x,y, marker='o')
plt.title('Wykres przemieszczeń w węzłach siatki MES')
plt.xlabel('Odległość [m]')
plt.ylabel('Przemieszczenia [m]')
plt.grid(True)
plt.show()