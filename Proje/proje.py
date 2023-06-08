import pandas as pd
import sqlite3
import numpy as np
#SÖZLÜK LİSTE VE DEĞER 
admin=("Mehmet12","Neslihan51","Batuhan34")
admin_sfr={admin[0]:3124234,admin[1]:32432523,admin[2]:24234234}
misafir_tc={}
kullanıcılar=["ALi","Ayşe","Murat"]
kullanıcı_sfr={"ALi":"32452"}
veri = pd.read_csv("Kitap3.csv", sep=';',encoding='ISO-8859-1')
y =pd.DataFrame(veri,columns=["bolge","katsayi"])
bolge_katsayıları={"pendik":y["katsayi"][0],"maltepe":y["katsayi"][1],"sultanbeyli":y["katsayi"][2],"kadıköy":y["katsayi"][3],"üsküdar":y["katsayi"][4]}
x=0
T=2

sorular=["bina numarasını giriniz","binanızın bölgesini giriniz","Binanızın değerini giriniz ","Binanızın metrekaresini giriniz","Binanızın kaç +1 olduğunu giriniz"]
#DEF fonksiyonu
def admin_giriş(x,i):
      while(x<3):
          sifre=input("şifrenizi giriniz")
          if(sifre==str(admin_sfr[admin[i-1]])):
              x=3
              print("hoş geldiniz",admin[i-1])
              print("""
                    1.Kullanıcıların listesini ve değişiklik yapmak için 1'i tıklatınız
                    2.Misafir kullanıcıların listesini görmek için 2'i yi tıklayınız
                    3.Girilen binalara ne yapılcağını görmek için 3'e tıklayınız
                    
                    4.Bölge katsayılarını görüntülemek ve değiştrmek için 4'e tıklayınız""")
              deger=input()
              return deger
          else:
              print("""yanlis girdiniz 
                    şifreyi unuttuysanız yetkili birine iletmeniz gerekecektir""")
              x+=1
              print("son",3-x,"hakkınız kaldı")
          
def Bina_bilgileri_girisi():
    
    veriler=[]
    Bina_bilgisi=[]
    vt=sqlite3.connect("Bina_tablosu.db")
    im=vt.cursor()
    for i in range(5):
        print(sorular[i-1])
        deger=input()
        Bina_bilgisi.append(deger)
    veriler.extend(tuple(Bina_bilgisi))
    im.execute("CREATE TABLE IF NOT EXISTS Binabilgileri (Bina Numarası,Bölge,Değeri,Metrekare,OdaSayısıBanyo)")
    im.execute("INSERT INTO Binabilgileri Values (?,?,?,?,?)",veriler) 
    vt.commit()
    return veriler,Bina_bilgisi         
while(True):
    x=0
    print("""
          Sisteme hoş geldiniz  
          1.Admin girişi için 1'i tıklayınız
          2.Misajir kullanıcı için ve yapınız değerini öğrenmek için 2'ye  tıklayınız
          3.Kullanıcı girişi için 3"e tıklayınız
          4.Şifreyi unuttum""")
    secim=int(input())
    if(secim==1):
        kullanici_adi=input("kullancı adinizi giriniz")
        if kullanici_adi in admin:
            for i in range(len(admin_sfr)):
                if kullanici_adi in admin[i-1]:
                    giris=admin_giriş(x,i)
                    if(giris=="1"):
                        print("""
                              1.Kullanıcı Listesini ve şifrelerini görüntülemek için 1 e tıklayanız
                              2.Kullanıcı kaldırmak için 2'e tıklayınız
                              """)
                        kullanici_i=input()
                        if(kullanici_i=="1"):
                            print(kullanıcı_sfr)
                        elif(kullanici_i=="2"):
                            kullanici_silme=input("Sileceginiz kullanicinin ismini giriniz")
                            kullanıcılar.remove(kullanici_silme)
                            print("Kullanici kaldırılmıştır Sistemin başına geri dönüyorsunuz")
                        else:
                            print("yanlış girdiniz")
                    elif(giris=="2"):
                        print(misafir_tc.keys())
                    elif(giris=="3"):
                        vt=sqlite3.connect("Bina_tablosu.db")
                        im=vt.cursor()
                        im.execute("SELECT *FROM binabilgileri")
                        Bina_Verileri=im.fetchall()                     
                        print(Bina_Verileri)                                          
                    elif(giris=="4"):
                        veri = pd.read_csv("Kitap3.csv", sep=';',encoding='ISO-8859-1')
                        print(veri)
                else:
                    continue
        else:
            print("yanlis girdiniz")
    elif(secim==2):
        print("misafir girişine hoş geldiniz")
        while(True):
            tc=input("tc'nizi giriniz ")
            if(12==len(tc)):
                break
            else:
                print("""
                      tc 12 karakterli olmalıdır
                      tekrar deneyiniz""")
        isim=input("isminizi giriniz")
        misafir_tc.setdefault(isim,tc)
        print("""
               1.Evinizin fiyatı hakkında bilgi almak için 1'i tıklayınız
               2.Evinize neler yapabileceğinize bakmak için 2'i tıklayınız
               """)
        secim3=input()
        if(secim3=="1"):
            secim2=int(input("""Evinizin dayanıklılık durumunu giriniz
                     1.Dayanıklı ise 1 i tıklayınız 
                     2.Dayanıksız ise 2 i tıklayınız
                     3.Orta dayanıklı ise 3 ü tıklayınız"""))  
            while(x!=1):
                if(secim2==1):
                    bolge=input("evinizin hangi bölgede olduğunuzu giriniz")
                    if bolge.lower() in bolge_katsayıları.keys():
                        m2=int(input("evin metre karesini giriniz"))
                        fiyat=m2*bolge_katsayıları[bolge]+500000
                        print("evinizi en fazla bu kadara satabilirsiniz {}".format(fiyat))
                        break
                    else:
                        print("Böyle bölge yoktur")
                        x=int(input("çıkmak için 1 e tıklayınız"))
                elif(secim2==2):
                    bolge=input("evinizin hangi bölgede olduğunuzu giriniz")
                    if bolge.lower() in bolge_katsayıları.keys():
                        m2=int(input("evin metre karesini giriniz"))
                        fiyat=m2*bolge_katsayıları[bolge]+200000
                        print("evinizi en fazla bu kadara satabilirsiniz {}".format(fiyat))
                        break
                    else:
                        print("Böyle bölge yoktur")
                        x=int(input("çıkmak için 1 e tıklayınız"))
                elif(secim2==3):
                    bolge=input("evinizin hangi bölgede olduğunuzu giriniz")
                    if bolge.lower() in bolge_katsayıları.keys():
                        m2=int(input("evin metre karesini giriniz"))
                        fiyat=m2*bolge_katsayıları[bolge]
                        print("evinizi satamassınız ama bu kadar fiyat alabilirsiniz {}".format(fiyat))
                        break
                    else:
                        print("Böyle bölge yoktur")
                        x=int(input("çıkmak için 1 e tıklayınız"))
        elif(secim3=="2"):
            secim2=int(input("""Evinizin dayanıklılık durumunu giriniz
                     1.Dayanıklı ise 1 i tıklayınız 
                     2.Dayanıksız ise 2 i tıklayınız
                     3.Orta dayanıklı ise 3 ü tıklayınız"""))
            if(secim2==1):
                print("sadece satış yapabilirsiniz")
            elif(secim2==2):
                print("evinizin değerini alabilirsiniz yada eviniz yeniden yapılıp size belli bir ücret karşılığı geri verilir")
            elif(secim2==3):
                print("evinizi satabilirsiniz yada eviniz yeniden yapılıp size belli bir ücret karşılığı geri verilir")             
            else:
                print("Hatalı seçim")
    elif(secim==3):
        while(T!=0):
            x=0
            kullanici_adi2=input("kullanici adinizi giriniz")
            karakter_uzunlugu=len(kullanıcılar)   
            for i in range(karakter_uzunlugu):
                if kullanici_adi2 in kullanıcılar[i-1]:
                    while(x<3):
                        sifre=input("sifrenizi giriniz")
                        if(sifre==kullanıcı_sfr[kullanıcılar[i-1]]):                         
                            print("hoş geldiniz",kullanıcılar[i-1])
                            print("""
                                  1.Bina bilgilerini girişi için 1'i
                                  2.Bina kararı için 2'i tıklayınız'
                                  """)
                            kullanci_secimi=input()
                            if(kullanci_secimi=="1"):  
                                x=3
                                Bina_bilgileri_girisi() 
                            elif(kullanci_secimi=="2"):
                                print("Bilgilendirme yapılacaktır")                               
                                x=3    
                            else:
                                x=3
                                print("hatalı seçim")
                            karakter_uzunlugu=karakter_uzunlugu-1
                            break
                        else:
                            print("""şifreyi yanlış girdiniz
                                  eğer şifrenizi unuttuysanız ana menüye dönüp şifreyi unuttum seçeğine tıklayınız""")
                            x+=1
                            print("son",3-x,"hakkınız kaldı")
                elif((i+1)==karakter_uzunlugu):
                    print("""
 Kullanıcı adınız yanlıştır tekrar kullanıcı adını girmek istiyorsanız 1 e basınız çıkmak için herhangi bir tuşa basınız""")
                    hatalı_kullanici=input()
                    if(hatalı_kullanici=="1"):
                        continue
                    else:
                        T=0
                else:
                    continue
    else:
        print("""kurtarma seçenekleri 
              1.Güvenlik sorusu ile şifre yenilemek için 1'i tıklayınız
              2.Telefona kod ile şifre yenilemek için 2'i tıklayınız
              3.Kurtarma epostasıyla değiştirmke için 3'ü tıklayınız""")
    
                         
    
            

          
          

