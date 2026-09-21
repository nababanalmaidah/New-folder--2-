if nilai >= 90:
    print("Kinerja sangat baik")
elif nilai >= 80:
    print("Kinerja sangat baik")
elif nilai >= 70:
    print("Kinerja bagus")
elif nilai >= 60:
    print("Kinerja rata-rata")
else:
    print("Kinerja kurang")


 a = int(input("masukkan bilangan pertama: "))
 b = int(input("Masukkan bilangan kedua: "))
 c = int(input("Masukkan bilangan ketiga: "))

    if a >= b and a >= c:
        terbesar = a
    elif b >= a and b >= c:
        terbesar = b
    else:
        terbesar = c
    print ("Bilangan terbesar adalah:", terbesar)


n = int(input("Masukkan n: "))

a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    a, b = a + b

n = int(input("Masukkan n: "))

for i in range(1, n + 1, 2):
    print(i, end=" ")

n = int(input("Masukkan n: "))

for i in range(1, n + 1):
    for j in range(i):
        print(i, end=" ")
    print()