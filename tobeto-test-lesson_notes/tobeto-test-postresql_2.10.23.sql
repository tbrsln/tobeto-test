-- SQL => Structured Query Languages 
-- Veri sorgulama - Veri Manipülasyonu

--SELECT 
-- Select [kolonlar]/* from [tablo_adi] 
Select * from products
Select product_name, unit_price from products

--postresql küçük büyük harf duyarlılığı yok ama tablo isimlerine dikkat etmeliyiz
-- querylerimi ; ile ayırdığım zaman en sonki queryi gösteriyor
-- yazdığım sorguyu seçerek çalıştırabiliyorum


--WHERE 'den 'dan anlamı katar sorguya
--filtreleme 

Select * from products where unit_price >50;
Select * from products where unit_price >50 AND unit_price <100
Select * from products where unit_price BETWEEN 50 AND 100;
--son iki sorgu aynı şeyi ifade ediyor
Select product_name,category_id,unit_price from products
where unit_price >=50 OR category_id >5
--queryde or kullanıyorsam birisinin doğru olması yeterlidir diyorum

--IN() 
--aynı parametre üzerinde birden fazla filtreleme yapıyor
--içerisine parametre olarak verilen n kadar veri ile ilgili alanın uyuşmasını bekler
Select * from products where product_name IN('Chai','Chang','Ikura')
--aynısını or ile de yazabilirdik

Select * from products where category_id IN(1,2,3);


--LIKE 
-- bir kalıba benzeyen ifadeleri getirir
--% => ilgili metnin sol ya da sağında eklendiğinde
--sağ veya sol için metinden sonra gelecek metni önemsemiyorum

Select * from products where product_name LIKE '%t%';
--isminin içersinde t harfi bulunan tüm ürünleri getirir
Select * from products where product_name LIKE '%t';
--t harfiyle biten tüm ürünleri getir 
Select * from products where LOWER(product_name) LIKE 't%';
--Lower fonksiyonu benim için tüm harfleri küçültür

-- _ => karakter atlama olarak geçer
Select * from products where product_name LIKE '%__r';
-- son harfi r olan ürünleri getirir

--BUILT -IN FUNCTIONS
--SUMMARY => TOPLAMA
Select SUM(unit_price) from products;

--AVERAGE => ortalama alma
Select AVG(unit_price) from products;

--MAXIMUM => verilerimin arasındaki maximum değeri döner
Select MAX(unit_price) from products;

--MINIMUM => verilerimin arasındaki maximum değeri döner
Select MIN(unit_price) from products;

--COUNT => Adet döndürür
--50den büyük kaç satır var 
Select COUNT(*) from products where unit_price >50;

--DISTINCT => tekrarları engeller
--kaç farklı şehirden çalışanım var?
Select DISTINCT city from employees; 

--SUB-QUERY  - Alt sorgu
--ortalamanın altında bir fiyata sahip olan ürünlerimin bilgisini istiyorum

-- iç içe sorgu bilmeden önce nasıl yaparız?
Select AVG(unit_price) from products --önce bunu sonra burdan çıkan sonucu aşağıdaki sorguya yazıyoruz
Select * from products where unit_price <28,83

Select * from products where unit_price < (select AVG(unit_price) from products)

--en pahalı ürün bilgileri 
Select MAX(unit_price) from products
Select * from products where unit_price = 263.5
--en pahalı ürün bilgileri iç içe sorgu
Select * from products
where unit_price = (Select MAX(unit_price) from products)


--ORDER BY => sıralama
-- default olarak => küçükten büyüğe sıralama gerçekleştirir
--ASCENDING => A(rtan)SC => küçükten büyüğe 
--DESCENDING => D(üşen)ESC => büyükten küçüğe
Select product_name, unit_price from products 
order by unit_price ASC

Select product_name, unit_price from products 
order by unit_price DESC


-- hazır fonksiyon gibi düşünebiliriz, 
--tablodan çekmiyor güncel tarihi veriyor
Select current_date as "Bugünün Tarihi"
Select date_part('year', current_date)

--GETDATE() => Güncel tarihi-saati
--DATEDIFF('interval'(year), date1,date2)
--=> iki tarih arasındaki intervale göre farkı verir
-- bu fonksiyonlar postresqlde çalışmıyor mssqlde çalışabilir





















