#---------------------------------------------------------------
# Функция которая возврощает двумерный список "Kluch_1"
#---------------------------------------------------------------
def Kluch():
     Kluch_1 = [
     [ "А","Б","В","Г","Д","Е","Ё","Ж","З","И","Й","К","Л","М"],
     [ "Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ"],
     [ "Ы","Ь","Э","Ю","Я","а","б","в","г","д","е","ё","ж","з"],
     [ "и","й","к","л","м","н","о","п","р","с","т","у","ф","х"],
     [ "ц","ч","ш","щ","ъ","ы","ь","э","ю","я","A","B","C","D"],
     [ "E","F","G","H","I","J","K","L","M","N","O","P","Q","R"],
     [ "S","T","U","V","W","X","Y","Z","a","b","c","d","e","f"],
     [ "g","h","i","j","k","l","m","n","o","p","q","r","s","t"],
     [ "u","v","w","x","y","z","\x20","\x21","\x22","\x23","\x24","\x25","\x26","\x27"],
     [ "\x28","\x29","\x2A","\x2B","\x2C","\x2D","\x2E","\x2F","0","1","2","3","4","5"],
     [ "6","7","8","9","\x3A","\x3B","\x3C","\x3D","\x3E","\x3F","\x40","\x5B","\x5C","\x5D"],
     [ "\x5E","\x5F","\x60","\x7B","\x7C","\x7D","\x7E","\xA1","\xA2","\xA3","\xA4","\xA5","\xA6","\xA7"],
     [ "\xA8","\xA0","\xA9","\xAA","\xAB","\xAC","\xAD","\xAE","\xAF","\xB0","\xB1","\xB2","\xB3","\xB4"],
     [ "\xB5","\xB6","\xB7","\xB8","\xB9","\xBA","\xBB","\xBC","\xBD","\xBE","\xBF","\xC0","\xC1","\xC2"],
     [ "\xC3","\xC4","\xC5","\xC6","\xC7","\xC8","\xC9","\xCA","\xCB","\xCC","\xCD","\xCE","\xCF","\xD0"]
     ]
     return Kluch_1


 #---------------------------------------------------------------
 # Функция которая возврощает двумерный список "key" считывая его из файла "KeY"
 #---------------------------------------------------------------
def Key(KeY):
    key=[]
    i=0
    f = open(KeY, encoding='utf-8')
    for line in f:                  #  CЧИТЫВАНИЕ СОДЕРЖИМОГО ФАЙЛА 'ключ.txt' ПО СТРОЧНО В СПИСОК """ key """
        key.append([])
        for sym in line:
            key[i].append(sym)
        i += 1
        del key[-1][-1]
    f.close()
    return key
