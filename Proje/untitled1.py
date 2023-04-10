i=3
while(i!=0):
    giris=input("""Üyeliğiniz var mı? varsa "evet" yoksa "hayır" yazın""")
    if(giris=="evet"):
        print("lobiye yönlendirliyosunuz")
    elif(giris=="hayır"):
        giris2=input("""üye olmak istiyorsanız "e"yi çıkmak için hergangi bir tuşu tuşlayınız""")
        if(giris2=="e"):
            while(True):
                Kullanici_Adi=input("Kullanıcı adı belirleyiniz en fazla 9 karakter olabilir")
                if(9<len(Kullanici_Adi)):
                    print("belirli olan karakter sayısından fazla karakter içeriyor tekrar deneyiniz")
                else:
                    sifre=input("şifre belirleyiniz")
                break
        else:
            i=0
    print("Lobiye hoş geldiniz")
    while(True):
        Kullanici_Adi2=input("kullanıcı adınızı giriniz")
        if(Kullanici_Adi==Kullanici_Adi2):
            print("hoş geldiniz",Kullanici_Adi2)
        while(True):
            sifre2=input("şifrenizi giriniz")
            if(sifre==sifre2):
                print("giriş başarılı")
                break
            else:
                print("şifreniz hatalıdır bu kadar hakkınız kaldı",i)
                i-=1
                numara=input("""şifrenizi unuttuyasınız "1" e tekrar denemek için herhangi tuşa  basınız""")
                if(i==0):
                    print("Tekrar başa döndürülüyosunuz")
                if(numara=="1"):
                    print("telefonuza mesaj gelecektir")
                    break
                else:
                    break
        else:
            print("yanlış girdiniz tekrar deneyiniz")
            break
          

