
ASGARI_UCRET_2020=2324.70
top_konut_satis_say=0
top_konut_kira_say=0
top_isyeri_satis_say=0
top_isyeri_kira_say=0
top_arsa_satis_say=0
top_arsa_kira_say=0
max_satis_genel=0
max_satis_genel_ad_soyad=""
max_satis_genel_emlak_tipi=""
max_satis_genel_emlak_tipi_uzun=""
max_kira_genel=0
max_kira_genel_ad_soyad=""
asgari_ucret_ustu_kira=0
top_max_satin_bedel=0 #top max satis bedeli
max_satin_say=0
max_s_say_ad_soyad = ""
max_s_say_toplam_bedel = 0
kota_dolu_calisan_say=0
primi_maasindan_yuksek=0
min10_veya_min25000_kira=0
prim_max=0
prim_max_ad_soyad =""
prim_max_maas = 0
prim_max_aylik_toplam_ucret = 0
prim_min = float("inf")
prim_min_ad_soyad = ""
prim_min_maas = 0
prim_min_aylik_toplam_ucret = 0
tum_calisanlara_ode=0
top_emlak_komisyonu=0
max_satin_bedel=0
max_s_b_ad_soyad = ""
max_s_b_satilan_emlak_say = 0
top_konut_satis_bedel=0
top_isyeri_satis_bedel=0
top_arsa_satis_bedel=0
satis_yapamayan=0

calisan_say=int(input("Acenteye bağlı emlak danışmanı sayısı:"))
while calisan_say<=0:
    print("Çalışan sayısı 0'dan büyük olmalı, lütfen tekrar deneyiniz.")
    calisan_say = int(input("Acenteye bağlı emlak danışmanı sayısı:"))

for i in range(calisan_say):
    min25000_kira=0
    satin = 0
    kira = 0
    konut_kira = 0 #kiralanan konut sayısı
    toplam_emlak_say = 0 # bir çalışan için kiralanan ve satılan emlakların toplamını verir
    is_yeri_satin_top_bedel = 0 #işyeri tipi olarak satılan emlakların toplam bedelini tutacak
    konut_satin_top_bedel = 0 #konut tipi olarak satılan emlakların toplam bedelini tutacak
    arsa_satin_top_bedel = 0 #arsa tipi olarak satılan emlakların toplam bedelini tutacak
    konut_kira_bedel = 0 #kiralanan konutların toplam bedelini tutacak
    max_konut_kira_bedel = 0 # en yüksek bedelle kiralanan konut
    emlak_komisyonu=0
    kota_doldu = False
    ad_soyad=input("Adınız ve soyadınız:")

    maas=float(input("Maaşınız:"))
    while maas<ASGARI_UCRET_2020:
        print("Maaşınız asgari ücretten düşük olamaz, lütfen tekrar deneyiniz.")
        maas = float(input("Maaşınız"))

    kota=float(input("Kotanız:"))
    while kota<maas*10:
        print("Kotanız maaşınızın en az 10 katı kadar olmalıdır, lütfen tekrar deneyiniz.")
        kota = float(input("Kotanız:"))

    while True:
        emlak_tipi=input("Emlak tipi: Konut, İş yeri, Arsa (K/k/İ/i/A/a karakterleri)")
        while not(emlak_tipi=="k" or emlak_tipi=="K" or emlak_tipi=="i" or emlak_tipi=="İ" or emlak_tipi=="a" or emlak_tipi=="A"):
            print("Hatalı emlak tipi kısaltması, lütfen tekrar giriniz.")
            emlak_tipi = input("Emlak tipi: Konut, İş yeri, Arsa (K/k/İ/i/A/a karakterleri)")

        islem_turu=input("İşlem türü: Satış, Kiralama (S/s/K/k karakterleri)")
        while not (islem_turu=="s" or islem_turu=="S" or islem_turu=="k" or islem_turu=="K"):
            print("Hatalı işlem tipi kısaltması, lütfen tekrar giriniz.")
            islem_turu = input("İşlem türü: Satış, Kiralama (S/s/K/k karakterleri)")

        satis_kira_bedeli=float(input("Satış/kira bedeli (TL):"))
        while satis_kira_bedeli<=0:
            print("Hatalı satış/kira bedeli, lütfen tekrar giriniz.")
            satis_kira_bedeli = float(input("Satış/kira bedeli (TL):"))

        baska_emlak=input("Sattığınız ya da kiraladığınız başka emlak var mı?(e/E/h/H karakterleri)")
        while not(baska_emlak=="e" or baska_emlak=="E" or baska_emlak=="h" or baska_emlak=="H"):
            print("Hatalı giriş yaptınız, lütfen tekrar giriniz.")
            baska_emlak = input("Sattığınız ya da kiraladığınız başka emlak var mı?(e/E/h/H karakterleri)")

        if islem_turu=="s" or islem_turu=="S": #satış işlem türü
            satin+=1 #satılan emlak adedi
            emlak_komisyonu+=satis_kira_bedeli*0.04 # emlak komisyonu satılan emlağın %4'ü kadardır
            if emlak_tipi == "k" or emlak_tipi == "K":
                konut_satin_top_bedel += satis_kira_bedeli
                top_konut_satis_say+=1

            elif emlak_tipi == "i" or emlak_tipi == "İ":
                is_yeri_satin_top_bedel += satis_kira_bedeli
                top_isyeri_satis_say+=1

            else:
                arsa_satin_top_bedel += satis_kira_bedeli
                top_arsa_satis_say+=1

            if satis_kira_bedeli>max_satis_genel: #o ay en yüksek bedelle satılan emlağın bedeli
                max_satis_genel=satis_kira_bedeli
                max_satis_genel_ad_soyad=ad_soyad
                max_satis_genel_emlak_tipi = emlak_tipi
                if max_satis_genel_emlak_tipi=="k" or max_satis_genel_emlak_tipi=="K":
                    max_satis_genel_emlak_tipi_uzun=="Konut"
                elif max_satis_genel_emlak_tipi=="i" or max_satis_genel_emlak_tipi=="İ":
                    max_satis_genel_emlak_tipi_uzun =="İş yeri"
                else:
                    max_satis_genel_emlak_tipi_uzun == "Arsa"


        else:# kira işlem türü
            kira+=1 #kiralanan emlak adedi
            emlak_komisyonu+=satis_kira_bedeli # emlak komisyonu kiralanan emlağın bir aylık kirası kadardır
            if satis_kira_bedeli>25000:
                min25000_kira+=1
                if min25000_kira==1:
                    min10_veya_min25000_kira+=1
            if emlak_tipi=="k" or emlak_tipi=="K":
                konut_kira_bedel+=satis_kira_bedeli
                konut_kira+=1
                if satis_kira_bedeli>max_konut_kira_bedel:
                    max_konut_kira_bedel=konut_kira_bedel

            if satis_kira_bedeli>ASGARI_UCRET_2020:
                asgari_ucret_ustu_kira+=1

            if satis_kira_bedeli>max_kira_genel:
                max_kira_genel=satis_kira_bedeli
                max_kira_genel_ad_soyad=ad_soyad

            if emlak_tipi == "k" or emlak_tipi == "K":
                top_konut_kira_say += 1

            elif emlak_tipi == "i" or emlak_tipi == "İ":
                top_isyeri_kira_say += 1

            else:
                top_arsa_kira_say += 1

        if baska_emlak=="h" or baska_emlak=="H":
            break
    if emlak_komisyonu>=kota:
        kota_doldu=True
    toplam_emlak_say = satin + kira #bir danışmanın sattığı ve kiraladığı toplam emlakların sayısı
    bir_calisan_top_satin_bedel = konut_satin_top_bedel + is_yeri_satin_top_bedel + arsa_satin_top_bedel # o ay bir çalışanın sattığı emlakların toplam ücretini hesaplar

    if satin == 0:  # o ay hiç satış yapamayan danışman sayısını hesapladı
        satis_yapamayan += 1
    if bir_calisan_top_satin_bedel > max_satin_bedel:  # satış bedeli olarak en çok satış yapan danışman
        max_satin_bedel = bir_calisan_top_satin_bedel
        max_s_b_ad_soyad = ad_soyad
        max_s_b_satilan_emlak_say = satin

    if satin > max_satin_say:  # satış adedi olarak en çok satış yapan danışman
        max_satin_say = satin
        max_s_say_ad_soyad = ad_soyad
        max_s_say_toplam_bedel = bir_calisan_top_satin_bedel
    prim = emlak_komisyonu * 0.1
    if prim > maas:
        primi_maasindan_yuksek += 1 # o ayki primi maaşından yüksek olan çalışan sayısını bulacak
    if kira > 10 :
        min10_veya_min25000_kira += 1  # min 10 emlak kiralayan veya 25000tl kira getirisi getiren emlak danışmanlarının sayısı

    print("\nAd Soyad:",ad_soyad)
    print("O ay sattığınız emlak adedi: {0} ve oranı: %{1:.2f}\tkiraladığınız emlak adedi: {2} ve oranı: %{3:.2f}".format(satin,satin*100/toplam_emlak_say,kira,kira*100/toplam_emlak_say))
    print("O ay konut tipi olarak satılan emlakların toplam bedeli: {0}TL".format(konut_satin_top_bedel))
    print("İş yeri tipi olarak satılan emlakların toplam bedeli: {0}TL".format(is_yeri_satin_top_bedel))
    print("Arsa tipi olarak satılan emlakların toplam bedeli: {0}TL".format(arsa_satin_top_bedel))
    print("O ay kiraladığınız konutların ortalama kira bedeli: {0:.2f}TL".format(konut_kira_bedel/konut_kira)) #kiralanan konut sayısına böl
    print("O ay en yüksek bedelle kiraladığınız konutun kira bedeli :",max_konut_kira_bedel,"TL")
    print("O ayki maaşınız: ",maas,"TL")
    print("O ayki priminiz: ",prim,"TL")
    print("O ayki kotanız: ",kota,"TL")
    print("O ay acenteye kazandırdığı toplam komisyon tutarı: ",emlak_komisyonu,"TL")
    print("O ayki kotanız doldu mu? ",end="")
    if kota_doldu:
        kota_dolu_calisan_say+=1
        print("Evet")
        print(ASGARI_UCRET_2020 / 2, "TL ikramiye almaya hak kazandınız.")
        aylik_toplam_ucret=maas+emlak_komisyonu*0.1+ASGARI_UCRET_2020/2
        print("Ay toplam ücreti: ",aylik_toplam_ucret,"TL")
    else:
        print("Hayır")
        print("Maalesef ikramiye almaya hak kazanamadınız.")
        aylik_toplam_ucret=maas+emlak_komisyonu*0.1
        print("Ay toplam ücreti: ",aylik_toplam_ucret,"TL")
    print("---------------------------------------------")

    if prim > prim_max: # maximum primi hesaplar
        prim_max = prim
        prim_max_ad_soyad = ad_soyad
        prim_max_maas = maas
        prim_max_aylik_toplam_ucret = aylik_toplam_ucret
    #prim_min=prim
    if prim <prim_min : #minimum primi hesaplar
        prim_min = prim
        prim_min_ad_soyad = ad_soyad
        prim_min_maas = maas
        prim_min_aylik_toplam_ucret = aylik_toplam_ucret

    # aşağıda top_... şeklinde yazılmış tüm değişkenler bir ayın sonunda tüm çalışanların toplamda elde ettiği değerleri ifade etmektedir
    top_konut_satis_bedel += konut_satin_top_bedel
    top_isyeri_satis_bedel += is_yeri_satin_top_bedel
    top_arsa_satis_bedel += arsa_satin_top_bedel
    top_emlak_komisyonu += emlak_komisyonu
    tum_calisanlara_ode += aylik_toplam_ucret  # tüm çalışanlara ödenecek aylık toplam ücret




print("Konut emlak tipindeki bu ayki satış sayısı: {0} , kiralama sayısı: {1} ve satılma oranı: %{2:.2f}".format(top_konut_satis_say,top_konut_kira_say,top_konut_satis_say*100/(top_konut_satis_say+top_konut_kira_say)))
print("İş yeri emlak tipindeki bu ayki satış sayısı: {0} , kiralama sayısı: {1} ve satılma oranı: %{2:.2f}".format(top_isyeri_satis_say,top_isyeri_kira_say,top_isyeri_satis_say*100/(top_isyeri_satis_say+top_isyeri_kira_say)))
print("Arsa emlak tipindeki bu ayki satış sayısı: {0} , kiralama sayısı: {1} ve satılma oranı: %{2:.2f}".format(top_arsa_satis_say,top_arsa_kira_say,top_arsa_satis_say*100/(top_arsa_satis_say+top_arsa_kira_say)))

print("Konut emlak tipi için o ay satılan emlakların satış bedellerinin toplamı: {0}TL".format(top_konut_satis_bedel))
print("İş yeri emlak tipi için o ay satılan emlakların satış bedellerinin toplamı: {0}TL".format(top_isyeri_satis_bedel))
print("Arsa emlak tipi için o ay satılan emlakların satış bedellerinin toplamı: {0}TL".format(top_arsa_satis_bedel))

print("O ay en yüksek bedelle satılan emlağın tipi: {0}, satış bedeli: {1}TL , satışı yapan danışmanın adı-soyadı: {2}".format(max_satis_genel_emlak_tipi_uzun,max_satis_genel,max_satis_genel_ad_soyad))

print("O ay en yüksek bedelle kiralanan konutun kira bedeli: {0}TL, kiralayan danışmanın adı-soyadı: {1}".format(max_kira_genel,max_kira_genel_ad_soyad))

print("O ay kiralanan konutlardan kira bedeli aylık asgari net ücretten yüksek olan konutların sayısı: {0} ve kiralanan konutlar içindeki oranı: %{1:.2f}".format(asgari_ucret_ustu_kira,asgari_ucret_ustu_kira*100/(top_konut_kira_say+top_isyeri_kira_say+top_arsa_kira_say))) #!!!

print("O ay hiç satış yapamayan danışmanların sayısı ve tüm danışmanlar içindeki oranı: %",format(satis_yapamayan/calisan_say,".2f"))

print("O ay satış adeti olarak en çok satış yapan danışmanın adı-soyadı: {0}, sattığı emlak sayısı: {1} ve toplam satış bedelleri: {2}TL".format(max_s_say_ad_soyad,max_satin_say,max_s_say_toplam_bedel))
print("O ay satış bedeli olarak en çok satış yapan danışmanın adı-soyadı: {0}, sattığı emlak sayısı: {1} ve toplam satış bedelleri: {2}TL".format(max_s_b_ad_soyad,max_s_b_satilan_emlak_say,max_satin_bedel))
print("O ay kotasını dolduran danışmanların sayısı ve tüm danışmanlar içindeki oranı: %",format(kota_dolu_calisan_say*100/calisan_say,".2f"))
print("O ay primi maaşından yüksek olan danışmanların sayısı ve tüm danışmanlar içindeki oranı: %",format(primi_maasindan_yuksek*100/calisan_say,".2f"))
print("O ay en az 10 adet veya en az 25000 TL tutarında emlak kiralayan danışmanların sayısı: ",min10_veya_min25000_kira)
print("O ay en yüksek prim alan danışmanın adı soyadı: {0} , maaşı: {1}TL , primi: {2}TL ve aylık toplam ücreti: {3}TL".format(prim_max_ad_soyad,prim_max_maas,prim_max,prim_max_aylik_toplam_ucret))
print("O ay en düşük prim alan danışmanın adı soyadı: {0} , maaşı: {1}TL , primi: {2}TL ve aylık toplam ücreti: {3}TL".format(prim_min_ad_soyad,prim_min_maas,prim_min,prim_min_aylik_toplam_ucret))
print("O ay tüm satış danışmanlarına ödenecek toplam ücretlerin toplamı: {0}TL ve ortalaması :{1:.2f}TL".format(tum_calisanlara_ode,tum_calisanlara_ode/calisan_say))
print("O ay acentenin kazandığı toplam komisyon :",top_emlak_komisyonu,"TL")
























