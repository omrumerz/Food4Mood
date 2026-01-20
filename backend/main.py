# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Tarayıcı erişimi için CORS ayarları
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

besin_verileri = {
    "stresli": {
        "nutrient": "Magnezyum ve B6 Vitamini",
        "foods": ["Bitter Çikolata", "Kabak Çekirdeği", "Ispanak"],
        "recipes": [
            "1. Magnezyum Smoothie: Ispanak, muz ve badem sütünü karıştırın.",
            "2. Çıtır Atıştırmalık: Kabak çekirdeklerini az tuzla kavurun.",
            "3. Bitter Keyfi: 3 kare bitter çikolata ve yanında papatya çayı.",
            "4. Yeşil Salata: Bol ıspanaklı, cevizli ve limonlu bir kase hazırlayın.",
            "5. Rahatlatıcı Çay: Melisa otu demleyip içine bal ekleyin."
        ]
    },
    "mutlu": {
        "nutrient": "Serotonin ve Omega-3",
        "foods": ["Muz", "Ceviz", "Somon"],
        "recipes": [
            "1. Mutluluk Kasesi: Yoğurt, dilimlenmiş muz ve ceviz karışımı.",
            "2. Omega Izgara: Fırında somon balığı ve yanında kuşkonmaz.",
            "3. Enerji Topları: Ezilmiş muz ve yulafı yuvarlayıp dondurun.",
            "4. Günaydın Tabağı: Tam buğday ekmeği üzerine ceviz ezmesi.",
            "5. Tropikal İçecek: Taze sıkılmış portakal ve muz karışımı."
        ]
    },
    "yorgun": {
        "nutrient": "Demir ve Kompleks Karbonhidratlar",
        "foods": ["Yulaf", "Kırmızı Et", "Pekmez"],
        "recipes": [
            "1. Güç Kahvaltısı: Sütlü yulaf lapası içine 1 kaşık pekmez.",
            "2. Demir Deposu: Yağsız ızgara biftek ve bol yeşil salata.",
            "3. Enerji İksiri: Bir bardak ılık suya pekmez ve limon ekleyin.",
            "4. Baklagil Gücü: Mercimek salatası ve yanında tam tahıllı ekmek.",
            "5. Atıştırmalık: Gün kurusu kayısı ve çiğ badem tüketin."
        ]
    },
    "uzgun": {
        "nutrient": "D Vitamini ve Triptofan",
        "foods": ["Yumurta", "Hindi Eti", "Süt"],
        "recipes": [
            "1. Sebzeli Omlet: 2 yumurta ve bol mevsim sebzesiyle pişirin.",
            "2. Hindi Çorbası: Sebzeli ve şehriyeli sıcak hindi çorbası.",
            "3. Gece İçeceği: Tarçınlı ve ballı sıcak süt için.",
            "4. Güneş Salatası: Haşlanmış yumurtalı ton balıklı salata.",
            "5. Meyve Tabağı: Çilek ve ananas dilimleriyle moral depolayın."
        ]
    },
    "sinirli": {
        "nutrient": "Potasyum ve C Vitamini",
        "foods": ["Patates", "Portakal", "Kereviz"],
        "recipes": [
            "1. Sakinleştirici Patates: Haşlanmış patates üzerine zeytinyağı ve biberiye.",
            "2. Vitamin Bombası: Taze sıkılmış portakal ve havuç suyu.",
            "3. Detoks Suyu: Kereviz sapı, elma ve limonu blenderdan geçirin.",
            "4. Hafif Öğün: Zeytinyağlı kereviz yemeği ve yanında cacık.",
            "5. Çıtır Sebze: Havuç ve salatalık dilimlerini yoğurt sosla yiyin."
        ]
    },
    "heyecanli": {
        "nutrient": "Kalsiyum ve Dengeli Şeker",
        "foods": ["Yoğurt", "Badem", "Kefir"],
        "recipes": [
            "1. Bademli Yoğurt: Süzme yoğurt içine çiğ badem ve yaban mersini.",
            "2. Probiyotik İçecek: Çilekli ev yapımı kefir hazırlayın.",
            "3. Dengeleyici Puding: Chia tohumu ve sütü geceden bekletin.",
            "4. Kuruyemiş Karışımı: Badem, fındık ve kuru üzüm tüketin.",
            "5. Hafif Akşam: Lor peynirli ve domatesli salata yapın."
        ]
    },
    "kaygili": {
        "nutrient": "L-theanine ve Antioksidanlar",
        "foods": ["Yeşil Çay", "Kuşkonmaz", "Yaban Mersini"],
        "recipes": [
            "1. Yatıştırıcı Çay: Taze demlenmiş yeşil çay ve içine bir dilim limon.",
            "2. Yeşil Izgara: Zeytinyağlı haşlanmış kuşkonmaz tabağı.",
            "3. Antioksidan Kase: Yoğurt üzerine taze yaban mersini ekleyin.",
            "4. Beyin Dostu: Bir avuç çiğ kaju fıstığı tüketin.",
            "5. Buharda Sebze: Brokoli ve karnabahar üzerine sarımsaklı yoğurt."
        ]
    },
    "uykulu": {
        "nutrient": "Tyrosine ve Hafif Kafein",
        "foods": ["Kahve", "Sert Peynir", "Tam Buğday"],
        "recipes": [
            "1. Ayıltıcı Kahve: Şekersiz bir fincan filtre kahve için.",
            "2. Enerji Sandviçi: Tam buğday ekmeğine kaşar peyniri ve domates.",
            "3. Canlandırıcı Su: Buzlu suyun içine nane ve salatalık dilimleyin.",
            "4. Atıştırmalık: 2 adet ceviz ve 1 dilim eski peynir.",
            "5. Protein Kahvaltısı: Haşlanmış yumurta ve bol maydanoz."
        ]
    },
    "yalniz": {
        "nutrient": "Rahatlatıcı Karbonhidratlar",
        "foods": ["Makarna", "Sıcak Çikolata", "Mısır"],
        "recipes": [
            "1. Sevgi Makarnası: Domates soslu ve peynirli tam buğday makarna.",
            "2. Sıcak Keyif: Az şekerli, bol kakaolu sıcak çikolata.",
            "3. Ev Sineması: Az yağlı patlamış mısır hazırlayın.",
            "4. Fırın Lezzeti: Ekmek üstü peynir ve kekikli fırın dilimleri.",
            "5. Tatlı Teselli: Fırınlanmış tarçınlı elma dilimleri."
        ]
    },
    "enerjik": {
        "nutrient": "Sürdürülebilir Enerji ve Protein",
        "foods": ["Kinoa", "Fıstık Ezmesi", "Chia"],
        "recipes": [
            "1. Süper Salata: Kinoa, nar ve maydanozlu renkli salata.",
            "2. Enerji Tostu: Elma dilimleri üzerine fıstık ezmesi sürün.",
            "3. Chia Puding: Hindistan cevizi sütü ve chia tohumu karışımı.",
            "4. Sporcu İçeceği: Muz, süt ve bir kaşık fıstık ezmesi smoothie.",
            "5. Tahıl Günü: Haşlanmış karabuğday ve sebze sote."
        ]
    },
    "odaklanmis": {
        "nutrient": "Antosiyanin ve Flavonoidler",
        "foods": ["Yaban Mersini", "Ceviz", "Biberiye"],
        "recipes": [
            "1. Zihin Açıcı Omlet: Taze biberiyeli ve peynirli omlet.",
            "2. Beyin Kasesi: Yaban mersini, ceviz ve yulaf karışımı.",
            "3. Odak Çayı: Biberiye ve limonu sıcak suda demleyin.",
            "4. Omega Salatası: Semizotu, ceviz ve nar ekşili salata.",
            "5. Akıllı Atıştırmalık: Bitter çikolata kaplı yaban mersini."
        ]
    },
    "saskin": {
        "nutrient": "C Vitamini ve Glikoz Dengesi",
        "foods": ["Kivi", "Kırmızı Biber", "Çilek"],
        "recipes": [
            "1. Renkli Tabak: Dilimlenmiş kivi, çilek ve ananas kasesi.",
            "2. Vitamin Sote: Kırmızı biberli ve mantarlı hızlı sote.",
            "3. Şaşırtıcı Smoothie: Kivi, ıspanak ve elma suyunu karıştırın.",
            "4. Çilekli Yoğurt: Ev yapımı yoğurt içine taze çilek dilimleri.",
            "5. Serinletici: Çilekli ve naneli soğuk çay hazırlayın."
        ]
    },
    "huzurlu": {
        "nutrient": "Apigenin ve Linalool",
        "foods": ["Papatya", "Kereviz", "Bal"],
        "recipes": [
            "1. Huzur Çayı: Papatya ve lavanta karışımı bitki çayı.",
            "2. Hafif Başlangıç: Kereviz saplarını labne peynirine batırıp yiyin.",
            "3. Tatlı Rüya: Bir kaşık süzme bal eklenmiş ılık papatya çayı.",
            "4. Sakin Öğün: Zeytinyağlı kereviz yemeği ve bol yoğurt.",
            "5. Yeşil İçecek: Salatalık, nane ve kereviz sapı suyu."
        ]
    },
    "keyifsiz": {
        "nutrient": "Folat ve Magnezyum",
        "foods": ["Mercimek", "Avokado", "Kuşkonmaz"],
        "recipes": [
            "1. Canlandırıcı Çorba: Bol baharatlı sarı mercimek çorbası.",
            "2. Avokado Tost: Tam tahıllı ekmek üzerine ezilmiş avokado ve pul biber.",
            "3. Yeşil Güç: Izgara kuşkonmaz ve yanında haşlanmış yumurta.",
            "4. Keyif Salatası: Avokadolu ve domatesli mısır salatası.",
            "5. Enerji Lokması: Kuru incir içine ceviz yerleştirip tüketin."
        ]
    },
    "sabirsiz": {
        "nutrient": "B Kompleks Vitaminleri",
        "foods": ["Tam Tahıl", "Fıstık Ezmesi", "Süt"],
        "recipes": [
            "1. Hızlı Kahvaltı: Tam tahıllı bisküvi ve bir bardak süt.",
            "2. Sabır Atıştırmalığı: Elma dilimleri ve fıstık ezmesi keyfi.",
            "3. Sakinleştirici Süt: İçine tarçın çubuğu atılmış ılık süt.",
            "4. Pratik Dürüm: Lavaş içine fıstık ezmesi ve muz dilimleri.",
            "5. Tahıl Bar: Ev yapımı yulaflı ve ballı bar."
        ]
    },
    "utangac": {
        "nutrient": "Çinko ve Selenyum",
        "foods": ["Kabak Çekirdeği", "Kaju", "Mantar"],
        "recipes": [
            "1. Mantar Ziyafeti: Fırında kaşarlı mantar dolması.",
            "2. Çinko Deposu: Bir avuç dolusu çiğ kabak çekirdeği.",
            "3. Kaju Salatası: Roka tabağı üzerine kavrulmuş kaju ekleyin.",
            "4. Mantarlı Omlet: İstiridye mantarlı ve bol maydanozlu omlet.",
            "5. Çıtır Karışım: Kaju ve fındığı tavada hafifçe ısıtın."
        ]
    },
    "gururlu": {
        "nutrient": "Yüksek Protein",
        "foods": ["Tavuk Göğsü", "Süzme Yoğurt", "Lor Peyniri"],
        "recipes": [
            "1. Başarı Tabağı: Izgara tavuk göğsü ve yanında haşlanmış brokoli.",
            "2. Protein Kasesi: Süzme yoğurt, lor peyniri ve taze meyve.",
            "3. Şampiyon Sandviçi: Tavuklu ve avokadolu tam buğday sandviç.",
            "4. Lor Salatası: Lor peyniri, çörek otu ve zeytinyağlı tabak.",
            "5. Fit Smoothie: Süzme yoğurt, çilek ve bir ölçek protein tozu (isteğe bağlı)."
        ]
    },
    "tedirgin": {
        "nutrient": "Omega-3 Yağ Asitleri",
        "foods": ["Somon", "Semizotu", "Keten Tohumu"],
        "recipes": [
            "1. Tedirginlik Savar: Yoğurt içine 1 kaşık keten tohumu ekleyin.",
            "2. Hafif Akşam: Zeytinyağlı sarımsaklı semizotu yemeği.",
            "3. Fırın Somon: Defne yapraklı fırın somon ve roka salatası.",
            "4. Tohum Salatası: Keten tohumlu ve narlı semizotu salatası.",
            "5. Balık Çorbası: Sebzeli ve bol limonlu sıcak balık çorbası."
        ]
    },
    "cesur": {
        "nutrient": "Kapsaisin ve Demir",
        "foods": ["Acı Biber", "Kırmızı Et", "Pekmez"],
        "recipes": [
            "1. Ateşli Sote: Acı biberli ve kekikli kırmızı et sote.",
            "2. Cesaret İksiri: Tahin ve pekmez karışımı yanında ceviz.",
            "3. Baharatlı Izgara: Acı pul biberli ızgara köfte tabağı.",
            "4. Enerji Bombası: Pekmezli ve yulaflı kurabiye.",
            "5. Acı Soslu Sebze: Meksika fasulyeli ve acı soslu sebze karışımı."
        ]
    },
    "kararsiz": {
        "nutrient": "Kan Şekeri Dengeleyiciler",
        "foods": ["Tarçın", "Elma", "Badem"],
        "recipes": [
            "1. Net Karar: Tarçın serpilmiş fırınlanmış elma dilimleri.",
            "2. Denge Kasesi: Elma rendesi, yoğurt ve bol tarçın.",
            "3. Atıştırmalık: Bir adet yeşil elma ve yanında 10 adet badem.",
            "4. Karar Çayı: Tarçın çubuğu ve elma kabuklu bitki çayı.",
            "5. Bademli Hurma: İçi badem dolu 3 adet hurma tüketin."
        ]
    }
}

@app.get("/oner")
def oner(mood: str):
    mood = mood.lower()
    return besin_verileri.get(mood, {"error": "Duygu bulunamadı"})