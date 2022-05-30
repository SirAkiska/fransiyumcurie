from PIL import Image 
print("     *****FRANSİYUM CURİE HOŞ GELDİNİZ*****      ")#Bir başlangıç menüsü hazırlamak istedik
print("#Elementler için -->1 \n#Element resimleri için -->2 \n#Karışımlar için -->3 \n#Asit-baz için -->4\nKahramanlar-->5 ")#if komutu yardımı ile kullanım tercıhleri oluşturduk
a=int(input("Lütfen tercıhte bulununuz:"))
if a==1:
    print("[Element kütüphanesi]")
    f0=open("D:\GitHub/fransiyumcurie\dosyalar\element.txt","r")#yedi tane elementsel bilgi içeren metni open komutu ile açıp "read"modu ile okuma yapmayı sağladık
    f1=open("D:\GitHub/fransiyumcurie\dosyalar\Semboller.txt","r")
    f2=open("D:\GitHub/fransiyumcurie\dosyalar/tür.txt","r")
    f3=open("D:\GitHub/fransiyumcurie\dosyalar\grupadı.txt","r")
    f4=open("D:\GitHub/fransiyumcurie\dosyalar\oda koşullarındaki halleri .txt.txt","r")
    f5=open("D:\GitHub/fransiyumcurie\dosyalar\erime noktaları .txt.txt","r")
    f6=open("D:\GitHub/fransiyumcurie\dosyalar\kaşif.txt","r")
    list1=list(f0)
    list2=list(f1)#metin dosyalarındaki bilgileri listelemeye giderek kullanım kolaylığı elde etmek istedik
    list3=list(f2)
    list4=list(f3)
    list5=list(f4)
    list6=list(f5)
    list7=list(f6)
    x=int(input("1-118 arasında atom numarası giriniz:"))#standart periyodik tablonun 118 elementini değerlendirdik
    x-=1#metin doysayısının ilk endeksini sıfırdan bire almak için yapıldı
    c0=list1[x]#kulanacağimiz f format tarzı için bilinmeyenler belirledik
    c1=list2[x]
    c2=list3[x]
    c3=list4[x]
    c4=list5[x]
    c5=list6[x]
    c6=list7[x]
    print("\n*****verdiğiniz atom numarasınna göre*****\n")#istediğimiz çiktiları yazdırmak için kullanılan panel
    print("elementin adı-->%s"% (c0))
    print("elementin bilimsel gösterimi -->%s"%(c1))
    print("elemen türü -->%s"%(c2))
    print("elementin bulunduğu grubun adın -->%s"%(c3))
    print("elementin oda koşullarındaki hali -->%s"%(c4))
    print("elementin erime noktası -->%s"%(c5))
    print("elementin keşfi --> %s"%(c6))
if a==2:
    print("[Resim kütüphanesi]")#resimler için pillow kütüphanesi kullandık 
    x = str(input("Bir Sayi giriniz: "))
    resim = "D:\GitHub/fransiyumcurie/element resimleri/"+ x +".jpg"#sayıları resimler ile eşleştırdık girilen sayıyı atom numarası gibi değerlendirebiliriz
    img = Image.open(resim)#resimleri açmak için kullandığımız komut satırı 
    img.show() 
if a==4:
    f0=open("D:\GitHub/fransiyumcurie\Asit-Baz/Asit.txt.txt","r")
    list1=list(f0)
    x=int(input("1-118 arasında atom numarası giriniz:"))
    n1=list1[x]
    print("Asitiniz %s"%(n1))





if a==5:
    print("****TEŞEKKÜRLER****")#periyodik tablo için önemli isimleri print komutu ile yazdık
    print("Lavoisier\nJohann Döbereiner\nAlexandre Beguyer de Chancourtois\nJohn Newlands\nHenry Moseley\nGilen Siborg\n5Dimitri Mendeleyev  ve Lothar Meyer\nMarie curie\nElizabeth Ascheim")
if a>=6:
    print("Lütfen uygun bir tercihte bulunuz\n***Elementler için-->1\n***Resimler için-->2\n***Karışımlar için-->3\n***Asit-baz için-->4")#olası tercihler dışında yapılacak tercihler için uyarı ve kaçış noktası planladık
