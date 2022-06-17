import webbrowser
from PIL import Image

class Fransiyum():

   def __init__(self, ad):#Baslangıç menüsü fonksiyonu oluşturduk.
      self.ad = ad
      self.calisma = True #Kod satırlarını tekrardan çalıştırmak için while döngüsüne bağladık.

   def baslangic(self):       
      secim = self.modsecim()
      if secim==1:
        self.elementler()
      if secim==2:
        self.resimler()
      if secim==3:
        self.karisimlar()
      if secim==4:
        self.asit_bazlar()
      if secim==5:
        self.kahramanlar()
        

   def modsecim(self):
      secim = int(input("\n****{}'ye HOŞ GELDİNİZ***** \n#Elementler için -->1 \n#Element resimleri için -->2 \n#Karışımlar için -->3 \n#Asit ve Bazlar için -->4 \n#Kahramanlar-->5 \n#Mod seçiniz:".format(self.ad)))
      while  secim < 1 or secim > 5: #olası tercihler dışında yapılacak tercihler için uyarı ve kaçış noktası planladık.
         secim = int(input("Lütfen 1 - 5 arasında belirtilen seçeneklerden birini giriniz!"))
         print("Lütfen Sayı Değeri Giriniz!")
      return secim   
      
   
     
   def elementler(self):
      x=int(input("1-118 arasında atom numarası giriniz:"))
      while x<1 or x>118: #Bir kaçış noktası ekledik yanlış girilen değeri tekrar girilmesi için.
        x=int(input("Lütfen 1-118 arasında atom numarası giriniz:"))
      print("[Element kütüphanesi]")
      f0=open("element.txt","r")#yedi tane elementsel bilgi içeren metni open komutu ile açıp "read"modu ile okuma yapmayı sağladık
      f1=open("Semboller.txt","r")
      f2=open("tür.txt","r")
      f3=open("grupadı.txt","r")
      f4=open("oda koşullarındaki halleri .txt.txt","r")
      f5=open("erime noktaları .txt.txt","r")
      f6=open("kaşif.txt","r")
      list1=list(f0)
      list2=list(f1)#metin dosyalarındaki bilgileri listelemeye giderek kullanım kolaylığı elde etmek istedik
      list3=list(f2)
      list4=list(f3)
      list5=list(f4)
      list6=list(f5)
      list7=list(f6)
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

   def resimler(self):
      x=str(input("1-118 arasından bir sayı giriniz: "))
      while x<1 or x>118:
       x=int(input("Lütfen 1-118 arasında atom numarası giriniz:"))
      print("[Resim kütüphanesi]")#resimler için pillow kütüphanesi kullandık 
      resim =""+ x +".jpg"#sayıları resimler ile eşleştırdık girilen sayıyı atom numarası gibi değerlendirebiliriz
      img = Image.open(resim)#resimleri açmak için kullandığımız komut satırı 
      img.show()

   def karisimlar(self):
       list=["Amonyak(1)","Karbonat(2)","Bakır(II)sülfat(3)","Sülfürik asit(4)","Sodyum bikarbonat(5)","Asetik asit(6)","Sodyum hidroksit(7)"," Hidroklorik asit(8)","Nitrik asit(9)","Kalsiyum karbonat(10)" ]
       print(list)
       a=int(input("Bileşik seçiniz:"))
       while a<1 or a>10 :
        a=int(input("Lütfen 1-10 arasında sayı giriniz:"))
       if a==1:
           print("           Amonyak(NH3)")
           print(" ")
           print("   Amonyak, formülü NH3 olan; azot atomu ve hidrojen atomundan oluşan renksiz, keskin ve hoş olmayan kokuya sahip bir gaz bileşiğidir. OH- iyonu içermediği halde suda zayıf baz özelliği gösterir. Bir amonyak molekülü, bir azot ve üç hidrojen atomundan oluşur.")
           print(" ")
           print("           Günlük Hayatta Kullanımı")
           print(" ")
           print("   Amonyak, gübre, ilaç, boya, parfüm gibi maddelerin sentezlenmesinde ilk aşamada kullanılmaktadır. Amonyak canlılar için zehirli bir maddedir, kullanılırken dikkat edilmesi gerekir. Piyasada amonyak adı altında satılan maddeler amonyağın sulu çözeltisi olan amonyum hidroksittir.")
           h=str(input("Amonyak deneyini açmak ister misiniz? (evet/hayır):"))
           if h=="evet":
              webbrowser.open("https://www.youtube.com/watch?v=rqiKVWr-1uk")
           if h=="hayır":
              print("\nNasıl isterseniz efendim :)")

       if a==2 :
            print("           Karbonat(CO3)")
            print(" ")
            print("   Karbonat, kimyada karbonik asitin bir tuzudur. Karbonat iyonu CO32- varlığında nitelendirilir. Aynı zamanda ismi karbonik asitin esteri manasına da gelebilir.Jeoloji ve mineralojide karbonat terimi hem karbonat minerallerine, hem de karbonat taşlarına tekabül eder ve her ikisi de CO32- şeklinde ifade edilir.")
            print(" ")
            print("            Günlük Hayatta Kullanımı")
            print(" ")
            print("   Karbonat, hamur işi tariflerinin vazgeçilmezi olarak bilinir,Karbonat aynı zamanda iyi bir diş temizleyicidir. Dişlerde çay, kahve ve sigaradan dolayı oluşan sarı lekelerin temizlenmesinde yardımcı olur.Karbonat, içinde barındırdığı anti bakteriyel özelliği sayesinde yer yüzeylerinin temizliği ve hijyeninde kullanılabilir. Etkin bir mikrop öldürücüdür aynı zamanda böcek ve zararlı haşaratı da kokusu sayesinde bulunduğunuz mekanlardan uzak tutacaktır.tekstil ürünlerinizde oluşacak lekelerin temizliği için karbonat tercih edebilirsiniz.")
            h=str(input("Karbonat hakkında bilgi içeren video için [bilgi], Karbonat ve sirke deneyi için [deney], Açmak istemiyorsanız [geç] yazınız:"))
            if h=="deney":
              webbrowser.open("https://www.youtube.com/watch?v=lmXP9YPYrWE")
            if h=="bilgi":
              webbrowser.open("https://www.youtube.com/watch?v=RUa43k0GUZs")
            if h=="geç":
              print("\nNasıl isterseniz :)")

       if a==3:
          print("           Bakır(II)sülfat(CuSO4)")
          print(" ")
          print("   Küprik sülfat ya da bakır sülfat olarak da denilen Bakır(II) sülfat, kimyasal formülü CuSO4 olan bir kimyasal bileşiktir. Bu tuzun hidrasyon derecelerine bağlı olarak bir dizi farklı bileşikleri mevcuttur. Susuz formu soluk yeşil ya da grimsi beyaz bir toz olmasına karşın en çok bilinen pentahidrat (CuSO4•5H2O) formu, parlak mavi renktedir. Çok az miktardaki CuSO4•5H2O çevreye çok zehirlidir, gözleri ve cildi tahriş eder ve yutulduğunda zararlı da olabilir. Oktahedral moleküler geometriye ve paramanyetik özelliğe sahip olan bakır(II) sülfat ekzotermik olarak suda çözünürek [Cu(H2O)6]2+ kompleksini oluşturur. Bakır(II) sülfat mavi vitriyol, göztaşı ve göktaşı olarak da bilinmektedir.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("    Bakır(II) sülfat bağlardaki ve meyve bahçelerindeki mantar hastalıkları ile mücadele amacıyla zirai ilaçların kullanılmasında etkin maddedir. Su borularının işgalci sucul bitkilerin köklerine karşı herbisit olarak bakır sülfat kullanılır. Yosun giderici şeklinde yüzme havuzlarında temizleyici olarak kullanılır. Seyreltik şeklindeki sülfat çözeltisi akvaryumda yaşayan balıklar parazit enfeksiyonları tedavisinde kullanılır ve akvaryumlarda bulunan salyangozları öldürmek için de bakır sülfat çözeltisi kullanılabilir.")
          h=str(input("Bakır(II)sülfat deneyini açmak ister misiniz? (evet/hayır):"))
          if h=="evet":
            webbrowser.open("https://www.youtube.com/watch?v=mdtbJ-AI8JI")
          if h=="hayır":
            print("\nNasıl isterseniz efendim :)")
          
       if a==4:
          print("           Sülfürik asit(H2SO4)")
          print(" ")
          print("   Sülfürik(VI) asit ya da halk arasında bilinen ismi ile zaç yağı, H2SO4, güçlü bir mineral asididir. Olası kaşifi 8. yüzyıl simyacısı Cabir bin Hayyan tarafından yenime uğratıcı, renksiz ve yoğunluğu yüksek sıvı olarak tanımlanmıştır. Suda her konsantrasyonda çözünebilir. Büyük ölçüde korozif oluşu, güçlü asidik yapısından ve dehidrasyon özelliğinden kaynaklanmaktadır.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("    Sülfürik asit çeşitli derişimleri durumunda gübre, pigment, boyar madde, patlayıcı madde, ilaçlama, inorganik tuz ve petrol arıtım ile metalurji işlemlerinde kullanılmaktadır. Bunların yanı sıra çeşitli pillerin yapımlarında da sülfürik asitten yararlanıldığını görebilmek mümkündür. Bu asidin halk arasında akü asidi olarak bilindiğini söyleyebiliriz.")
          h=str(input("Sülfürik asit ile şeker deneyini açmak ister misiniz? (evet/hayır):"))
          if h=="evet":
            webbrowser.open("https://www.youtube.com/watch?v=iX_X-SC_MY0")
          if h=="hayır":
            print("\nNasıl isterseniz efendim :)")
           
       if a==5:
          print("           Sodyum bikarbonat(NaHCO3)")
          print(" ")
          print("   Sodyum bikarbonat ya da soda kimyasal formulü NaHCO3 olan bir kimyasal bileşiktir. Kabartma tozu olarak da bilinir. Sodyum tuzlarından birisidir. Antiasit özelliği vardır. Kabartma tozu olarak da kullanılır. Suda çözünür. Beyaz katı kristal tozdur. Sodyum karbonat'ı andıran hafif alkali tadı vardır. Salin solüsyonu bileşiminde de kullanılır.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("   Sodyum bikarbonat, halk arasında sıklıkla hamur kabartma tozu olarak bilindiği için, bu şekilde kullanımı yaygındır. Ancak bunun yanı sıra yanmış tepsilerin ve tencerelerin rahat bir şekilde temizlenebilmesi için iyi bir çözümdür ayrıca demliklerin içerisindeki kalıntıların, termoslardaki ve vazolardaki kalıntıların temizlenmesinde de kullanılır.Ayrıca ağız kokusu olanların da derdine çare olabilmektedir. İstenmeyen kokuları önleyen bu madde, lavabo kokularının önlenmesi, ayakkabı kokularının giderilmesi, buzdolabı kokularının giderilmesi için de kullanılabilir.Böcek sokmaları sonrasında, böcek ısırığının olduğu yere sodyum bikarbonatlı su ile uygulama yapıldığında ısırılan bölgedeki kaşıntıyı engellemektedir.Güneş yanıklarında sodyum bikarbonatlı su yanan bölgeye anında uygulanırsa, yanık bölgedeki ağrıyı hafifletmektedir.")
          h=str(input("Sodyum bikarbonat deneyini izlemek ister m-isiniz? (evet/hayır):"))
          if h=="evet":
            webbrowser.open("https://www.youtube.com/watch?v=cAjP5JR11AE")
          if h=="hayır":
            print("\nNasıl isterseniz efendim :)")
       if a==6:
          print("           Asetik asit(CH3COOH)")
          print(" ")
          print("   Asetik asit veya etanoik asit CH3COOH formüllü bir organik asittir, sirkeye ekşi tadını ve keskin kokusunu vermesiyle bilinir. Karboksilik asitlerin en küçüklerindendir (en küçük olan formik asittir). Doğada karbonhidratların yükseltgenmesiyle oluşur. Sanayide asetik asit hem biyolojik yolla hem de sentetik yolla imal edilir. Tuz ve esterine asetat denir. Suda tamamen çözünür.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("   Sirke imalatında kullanılır. Ayrıca turşu yapımında mikroorganizmaların oluşmasını engelleyerek sebzelerin bozulmasını engeller. Sanayide çoğu kimyasalın üretiminde hammadde olarak kullanılır. Özellikle vinil asetat üretiminde kullanılır, bundan elde edilen polivinil asetat tahta tutkalı olarak kullanılır.Çözücü olarak sanayide kullanılır. Örneğin, PET plastiklerin üretiminde kullanılan tereftalik asitin üretiminde çözücü olarak kullanılır. Bu kullanım asetik asitin tüm kullanımı içerisinde %5-10 oranındadır. 4. Gıda sektöründe tampon olarak kullanılır. Asitlik sağlayıcı, koruyucu, lezzet verici olarak kullanılır.")
          h=str(input("Asetil asit deneyini açmak ister misiniz? (evet/hayır):"))
          if h=="evet":
            h=str(input("\nSodyum bikarbonata baktıysanız aynı deneyi izleyeceksiniz. \nEmin misiniz?\n"))
            if h=="eminim" or "evet" or "evet eminim":
               webbrowser.open("https://www.youtube.com/watch?v=cAjP5JR11AE")
          if h=="hayır" or "istemiyorum":
            print("\nNasıl isterseniz :)")
          
       if a==7:
          print("            Sodyum hidroksit(NaOH)")
          print(" ")
          print("   Kostik ve kostik soda olarak da bilinen sodyum hidroksit (kostik soda veya sud kostik de denir), NaOH formülüne sahip bir inorganik bileşiktir. Sodyum katyonları Na+ ve hidroksit anyonları OH- içeren beyaz renkli katı bir iyonik bileşiktir.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("   En kuvvetli baz olan kostiğin kullanım alanı çok geniştir. Tekstil endüstrisinde kostik kullanılır. Sabun ve temizlik malzemeleri imalatında kullanımı vardır. Özellikle sıvı ve katı sabun yapımında. Petrol rafinelerinde kostik kullanılır. Yapay ipek yapımında kostik kullanılır. Kağıt hamuru ve kağıt üretiminde kostik kullanılır. PH yükseltilmesi gereken yerlerde kostik kullanılır. Arıtmalarda asidik ortamın nötralizasyonunda ve çöktürme amaçlı kostik kullanılır. Boya kimyasalları sektöründe kostik kullanılır. Zeytinin işlemesinde kostik kullanılır. Saf su üretiminde (İyon Değiştirici Reçinelerin Rejenerasyonunda) ve su arıtma da kostik kullanılır. Patlayıcı maddelerin üretiminde kostik kullanılır. Tarımsal kimyasaalların üretilmesinde kostik kullanılır. İlaç endüstrisinde kostik kullanılır.")
          h=str(input("Sodyum hidroksit deneyini açmak ister misiniz? (evet/hayır):"))
          if h=="evet":
            h=str(input("Sodyum bikarbonat ve Asetik asit ile aynı deneyde yer alıyor izlemek istediğinize emin misiniz?\n"))
            if h=="evet" or "eminim" or "evet eminim" or "açılsın" :
               webbrowser.open("https://www.youtube.com/watch?v=cAjP5JR11AE")
            if h=="hayır":
              print("\nNasıl isterseniz efendim :)")
          if h=="hayır" or "istemiyorum":
            print("\nNasıl isterseniz efendim :)")
       if a==8:
          print("            Hidroklorik asit(HCl)")
          print(" ")
          print("    Hidroklorik asit, hidrojen ve klor elementlerinden oluşan, oda sıcaklığı ve normal basınçta gaz hâlinde olan hidrojen klorürün sulu çözeltisine verilen ad. Halk arasında tuz ruhu olarak da bilinir. 9. yüzyılda simyacı Cabir bin Hayyan tarafından keşfedildi ve sonrasında simya alanında kullanıldı.Günümüzde PVC'den demir-çeliğe, organik madde üretiminden gıda sektörüne kadar hemen hemen tüm alanlarda hidroklorik asit kullanılmaktadır.Hidroklorik asit, sağladığı kolaylıkların yanında, zehirli bir maddedir ve insan dokuları başta olmak üzere çoğu yüzeye büyük tahribat verir. Bu nedenle bu asit ile çalışılırken güvenlik önlemleri en üst düzeyde tutulmalıdır.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("     Sanayide petrol, reçine rejenerasyonu, kağıt, ilaç, boya, kimya, tekstil, metal klorürü üretimi gibi alanlarda kullanılmaktadır. Çeliğin dekapajı: Hidroklorik asit çeliğin temizlenmesi için yapılan dekapaj işleminde sıkça kullanılmaktadır. PVC maddesi için üretilen Vinil klorit gibi organik madde üretiminde hidroklorik asit kullanılmaktadır. Hidroklorik asitten elde edilen fosgen 1. Dünya Savaşında kimyasal silah olarak kullanılan bir organik maddedir.")
          h=str(input("Hidroklorik asit deneyini açmak ister misiniz? (evet/hayır):"))
          if h=="evet":
            webbrowser.open("https://www.youtube.com/watch?v=fjYLI0G5IVw")
          if h=="hayır":
            print("\nNasıl isterseniz efendim :)")
       if a==9:
          print("            Nitrik asit(HNO3)")
          print(" ")
          print("    Nitrik asit HNO3 kimyasal formülüne sahip oldukça aşındırıcı bir inorganik asittir. Kezzap olarak da adlandırılır.Saf bileşik renksizdir. Ancak uzun süre bekleyen eski asitler azot oksitleri ve suya ayrışması nedeniyle sarı renge dönebilme özelliğindedirler. Piyasada bulunan nitrik asitlerin çoğu % 68'lik bir konsantrasyona sahiptir. Çözelti, % 86'dan fazla HNO3 içerdiğinde, dumanlı nitrik asit olarak adlandırılır. Mevcut azot dioksit miktarına bağlı olarak, dumanlı nitrik asit ayrıca %86’nın üzerindeki konsantrasyonlarda kırmızı dumanlı nitrik asit veya %95’in üzerindeki konsantrasyonlarda beyaz dumanlı nitrik asit olarak tanımlanır. Nitrik asit, tipik olarak bir organik moleküle nitro grubunun eklenmesi olan nitrolama için kullanılan ana reaksiyon maddesidir. Ortaya çıkan bazı nitro bileşikleri şok ve termik olarak hassas patlayıcı maddeler olsa da, bazıları mühimmat ve yıkımlarda kullanılacak kadar kararlıdır. Diğerleri ise daha kararlıdır ve mürekkep ve boyar maddelerde pigment olarak kullanılır. Nitrik asit, ayrıca kuvvetli bir oksitleyici madde olarak da yaygın şekilde kullanılmaktadır.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("   Gübre üretiminde kullanılır. Metal sanayisinde metallerin saflaştırılmasında kullanılır. Metallerin dağlanması işlemi sırasında kullanılır. Patlayıcı maddelerin üretiminde kullanılır. PH indirgenmesi gereken su arıtması gibi yerlerde kullanılır. Boya kimyasalları sektöründe kullanılır. Dinamit üretiminde kullanılır. Gümüş nitrat üretilmesi için kullanılır. Elektro polisaj işlemlerinde kullanılmaktadır.")
          h=str(input("Nitrik asit deneyini açmak ister misiniz? (evet/hayır):"))
          if h=="evet":
            webbrowser.open("https://www.youtube.com/watch?v=LBrje9A1mHg")
          if h=="hayır":
            print("\nNasıl isterseniz efendim :)")
       if a==10:
          print("            Kalsiyum karbonat(CaCO3)")
          print(" ")
          print("    Kalsiyum karbonat, halk arasında kireç taşı olarak bilinen bir tür kimyasal bileşiktir. Bileşik formülü CaCO3 şeklindedir. Bu bileşik doğada en fazla eski kayaçlarda ve deniz kabuklarında bulunur. Kalsiyum karbonat, antiasitlerin bir üyesi olsa da, fazlası biyolojik olarak zararlıdır. Kalsiyum karbonatın doğada bulunduğu kayaçlar içinde en yoğun bilinenleri, aragonit, kalsit, vaterit, tebeşir, kireç taşı, mermer ve travertendir. Bir kayaç üzerinde kalsiyum karbonatın varlığının tespit edilmesi için hidroklorik asit veya sülfürik asit kullanılır.")
          print(" ")
          print("            Günlük Hayatta Kullanımı")
          print(" ")
          print("    Kalsiyum karbonat, sanayide, mermer, tebeşir ve kireç taşı gibi farklı malzemelerin üretiminde yoğun olarak kullanılır. Aynı şekilde boya malzemelerinin üretilmesinde yoğun olarak bu bileşikten yararlanılır. PVC üretiminde de kullanılan kalsiyum karbonat, seramik yapımında yararlanılan bir moleküldür. Tıp alanında,genellikle Böbrek fonksiyonunu kaybetmiş, kandaki fosforu idrar yolu ile atamayan kronik böbrek yetersizliği durumlarında besinlerdeki fosforu bağlamasında, fosfatlı bileşiklerin dengelenmesinde kullanılır. (phos-ex) Gıda alanında ise E170 adıyla katkı maddesi şeklinde ve soya sütünde kullanılır. Son yıllarda çevresel dengenin sağlanmasında kalsiyum karbonatın önemli bir yere sahip olduğu görülmüştür.")
      
   def asit_bazlar(self):
       h=str(input("Asitler ile ilgili bilgi için 'Asit' yazınız. Bazlar ile ilgili bilgi için 'Baz' yazınız. İstemiyorsanız 'Geç' yazınız.\n"))
       if h=="Asit" or "asit":
         webbrowser.open("https://tr.wikipedia.org/wiki/Asit")
       if h=="Baz" or "baz":
         webbrowser.open("https://tr.wikipedia.org/wiki/Baz")
       if h=="geç" or "Geç":
         print("\nTabi efendim.")
         x=int(input("\n1-14 arasında Ph değeri giriniz:"))
         f0=open("Asit_Baz.txt","r")
         list1=list(f0)
         x=int(input("1-14 arasında Ph değeri giriniz:"))
         x-=1
         while x<1 or x>14:
           x=int(input("Lütfen 1-14 arasında değer giriniz:"))#olası tercihler dışında yapılacak tercihler için uyarı ve kaçış noktası planladık
         n1=list1[x]
         print("İstediğiniz %s"%(n1))
 
  
   def kahramanlar(self):
    a=str(input("Press F to pay respects\n"))

    if a=="F" or "f":
      resim = "F.jpg"
      img=Image.open(resim)
      img.show()
      print("****TEŞEKKÜRLER****")#periyodik tablo için önemli isimleri print komutu ile yazdık
      print("Lavoisier\nJohann Döbereiner\nAlexandre Beguyer de Chancourtois\nJohn Newlands\nHenry Moseley\nGilen Siborg\nDimitri Mendeleyev  ve Lothar Meyer\nMarie curie\nElizabeth Ascheim")
      
    else:
      while a!="F" or a!="f":
        a=str(input("Press F to pay respects\n"))


Periyodik_Tablo = Fransiyum("FransiyumCruie") #Sınıfa bir değişken atadık.
while Periyodik_Tablo.calisma: #Sınıfı while döngüsüne sokarak sürekli çalışmasını sağladık.
  Periyodik_Tablo.baslangic()
