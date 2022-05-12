<<<<<<< Updated upstream
=======
from PIL import Image
print("*****FRANSİYUM CURİE HOŞ GELDİNİZ*****")
print("element bilgileri için -->1 \n element resimleri için -->2 \n günlük karışımlar için -->3 \n asit-baz için -->4 ")
a=int(input("Lütfen tercıhte bulununuz"))
if a==1:
    print("istediğiniz elementin atom numarasını giriniz")
    f0=open("D:\GitHub/fransiyumcurie\dosyalar/element.txt","r")
    f1=open("D:\GitHub/fransiyumcurie\dosyalar/sembol.tx t","r")
    f2=open("D:\GitHub/fransiyumcurie/dosyalar/tür","r")
    f3=open("D:\GitHub/fransiyumcurie\dosyalar/grupadı","r")
    f4=open("D:\GitHub/fransiyumcurie\dosyalar/hal","r")
    f5=open("D:\GitHub/fransiyumcurie\dosyalar/erime","r")
    list1=list(f0)
    list2=list(f1)
    list3=list(f2)
    list4=list(f3)
    list5=list(f4)
    list6=list(f5)
    x=int(input("1-118 arasında atom numarası giriniz"))
    x-=1
    c0=list1[x]
    c1=list2[x]
    c2=list3[x]
    c3=list4[x]
    c4=list5[x]
    c5=list6[x]
    print("verdiğiniz atom numarasınna göre")
    print("elementin adı-->%s"%(c0))
    print("elementin bilimsel gösterimi -->%s"%(c1))
    print("elemen türü -->%s"%(c2))
    print("elementin bulunduğu grubun adın -->%s"%(c3))
    print("elementin oda koşullarındaki hali -->%s"%(c4))
    print("elementin erime noktası -->%s"%(c5))


>>>>>>> Stashed changes
