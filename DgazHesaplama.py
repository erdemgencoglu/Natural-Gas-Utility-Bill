ocak	=31
subat	=28
mart	=31
nisan	=30
mayıs	=31
haziran	=30
temmuz	=30
agustos	=31
eylul	=30
ekim	=30
kasım	=30
aralık	=31

birimFiyat=0.79 #Vergiler dahil m3 fiyatı

aylıkSarfiyat=input("Aylık Sarfiyatinizi m3 cinsinden giriniz: ")
#Şimdilik büyük küçük harf uyarlılığı yapılmadı
donem=input("Hangi aya ait faturayı hesaplamak istersiniz(Ay isimlerinde kücük harf kul.)? :")

ay=eval(donem)
#Kullanıcının günlük sarfiyatı
gunlukSarfiyat=int(aylıkSarfiyat)/ay
fatura=birimFiyat*gunlukSarfiyat*ay
print("Faturaniz ",fatura," Tl dir.");
