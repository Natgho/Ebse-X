#!/usr/bin/env python3
# Hangi paket yoneticisinin oldugu kontrol edilecek. Simdilik tek sistem icin yaziyorum.

# Sistemdeki yuklu python surumunun uyumlulugu denetlenecek

import os
import sys
import time

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



# Sistemde bumblebee olup olmadigi kontrol edilecek.
# Yoksa program surdurulecek, varsa program sonlandirilacak
bumblebee = os.popen("whereis optirun")
for icerik in bumblebee:
    if icerik.find("usr/bin/optirun") != -1:
        tercih=input("Sistemde şu an optirun var gözükmekte.\nSileyim mi?(e/h)")
        if tercih=="h" or  tercih == "H":
            print("Yükleme sonlandırılıyor...")
            sys.exit(0)

#header sisteme ekleniyor
install_header = os.popen("apt-get install linux-headers-generic")
header_checker=0
for headers in install_header:
    print(headers)
    if install_header.find("error") != -1 or install_header.find("hata") != -1:
        print("Programlar yuklenirken hata olustu, lutfen ekran goruntusu alip,\n admin@sezerbozkir.com adresine gonderiniz.")
        header_checker+=1
print("* "*30)
if header_checker==0:
    print("Kaynaklarin eklenmesi icin gerekli olan linuc-headers yuklendi.")

# Bumblebee repositoryleri sisteme eklenecek
print("* "*30)
print("Bumblebee kutuphaneleri sisteme ekleniyor...")
resository_add = os.popen("apt-add-repository ppa:xorg-edgers/ppa")
print("Lutfen ilk kaynagin eklenmesi icin enter tusuna basiniz.")
checker=0
for repository_check in resository_add:
    print(repository_check)
    if repository_check.find("error") != -1:
        print("Kaynaklar eklenirken hata olustu, lutfen ekran goruntusu alip,\n admin@sezerbozkir.com adresine gonderiniz.")
        checker+=1
print("* "*30)
if checker==0:
    print("ilk kaynak  ekleme islemi basari ile gerceklestirildi.")
print("* "*30)

print("Sistem guncellestiriliyor...")
system_update = os.popen("apt-get update")
for updating in system_update:
    print(updating)
print("* "*30)


resository_add2 = os.popen("add-apt-repository ppa:bumblebee/stable")
print("Lutfen ikinci kaynagin eklenmesi icin enter tusuna basiniz.")
checker2=0
for repository_check2 in resository_add2:
    print(repository_check2)
    if repository_check2.find("error") != -1:
        print("Kaynaklar eklenirken hata olustu, lutfen ekran goruntusu alip,\n admin@sezerbozkir.com adresine gonderiniz.")
        checker2+=1
print("* "*30)
if checker2==0:
    print("ikinci kaynak  ekleme islemi basari ile gerceklestirildi.")
print("* "*30)

print("Tum kaynaklar basari ile eklendi,\n bumblebee yuklenmeden once paketlerin guncellenmesi gerekli.")
print("paketler guncellenmeye basliyor...")
time.sleep(3)
print("* "*30)
system_update = os.popen("apt-get update")
for updating in system_update:
    print(updating)
print("* "*30)

# Kurulumlar gerceklestirilecek ve hata kontrolleri yapilacak.
install_bumblebee = os.popen("apt-get install bumblebee bumblebee-nvidia primus")
checker3=0
for icerik2 in install_bumblebee:
    print(icerik2)
    if install_bumblebee.find("error") != -1 or install_bumblebee.find("hata") != -1:
        print("Programlar yuklenirken hata olustu, lutfen ekran goruntusu alip,\n admin@sezerbozkir.com adresine gonderiniz.")
        checker2+=1
print("* "*30)
if checker2==0:
    print("Bumblebee ve yardimci elemanlar basariyla yuklendi.")

print("* "*30)

install_bumblebee = os.popen("apt-get install nvidia-331 nvidia-settings")
checker3=0
for icerik2 in install_bumblebee:
    print(icerik2)
    if install_bumblebee.find("error") != -1 or install_bumblebee.find("hata") != -1:
        print("Programlar yuklenirken hata olustu, lutfen ekran goruntusu alip,\n admin@sezerbozkir.com adresine gonderiniz.")
        checker2+=1
print("* "*30)
if checker2==0:
    print("Nvidia-331 ekran karti ve driver duzenleyici yuklendi.")

print("* "*30)
# Gerekirse geri silme islemleri yapilacak
# 32 bit uyumluluk paketi yuklenecek

#apt-get install linux-headers-generic
# /etc/bumblebee/bumblebee.conf dosyasi acilacak
filee = open("/etc/bumblebee/bumblebee.conf","r")
print("Bumblebee conf dosyanız bulundu;")
conf_icerigi = filee.read()
filee.close()
print(conf_icerigi)
# Dosyanin icerisindeki Driver= kisminin devamina Nvidia eklenecek
print("içerik uygun şekilde değiştirilecek...")
# KernelDriver=nvidia-current kismi yuklenen nvidia surumuyle degistirilecek.
duzeltilmis_conf = conf_icerigi.replace("nvidia-current","nvidia-331")
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

print("* "*40 + "\n\n")
