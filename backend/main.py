# -*- coding: utf-8 -*-
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from textblob import TextBlob

app = FastAPI()

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
        "recipes": ["1. Magnezyum Smoothie", "2. Kabak Çekirdeği Kavurma", "3. Bitter ve Papatya Çayı", "4. Ispanak Salatası", "5. Melisa Çayı"]
    },
    "mutlu": {
        "nutrient": "Serotonin ve Omega-3",
        "foods": ["Muz", "Ceviz", "Somon"],
        "recipes": ["1. Mutluluk Kasesi", "2. Izgara Somon", "3. Muzlu Yulaf Topları", "4. Ceviz Ezmeli Ekmek", "5. Muzlu Portakal Suyu"]
    },
    "yorgun": {
        "nutrient": "Demir ve Kompleks Karbonhidratlar",
        "foods": ["Yulaf", "Kırmızı Et", "Pekmez"],
        "recipes": ["1. Pekmezli Yulaf", "2. Izgara Biftek", "3. Pekmezli Ilık Su", "4. Mercimek Salatası", "5. Gün Kurusu ve Badem"]
    },
    "uzgun": {
        "nutrient": "D Vitamini ve Triptofan",
        "foods": ["Yumurta", "Hindi Eti", "Süt"],
        "recipes": ["1. Sebzeli Omlet", "2. Hindi Çorbası", "3. Ballı Sıcak Süt", "4. Yumurtalı Ton Balığı", "5. Çilekli Meyve Tabağı"]
    },
    "sinirli": {
        "nutrient": "Potasyum ve C Vitamini",
        "foods": ["Patates", "Portakal", "Kereviz"],
        "recipes": ["1. Zeytinyağlı Patates", "2. Portakal Havuç Suyu", "3. Kereviz Detoksu", "4. Zeytinyağlı Kereviz", "5. Yoğurtlu Havuç"]
    },
    "heyecanli": {
        "nutrient": "Kalsiyum ve Dengeli Şeker",
        "foods": ["Yoğurt", "Badem", "Kefir"],
        "recipes": ["1. Bademli Yoğurt", "2. Çilekli Kefir", "3. Chia Puding", "4. Kuru Üzüm ve Badem", "5. Lorlu Domates Salatası"]
    },
    "kaygili": {
        "nutrient": "L-theanine ve Antioksidanlar",
        "foods": ["Yeşil Çay", "Kuşkonmaz", "Yaban Mersini"],
        "recipes": ["1. Limonlu Yeşil Çay", "2. Izgara Kuşkonmaz", "3. Yaban Mersinli Yoğurt", "4. Çiğ Kaju", "5. Buharda Brokoli"]
    },
    "uykulu": {
        "nutrient": "Tyrosine ve Hafif Kafein",
        "foods": ["Kahve", "Sert Peynir", "Tam Buğday"],
        "recipes": ["1. Filtre Kahve", "2. Peynirli Sandviç", "3. Naneli Buzlu Su", "4. Eski Peynir ve Ceviz", "5. Yumurtalı Kahvaltı"]
    },
    "yalniz": {
        "nutrient": "Rahatlatıcı Karbonhidratlar",
        "foods": ["Makarna", "Sıcak Çikolata", "Mısır"],
        "recipes": ["1. Domatesli Makarna", "2. Sıcak Çikolata", "3. Patlamış Mısır", "4. Fırın Peynirli Ekmek", "5. Tarçınlı Elma"]
    },
    "enerjik": {
        "nutrient": "Sürdürülebilir Enerji ve Protein",
        "foods": ["Kinoa", "Fıstık Ezmesi", "Chia"],
        "recipes": ["1. Narlı Kinoa Salatası", "2. Fıstık Ezmeli Elma", "3. Chia Puding", "4. Muzlu Smoothie", "5. Karabuğday Sote"]
    },
    "odaklanmis": {
        "nutrient": "Antosiyanin ve Flavonoidler",
        "foods": ["Yaban Mersini", "Ceviz", "Biberiye"],
        "recipes": ["1. Biberiyeli Omlet", "2. Zihin Kasesi", "3. Biberiye Çayı", "4. Semizotu Salatası", "5. Bitterli Yaban Mersini"]
    },
    "saskin": {
        "nutrient": "C Vitamini ve Glikoz Dengesi",
        "foods": ["Kivi", "Kırmızı Biber", "Çilek"],
        "recipes": ["1. Renkli Meyve Tabağı", "2. Biberli Mantar Sote", "3. Kivi Smoothie", "4. Çilekli Yoğurt", "5. Naneli Çilek Çayı"]
    },
    "huzurlu": {
        "nutrient": "Apigenin ve Linalool",
        "foods": ["Papatya", "Kereviz", "Bal"],
        "recipes": ["1. Lavantalı Papatya Çayı", "2. Labneli Kereviz Sapı", "3. Ballı Papatya Çayı", "4. Zeytinyağlı Kereviz", "5. Naneli Salatalık Suyu"]
    },
    "keyifsiz": {
        "nutrient": "Folat ve Magnezyum",
        "foods": ["Mercimek", "Avokado", "Kuşkonmaz"],
        "recipes": ["1. Mercimek Çorbası", "2. Avokado Tost", "3. Kuşkonmaz ve Yumurta", "4. Avokadolu Mısır Salatası", "5. Cevizli Kuru İncir"]
    },
    "sabirsiz": {
        "nutrient": "B Kompleks Vitaminleri",
        "foods": ["Tam Tahıl", "Fıstık Ezmesi", "Süt"],
        "recipes": ["1. Tahıllı Bisküvi ve Süt", "2. Fıstık Ezmeli Elma", "3. Tarçınlı Ilık Süt", "4. Muzlu Lavaş Dürüm", "5. Yulaflı Bar"]
    },
    "utangac": {
        "nutrient": "Çinko ve Selenyum",
        "foods": ["Kabak Çekirdeği", "Kaju", "Mantar"],
        "recipes": ["1. Kaşarlı Mantar Dolması", "2. Kabak Çekirdeği", "3. Kajulu Roka Salatası", "4. Mantarlı Omlet", "5. Tavada Kaju"]
    },
    "gururlu": {
        "nutrient": "Yüksek Protein",
        "foods": ["Tavuk Göğsü", "Süzme Yoğurt", "Lor Peyniri"],
        "recipes": ["1. Izgara Tavuk", "2. Meyveli Süzme Yoğurt", "3. Tavuklu Sandviç", "4. Lorlu Çörek Otlu Tabak", "5. Çilekli Fit Smoothie"]
    },
    "tedirgin": {
        "nutrient": "Omega-3 Yağ Asitleri",
        "foods": ["Somon", "Semizotu", "Keten Tohumu"],
        "recipes": ["1. Keten Tohumlu Yoğurt", "2. Sarımsaklı Semizotu", "3. Fırın Somon", "4. Narlı Semizotu Salatası", "5. Balık Çorbası"]
    },
    "cesur": {
        "nutrient": "Kapsaisin ve Demir",
        "foods": ["Acı Biber", "Kırmızı Et", "Pekmez"],
        "recipes": ["1. Acılı Et Sote", "2. Tahin Pekmez ve Ceviz", "3. Acılı Köfte", "4. Pekmezli Kurabiye", "5. Meksika Fasulyeli Sote"]
    },
    "kararsiz": {
        "nutrient": "Kan Şekeri Dengeleyiciler",
        "foods": ["Tarçın", "Elma", "Badem"],
        "recipes": ["1. Tarçınlı Fırın Elma", "2. Tarçınlı Elma Rendesi", "3. Elma ve Badem", "4. Tarçınlı Elma Çayı", "5. Bademli Hurma"]
    }
}

@app.get("/oner")
def oner(mood: str):
    mood = mood.lower()
    return besin_verileri.get(mood, {"error": "Duygu bulunamadı"})

@app.get("/analiz")
def duygu_analizi(metin: str):
    analiz = TextBlob(metin)
    puan = analiz.sentiment.polarity
    metin_lower = metin.lower()
    
    # Türkçe anahtar kelime eşleştirme mantığı
    if any(k in metin_lower for k in ["yorgun", "bitkin", "halsiz"]):
        duygu = "yorgun"
    elif any(k in metin_lower for k in ["stres", "gergin", "baskı"]):
        duygu = "stresli"
    elif any(k in metin_lower for k in ["üzgün", "kötü", "ağlamak"]):
        duygu = "uzgun"
    elif any(k in metin_lower for k in ["mutlu", "iyi", "harika"]):
        duygu = "mutlu"
    elif any(k in metin_lower for k in ["kızgın", "sinirli", "öfke"]):
        duygu = "sinirli"
    elif any(k in metin_lower for k in ["heyecan", "sabırsız"]):
        duygu = "heyecanli"
    elif any(k in metin_lower for k in ["yalnız", "tek başıma"]):
        duygu = "yalniz"
    elif any(k in metin_lower for k in ["korku", "kaygı", "endişe"]):
        duygu = "kaygili"
    else:
        # Puanlama sistemine göre karar ver
        if puan > 0.2: duygu = "mutlu"
        elif puan < -0.2: duygu = "uzgun"
        else: duygu = "huzurlu"

    sonuc = besin_verileri.get(duygu, besin_verileri["huzurlu"])
    
    return {
        "tespit_edilen_duygu": duygu,
        "puan": puan,
        "besin_bilgisi": sonuc
    }