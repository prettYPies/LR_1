n = int(input("Введите длину списка: "))
l = [0] * n
for i in range(n):
    print("Введите ", i+1, " элемент списка: ")
    l[i] = int(input(": "))
print("kek  ", n)
k = 1
for i in range(n-1):
    if l[i] < l[i+1]:
        k+=1
print("kol = ", k)
if k == n:
    print("True")
else:
    print("False")
