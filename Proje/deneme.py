import sqlite3
veriler=[]
Bina_bilgisi=[]
sorular=["bina numarasını giriniz","binanızın bölgesini giriniz","Binanızın değerini giriniz ","Binanızın metrekaresini giriniz","Binanızın kaç +1 olduğunu giriniz"]
vt=sqlite3.connect("Bina_tablosu.db")
im=vt.cursor()
for i in range(5):
    print(sorular[i-1])
    deger=input()
    Bina_bilgisi.append(deger)
veriler.extend(tuple(Bina_bilgisi))
im.execute("CREATE TABLE IF NOT EXISTS Binabilgileri (Bina Numarası,Bölge,Değeri,Metrekare,OdaSayısıBanyo)")
im.execute("INSERT INTO Binabilgileri Values (?,?,?,?,?)",veriler)
im.execute("SElECT *From Binabilgileri")
bilgiler=im.fetchall()#Bütün veriyi bir anda almak için kullanılı
tek_bilgi=im.fetchone()#tek veriyi almak için kullanılır
istek_bilgi=im.fetmany()#ne kadar alacağınızı seçmek için
print(bilgiler)
vt.commit()
vt.close()