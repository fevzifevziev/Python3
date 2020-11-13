import random
import modul_1
import mod_peremen
fail_kluch = open('ключ.txt', 'w', encoding='utf-8')     # Открываем файл "ключ.txt"
A      = mod_peremen.Kluch()                           # Присваиваем переменной "A" двумерный список модуля "mod_peremen" функции "Kluch()"

random.shuffle(A)                                   # Перемешиваем все эллементы по СТОЛБЦУ в массиве
for sublist in A:                                 # Перемешиваем все эллементы по СТРОКЕ  в массиве
    random.shuffle(sublist)


for i in range(len(A)):                          # Заполняем файл "ключ.txt" отсортированным двумерным списком "A"
    for j in range(len(A[i])):
        fail_kluch.write(A[i][j])
    fail_kluch.write("\n")
fail_kluch.close()                               # Закрываем файл  "ключ.txt"

for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print("")
print("\n")
