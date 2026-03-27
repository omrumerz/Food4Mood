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

# Gelişmiş Besin ve Tarif Veritabanı
besin_verileri = {
    "stresli": {
        "nutrient": "Magnezyum ve B6 Vitamini",
        "foods": ["Bitter Çikolata", "Kabak Çekirdeği", "Ispanak"],
        "recipes": [
            {"name": "Magnezyum Smoothie", "duration": "5 dk", "calories": "180 kcal", "steps": "Ispanak, muz ve badem sütünü blenderdan geçirin. Üzerine bitter çikolata rendeleyin."},
            {"name": "Çıtır Atıştırmalık", "duration": "15 dk", "calories": "120 kcal", "steps": "Kabak çekirdeklerini az tuzla tavada 5 dakika kavurun. Soğuyunca tüketin."}
        ]
    },
    "mutlu": {
        "nutrient": "Serotonin ve Omega-3",
        "foods": ["Muz", "Ceviz", "Somon"],
        "recipes": [
            {"name": "Mutluluk Kasesi", "duration": "8 dk", "calories": "310 kcal", "steps": "Yoğurt üzerine dilimlenmiş muz ve dövülmüş ceviz ekleyerek servis edin."},
            {"name": "Omega Izgara", "duration": "25 dk", "calories": "450 kcal", "steps": "Somonu zeytinyağı ve limonla marine edip fırında 20 dakika pişirin."}
        ]
    },
    "yorgun": {
        "nutrient": "Demir ve Kompleks Karbonhidratlar",
        "foods": ["Yulaf", "Kırmızı Et", "Pekmez"],
        "recipes": [
            {"name": "Güç Kahvaltısı", "duration": "10 dk", "calories": "290 kcal", "steps": "Yulafı sütle pişirin, içine bir kaşık pekmez ve fındık ekleyin."},
            {"name": "Demir Deposu Izgara", "duration": "20 dk", "calories": "350 kcal", "steps": "Yağsız bifteği döküm tavada pişirin, yanında bol limonlu maydanoz salatasıyla tüketin."}
        ]
    },
    "uzgun": {
        "nutrient": "D Vitamini ve Triptofan",
        "foods": ["Yumurta", "Hindi Eti", "Süt"],
        "recipes": [
            {"name": "Moral Omleti", "duration": "7 dk", "calories": "210 kcal", "steps": "2 yumurtayı beyaz peynir ve dereotu ile çırpıp az yağda pişirin."},
            {"name": "Sıcak Rahatlama", "duration": "5 dk", "calories": "150 kcal", "steps": "Sütü ısıtın, içine bir çay kaşığı bal ve bir tutam tarçın ekleyin."}
        ]
    },
    "sinirli": {
        "nutrient": "Potasyum ve C Vitamini",
        "foods": ["Patates", "Portakal", "Kereviz"],
        "recipes": [
            {"name": "Sakinleştirici Salata", "duration": "12 dk", "calories": "110 kcal", "steps": "Rendelediğiniz kerevizi yoğurt ve dövülmüş cevizle karıştırın."},
            {"name": "Potasyum Sote", "duration": "20 dk", "calories": "240 kcal", "steps": "Patatesleri küp küp doğrayıp biberiye ile fırınlayın."}
        ]
    },
    "heyecanli": {
        "nutrient": "Kalsiyum ve Dengeli Glikoz",
        "foods": ["Yoğurt", "Badem", "Kefir"],
        "recipes": [
            {"name": "Denge Kasesi", "duration": "5 dk", "calories": "190 kcal", "steps": "Süzme yoğurda çiğ badem ve yaban mersini ekleyerek karıştırın."},
            {"name": "Meyveli Kefir", "duration": "3 dk", "calories": "130 kcal", "steps": "Kefiri çileklerle beraber blenderdan geçirin."}
        ]
    },
    "kaygili": {
        "nutrient": "L-theanine ve Antioksidanlar",
        "foods": ["Yeşil Çay", "Kuşkonmaz", "Yaban Mersini"],
        "recipes": [
            {"name": "Huzur Çayı", "duration": "5 dk", "calories": "0 kcal", "steps": "Yeşil çayı 80 derecede demleyin, içine taze nane ekleyin."},
            {"name": "Hafif Sote", "duration": "15 dk", "calories": "90 kcal", "steps": "Kuşkonmazları az zeytinyağında 5-6 dakika çevirin, üzerine tuz ekleyin."}
        ]
    },
    "uykulu": {
        "nutrient": "Tyrosine ve Kafein",
        "foods": ["Kahve", "Sert Peynir", "Tam Buğday"],
        "recipes": [
            {"name": "Ayılma Sandviçi", "duration": "8 dk", "calories": "280 kcal", "steps": "Tam buğday ekmeğine eski kaşar ve domates ekleyerek tost yapın."},
            {"name": "Enerji Kahvesi", "duration": "5 dk", "calories": "5 kcal", "steps": "Filtre kahve demleyin ve içine uyanıklığı artırmak için tarçın ekleyin."}
        ]
    },
    "yalniz": {
        "nutrient": "Serotonin Destekçileri",
        "foods": ["Makarna", "Sıcak Çikolata", "Mısır"],
        "recipes": [
            {"name": "Ev Makarnası", "duration": "15 dk", "calories": "380 kcal", "steps": "Tam buğday makarnayı domates sosu ve bol fesleğenle pişirin."},
            {"name": "Sarılma Etkili İçecek", "duration": "7 dk", "calories": "220 kcal", "steps": "%70 kakaolu bitter çikolatayı sütle eriterek hazırlayın."}
        ]
    },
    "enerjik": {
        "nutrient": "Yüksek Protein ve Kompleks Karbonhidrat",
        "foods": ["Kinoa", "Fıstık Ezmesi", "Chia"],
        "recipes": [
            {"name": "Performans Salatası", "duration": "20 dk", "calories": "320 kcal", "steps": "Haşlanmış kinoayı haşlanmış tavuk göğsü ve yeşilliklerle karıştırın."},
            {"name": "Chia Puding", "duration": "10 dk", "calories": "210 kcal", "steps": "Chia tohumlarını sütte bekletin, üzerine fıstık ezmesi ekleyin."}
        ]
    },
    "odaklanmis": {
        "nutrient": "Antosiyanin ve Flavonoid",
        "foods": ["Yaban Mersini", "Ceviz", "Biberiye"],
        "recipes": [
            {"name": "Zihin Salatası", "duration": "10 dk", "calories": "160 kcal", "steps": "Roka, ceviz ve yaban mersini üzerine nar ekşili sos dökün."},
            {"name": "Biberiyeli Fırın", "duration": "25 dk", "calories": "230 kcal", "steps": "Tavukları taze biberiye ve sarımsakla fırınlayın."}
        ]
    },
    "saskin": {
        "nutrient": "C Vitamini Dengesi",
        "foods": ["Kivi", "Kırmızı Biber", "Çilek"],
        "recipes": [
            {"name": "Renkli Tabak", "duration": "5 dk", "calories": "110 kcal", "steps": "Kivi ve çilekleri dilimleyip üzerine az bal gezdirin."},
            {"name": "Vitamini Bol Sote", "duration": "12 dk", "calories": "95 kcal", "steps": "Kırmızı biberleri jülyen doğrayıp az yağda soteleyin."}
        ]
    },
    "huzurlu": {
        "nutrient": "Apigenin",
        "foods": ["Papatya", "Kereviz", "Bal"],
        "recipes": [
            {"name": "Akşam Huzuru", "duration": "6 dk", "calories": "40 kcal", "steps": "Papatya çayını demleyip içine yarım kaşık bal ekleyin."},
            {"name": "Hafif Atıştırmalık", "duration": "5 dk", "calories": "60 kcal", "steps": "Kereviz saplarını labne peynirine banarak tüketin."}
        ]
    },
    "keyifsiz": {
        "nutrient": "Folat ve Magnezyum",
        "foods": ["Mercimek", "Avokado", "Kuşkonmaz"],
        "recipes": [
            {"name": "Canlandırıcı Çorba", "duration": "30 dk", "calories": "180 kcal", "steps": "Kırmızı mercimeği zerdeçal ile pişirip blenderdan geçirin."},
            {"name": "Avokado Tost", "duration": "10 dk", "calories": "260 kcal", "steps": "Ezip baharatladığınız avokadoyu kızarmış ekmek üzerine sürün."}
        ]
    },
    "sabirsiz": {
        "nutrient": "B Kompleks Vitaminleri",
        "foods": ["Tam Tahıl", "Fıstık Ezmesi", "Süt"],
        "recipes": [
            {"name": "Hızlı Atıştırmalık", "duration": "3 dk", "calories": "220 kcal", "steps": "Pirinç patlağı üzerine fıstık ezmesi ve muz dilimleri ekleyin."},
            {"name": "Tahıl Gevreği", "duration": "2 dk", "calories": "190 kcal", "steps": "Tam tahıllı gevreği soğuk süt ve tarçınla hazırlayın."}
        ]
    },
    "utangac": {
        "nutrient": "Çinko ve Selenyum",
        "foods": ["Kabak Çekirdeği", "Kaju", "Mantar"],
        "recipes": [
            {"name": "Güven Veren Mantar", "duration": "15 dk", "calories": "140 kcal", "steps": "Mantarları sarımsak ve kekik ile tavada soteleyin."},
            {"name": "Kaju Karışımı", "duration": "5 dk", "calories": "170 kcal", "steps": "Çiğ kaju ve kabak çekirdeklerini karıştırıp tüketin."}
        ]
    },
    "gururlu": {
        "nutrient": "Yüksek Kaliteli Protein",
        "foods": ["Tavuk Göğsü", "Süzme Yoğurt", "Lor Peyniri"],
        "recipes": [
            {"name": "Şampiyon Tabağı", "duration": "25 dk", "calories": "310 kcal", "steps": "Haşlanmış tavuğu baharatlı lor peyniri ile servis edin."},
            {"name": "Fit Dip Sos", "duration": "5 dk", "calories": "120 kcal", "steps": "Süzme yoğurdu dereotu ve nane ile karıştırıp sebze çubuklarıyla tüketin."}
        ]
    },
    "tedirgin": {
        "nutrient": "Omega-3 Yağ Asitleri",
        "foods": ["Somon", "Semizotu", "Keten Tohumu"],
        "recipes": [
            {"name": "Sakinlik Salatası", "duration": "10 dk", "calories": "130 kcal", "steps": "Semizotunu yoğurt ve keten tohumu ile karıştırın."},
            {"name": "Fırınlanmış Somon", "duration": "20 dk", "calories": "420 kcal", "steps": "Somonu sadece tuz ve karabiberle fırın torbasında pişirin."}
        ]
    },
    "cesur": {
        "nutrient": "Kapsaisin ve Demir",
        "foods": ["Acı Biber", "Kırmızı Et", "Pekmez"],
        "recipes": [
            {"name": "Ateşli Sote", "duration": "20 dk", "calories": "340 kcal", "steps": "Kuşbaşı etleri sivri biber ve acı pul biberle kavurun."},
            {"name": "Enerji Shot", "duration": "2 dk", "calories": "60 kcal", "steps": "Bir bardak suya pekmez ve bol limon ekleyip tek seferde için."}
        ]
    },
    "kararsiz": {
        "nutrient": "Glikoz Dengesi",
        "foods": ["Tarçın", "Elma", "Badem"],
        "recipes": [
            {"name": "Netleştirici Elma", "duration": "15 dk", "calories": "150 kcal", "steps": "Elmaları dilimleyip üzerine tarçın dökerek fırınlayın."},
            {"name": "Bademli Hurma", "duration": "5 dk", "calories": "120 kcal", "steps": "Hurmaların içine birer adet badem yerleştirerek tüketin."}
        ]
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