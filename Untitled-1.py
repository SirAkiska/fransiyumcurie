from PIL import Image
print("     *****FRANSİYUM CURİE HOŞ GELDİNİZ*****      ")
print("element bilgileri için -->1 \nelement resimleri için -->2 \ngünlük karışımlar için -->3 \nasit-baz için -->4 ")
a=int(input("Lütfen tercıhte bulununuz:"))
if a==1:
    print("[Element kütüphanesi]")
    f0=open("D:\GitHub/fransiyumcurie\dosyalar\element.txt","r")
    f1=open("D:\GitHub/fransiyumcurie\dosyalar\Semboller.txt","r")
    f2=open("D:\GitHub/fransiyumcurie\dosyalar/tür.txt","r")
    f3=open("D:\GitHub/fransiyumcurie\dosyalar\grupadı.txt","r")
    f4=open("D:\GitHub/fransiyumcurie\dosyalar\oda koşullarındaki halleri .txt.txt","r")
    f5=open("D:\GitHub/fransiyumcurie\dosyalar\erime noktaları .txt.txt","r")
    f6=open("D:\GitHub/fransiyumcurie\dosyalar\kaşif.txt","r")
    list1=list(f0)
    list2=list(f1)
    list3=list(f2)
    list4=list(f3)
    list5=list(f4)
    list6=list(f5)
    list7=list(f6)
    x=int(input("1-118 arasında atom numarası giriniz:"))
    x-=1
    c0=list1[x]
    c1=list2[x]
    c2=list3[x]
    c3=list4[x]
    c4=list5[x]
    c5=list6[x]
    c6=list7[x]
    print("\n*****verdiğiniz atom numarasınna göre*****\n")
    print("elementin adı-->%s"% (c0))
    print("elementin bilimsel gösterimi -->%s"%(c1))
    print("elemen türü -->%s"%(c2))
    print("elementin bulunduğu grubun adın -->%s"%(c3))
    print("elementin oda koşullarındaki hali -->%s"%(c4))
    print("elementin erime noktası -->%s"%(c5))
    print("elementin keşfi --> %s"%(c6))
if a==2:
    print("[Resim kütüphanesi]")
    x = str(input("Bir Sayi giriniz: "))
    resim = "D:\GitHub/fransiyumcurie/element resimleri/"+ x +".jpg"
    img = Image.open(resim)
    img.show()
if a==3:
<<<<<<< Updated upstream
    print("furkan")
=======
    list=["Amonyak(1)","Karbonat(2)"]
    print(list)
    g=int(input("Bileşik seçiniz:"))
    if g==1 :
        print("           Amonyak-NH3")
        print(" ")
        print("  "+"Amonyak, formülü NH3 olan; azot atomu ve hidrojen atomundan oluşan renksiz, keskin ve hoş olmayan kokuya sahip bir gaz bileşiğidir. OH- iyonu içermediği halde suda zayıf baz özelliği gösterir. Bir amonyak molekülü, bir azot ve üç hidrojen atomundan oluşur.")
        print(" ")
        print("           Günlük Hayatta Kullanımı")
        print(" ")
        print("  "+"Amonyak, gübre, ilaç, boya, parfüm gibi maddelerin sentezlenmesinde ilk aşamada kullanılmaktadır. Amonyak canlılar için zehirli bir maddedir, kullanılırken dikkat edilmesi gerekir. Piyasada amonyak adı altında satılan maddeler amonyağın sulu çözeltisi olan amonyum hidroksittir.")
    if g==2 :
        print("Karbonat")
        print(" ")
        print("  "+" Karbonat, kimyada karbonik asitin bir tuzudur. Karbonat iyonu CO32- varlığında nitelendirilir. Aynı zamanda ismi karbonik asitin esteri manasına da gelebilir.Jeoloji ve mineralojide karbonat terimi hem karbonat minerallerine, hem de karbonat taşlarına tekabül eder ve her ikisi de CO32- şeklinde ifade edilir.")
>>>>>>> Stashed changes
