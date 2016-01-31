#!/usr/bin/env python3
import os

#Hangi dizinde olduğumuzu öğrenme
print("Şu an ki dizinimiz;")
print(os.getcwd())

#bir metni bir dosyadan okuyup, icerigini editleyip yeniden ayni dosyaya yazma
filer = open("ornek.txt","w")
filer.write("icerisinde bunlar olacak.\nbak ayni zamanda bu da olacak haberin olsun.")
filer.close()
filee = open("ornek.txt","r")
icerik = filee.read()
filee.close()
duzenleme = icerik.replace("bunlar","sezer")
file2 =  open("ornek.txt","w")
file2.write(duzenleme)