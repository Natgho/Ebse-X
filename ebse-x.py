#!/usr/bin/env python3
# Hangi paket yoneticisinin oldugu kontrol edilecek. Simdilik tek sistem icin yaziyorum.

# Sistemdeki yuklu python surumunun uyumlulugu denetlenecek


import os
import sys

print("* "*40)
print("*\t Merhaba;")
print("*\t Ebse-x V0.1'e Hosgeldiniz :)")
print("*\t Birazdan Otomatik Olarak Ekran Kartlariniz")
print("*\t Tanimlanip, Bumblebee Kurulumu Uygunsa Yukleme Yapialacaktir.")
print("*\t Arkanıza yaslanın ve keyfini çıkarın :)")
print("* "*40 + "\n\n")
# Sistemdeki ekran kartlari lsusb komutuyla ogrenilecek.
kart_sayisi=0
nvidia=0
intel=0
komut = os.popen("lspci")

# Gelen text icerisinde intel ve Nvidia aranacak varsa program
# surdurulecek, yoksa program sonlanacak.
for icerigi in komut.readlines():
    if icerigi.find("VGA") != -1:
        kart_sayisi +=1
        print("* "*30)
        print("Ekran kartlarınızdan birisi tespit edildi.")
        if icerigi.find("NVIDIA") != -1:
            print("Tespit edilen Ekran Kartınız;\n" + icerigi)
            nvidia+=1
            print("* "*30)
        if icerigi.find("ATI") != -1:
            print("Tespit edilen Ekran Kartınız;\n" + icerigi)
        if icerigi.find("Intel"):
            intel+=1
            print("Tespit edilen Ekran Kartınız;\n" + icerigi)
if kart_sayisi < 2:
    print("Sizin sisteminiz hibrit kart sistemi kullanmamakta.")
    sys.exit(0)
else:
    print("Sistemin hibrit olduğu tanımlandı.\nYükleme işlemine başlanıyor...")

print("* "*40 + "\n\n")


# Sistemde bumblebee olup olmadigi kontrol edilecek.
# Yoksa program surdurulecek, varsa program sonlandirilacak
bumblebee = os.popen("whereis optirun")
for icerik in bumblebee:
    if icerik.find("usr/bin/optirun") != -1:
        tercih=input("Sistemde şu an optirun var gözükmekte.\nSileyim mi?(e/h)")
        if tercih=="h" or  tercih == "H":
            print("Yükleme sonlandırılıyor...")
            sys.exit(0)


# Bumblebee repositoryleri sisteme eklenecek
print("Bumblebee kutuphaneleri sisteme ekleniyor...")


# Kurulumlar gerceklestirilecek ve hata kontrolleri yapilacak.
# Gerekirse geri silme islemleri yapilacak

# 32 bit uyumluluk paketi yuklenecek

# /etc/bumblebee/bumblebee.conf dosyasi acilacak

# Dosyanin icerisindeki Driver= kisminin devamina Nvidia eklenecek

# KernelDriver=nvidia-current kismi yuklenen nvidia surumuyle degistirilecek.

# LibraryPath kisminin sonu editlenecek.

# Default xorg modules... ile baslayan kisim editlenecek.

# Islemi garantiye almak icin bumblebee servisi restartlanacak.

# Calismasini kontrol etmek icin normal glxgears baslatilip FPS orani incelenecek.

# Optirun ile glxgears baslatilip FPS orani kontrol edilecek.

# Programin dogru calistigina dair bilgi verilecek ve sistem bilgileri gosterilecek.

#İslem bitiminin ardindan kendi siteme gidecek ama belli bir sure sonra;
#web.open("http://www.istihza.com")

# Kurulum sirasinda faydalanabilinecek kaynaklar:
# https://forum.linuxmint.net.tr/index.php?topic=78.0
# http://enginsezen.com/blog/gnu-linux/31-bumblebee-kurulumu.html
# http://ubuntulog.com/bumblebee-kurulumu.html

