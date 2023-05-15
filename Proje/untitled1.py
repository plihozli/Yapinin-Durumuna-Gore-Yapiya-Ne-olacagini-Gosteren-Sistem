admin=("Mehmet12","Neslihan51","Batuhan34")
admin_sfr={admin[0]:3124234,admin[1]:32432523,admin[2]:24234234}
misafir_tc={}
kullanıcılar=["ALi","Ayşe","Murat"]
kullanıcı_sfr={}
bolge_katsayıları={"pendik":300,"maltepe":500,"sultanbeyli":400,"kadıköy":600,"üsküdar":700}
while(True):
    x=0
    print("""Sisteme hoş geldiniz  
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
                    while(x<3):
                        sifre=input("şifrenizi giriniz")
                        if(sifre==str(admin_sfr[admin[i-1]])):
                            print("hoş geldiniz",admin[i-1])
                            print("""1.Kullanıcıların listesini görmek için 1'i tıklatınız
                                  2.Misafir kullunıcıların listesini görmek için 2'i yi tıklayınız
                                  3.Girilen binalara ne yapılcağını görmek için 3'e tıklayınız
                                  4.Toplam tutarı görmek için 4'ü tıklayınız
                                  5.Bölge katsayılarını değiştirmek için e tıklayınız""")
                        else:
                            print("""yanlis girdiniz 
                                  şifreyi unuttuysanız yetkili birine iletmeniz gerekecektir""")
                            x+=1
                            print("son",3-x,"hakkınız kaldı")
        else:
            print("yanlis girdiniz")
    elif(secim==2):
        print("misafir girişine hoş geldiniz")
        while(True):
            tc=int(input("tc'nizi giriniz "))
            if(13==len(tc)):
                break
            else:
                print("""tc 12 karakterli olmalıdır
                      tekrar deneyiniz""")
        isim=input("isminizi giriniz")
        misafir_tc.setdefault(isim,tc)
        print("""1.Evinizin fiyatı hakkında bilgi almak için 1'i tıklayınız
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
                if bolge in bolge_katsayıları.keys():
                    m2=input("evin metre karesini giriniz")
                    fiyat=m2*bolge_katsayıları[bolge]+500000
                    print("evinizi en fazla bu kadara satabilirsiniz",fiyat)
                    break
                else:
                    print("Böyle bölge yoktur")
                    x=int(input("çıkmak için 1 e tıklayınız"))
    elif(secim==3):
        while(True):
            kullanici_adi=input("kullanici adinizi giriniz")
            for i in range(len(kullanıcılar)):
                if kullanici_adi in kullanıcılar[i-1]:
                    while(x<3):
                        sifre=input("sifrenizi giriniz")
                        if(sifre==str(kullanıcı_sfr[kullanıcılar][i-1])):
                            print("hoş geldiniz",kullanıcılar[i-1])
                            print("""1.Aylık ücretiniz varsa  almak için 1'i
                                  2.Yerleşebileceğiniz yerlere bakmak için 2 yi
                                  3.Binanıza ne yapılması karar verildiğini öğrenmek için 3'ü tıklayınız""")
                        else:
                            print("""şifreyi yanlış girdiniz
                                  eğer şifrenizi unuttuysanız ana menüye dönüp şifreyi unuttum seçeğine tıklayınız""")
                            x+=1
                            print("son",3-x,"hakkınız kaldı")
                elif(i==len(kullanıcılar)):
                    print("hatalı giriş")
    else:
        print("""kurtarma seçenekleri 
              1.Güvenlik sorusu ile şifre yenilemek için 1'i tıklayınız
              2.Telefona kod ile şifre yenilemek için 2'i tıklayınız
              3.Kurtarma epostasıyla değiştirmke için 3'ü tıklayınız""")
          
          

