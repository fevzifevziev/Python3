import mod_peremen
import modul_1


fail_result = open('де_шифрованный_результат.txt', 'w', encoding='utf-8')
fail_result.close()

i   = 0
KK  = {}                           #Словарь в котором ключ номер буквы в слове, а значение индекс этой буквы в основном массиве
key = []


key = mod_peremen.Key("ключ.txt")


chislo_strok = modul_1.chislo_strok("шифрованный_результат.txt")

for number in range(chislo_strok):
    A      = key
    spisok = modul_1.str(number,"шифрованный_результат.txt")
    length = len(spisok)
    for i in range(len(A)):
        for j in range(len(A[i])):
            for g in range(length):
                if spisok[g]==A[i][j]:
                    KK[g]=i,j
    i = 0

    A      = mod_peremen.Kluch()
    fail_result = open('де_шифрованный_результат.txt', 'a', encoding='utf-8')

    for g in range(length):
        for i in range(len(A)):
            for j in range(len(A[i])):
                (L,K)=KK.get(g)
                if L==i and K==j:
                    fail_result.write(A[i][j]+"")
    fail_result.write("\n")

    fail_result.close()
