import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(const MoodFoodApp());

class MoodFoodApp extends StatelessWidget {
  const MoodFoodApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      // 1. DEĞİŞİKLİK: Tarayıcı sekmesinde görünecek isim
      title: 'Food4Mood', 
      theme: ThemeData(useMaterial3: true, colorSchemeSeed: Colors.deepPurple),
      home: const AnaEkran(),
    );
  }
}

class AnaEkran extends StatefulWidget {
  const AnaEkran({super.key});
  @override
  State<AnaEkran> createState() => _AnaEkranState();
}

class _AnaEkranState extends State<AnaEkran> {
  String tavsiye = "";
  bool yukleniyor = false;
  bool secimYapildi = false;
  String secilenDuyguIcon = "";
  String secilenDuyguYazi = "";
  Color secilenDuyguRenk = Colors.deepPurple;

  final List<Map<String, dynamic>> duygular = [
    {"id": "stresli", "label": "Stresli 😫", "renk": 0xFFE57373},
    {"id": "mutlu", "label": "Mutlu 😊", "renk": 0xFFFFF176},
    {"id": "yorgun", "label": "Yorgun 😴", "renk": 0xFF81C784},
    {"id": "uzgun", "label": "Üzgün 😔", "renk": 0xFF64B5F6},
    {"id": "sinirli", "label": "Sinirli 😡", "renk": 0xFFFF8A65},
    {"id": "heyecanli", "label": "Heyecanlı 🤩", "renk": 0xFFBA68C8},
    {"id": "kaygili", "label": "Kaygılı 😟", "renk": 0xFFAED581},
    {"id": "uykulu", "label": "Uykulu 🥱", "renk": 0xFFFFD54F},
    {"id": "yalniz", "label": "Yalnız 🥺", "renk": 0xFF90A4AE},
    {"id": "enerjik", "label": "Enerjik ⚡", "renk": 0xFFFFB74D},
    {"id": "odaklanmis", "label": "Odaklanmış 🧠", "renk": 0xFF4DD0E1},
    {"id": "saskin", "label": "Şaşkın 😯", "renk": 0xFFCE93D8},
    {"id": "huzurlu", "label": "Huzurlu 🍃", "renk": 0xFFB2DFDB},
    {"id": "keyifsiz", "label": "Keyifsiz 😑", "renk": 0xFFBCAAA4},
    {"id": "sabirsiz", "label": "Sabırsız ⏳", "renk": 0xFFFFCC80},
    {"id": "utangac", "label": "Utangaç 😳", "renk": 0xFFF48FB1},
    {"id": "gururlu", "label": "Gururlu 😎", "renk": 0xFF9FA8DA},
    {"id": "tedirgin", "label": "Tedirgin 😰", "renk": 0xFFFFAB91},
    {"id": "cesur", "label": "Cesur 🦁", "renk": 0xFFD4E157},
    {"id": "kararsiz", "label": "Kararsız 🤔", "renk": 0xFFB0BEC5},
  ];

  Future<void> oneriyiGetir(Map<String, dynamic> duygu) async {
    setState(() {
      yukleniyor = true;
      secimYapildi = true;
      secilenDuyguYazi = duygu["label"].split(" ")[0];
      secilenDuyguIcon = duygu["label"].split(" ")[1];
      secilenDuyguRenk = Color(duygu["renk"]);
    });

    try {
      final url = Uri.parse('https://food4mood-api.onrender.com/oner?mood=${duygu["id"]}');
      final cevap = await http.get(url);
      if (cevap.statusCode == 200) {
        final veri = json.decode(utf8.decode(cevap.bodyBytes));
        setState(() {
          tavsiye = "🧪 İhtiyacın: ${veri['nutrient']}\n\n🍎 Öneriler: ${veri['foods'].join(', ')}\n\n📝 Tarifler:\n${veri['recipes'].join('\n')}";
        });
      }
    } catch (e) {
      setState(() => tavsiye = "Sunucuya bağlanılamadı.");
    } finally {
      setState(() => yukleniyor = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        // 2. DEĞİŞİKLİK: Uygulamanın üst barında yazacak isim
        title: const Text("Food4Mood", style: TextStyle(fontWeight: FontWeight.bold)),
        centerTitle: true,
        leading: secimYapildi ? IconButton(icon: const Icon(Icons.arrow_back), onPressed: () => setState(() => secimYapildi = false)) : null,
      ),
      body: secimYapildi ? _tarifEkrani() : _duyguSecimEkrani(),
    );
  }

  Widget _duyguSecimEkrani() {
    return SingleChildScrollView(
      child: Column(
        children: [
          const Padding(
            padding: EdgeInsets.symmetric(vertical: 20),
            child: Text("Bugün nasılsın?", style: TextStyle(fontSize: 18, color: Colors.grey)),
          ),
          Wrap(
            spacing: 12, runSpacing: 12,
            alignment: WrapAlignment.center,
            children: duygular.map((duygu) {
              var parcalar = duygu["label"].split(" ");
              return SizedBox(
                width: 105, height: 105,
                child: ElevatedButton(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Color(duygu["renk"]),
                    padding: EdgeInsets.zero,
                    elevation: 3,
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(22)),
                  ),
                  onPressed: () => oneriyiGetir(duygu),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Text(parcalar[1], style: const TextStyle(fontSize: 45)),
                      Text(parcalar[0], style: const TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: Colors.black87)),
                    ],
                  ),
                ),
              );
            }).toList(),
          ),
          const SizedBox(height: 30),
        ],
      ),
    );
  }

  Widget _tarifEkrani() {
    return Padding(
      padding: const EdgeInsets.all(20),
      child: Column(
        children: [
          Expanded(
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(30),
                boxShadow: [BoxShadow(color: secilenDuyguRenk.withOpacity(0.3), blurRadius: 20)],
              ),
              child: yukleniyor 
                ? const Center(child: CircularProgressIndicator()) 
                : SingleChildScrollView(
                    child: Column(
                      children: [
                        Text(secilenDuyguIcon, style: const TextStyle(fontSize: 70)),
                        Text(secilenDuyguYazi, style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: secilenDuyguRenk)),
                        const Divider(height: 40),
                        Text(tavsiye, style: const TextStyle(fontSize: 16, height: 1.6)),
                      ],
                    ),
                  ),
            ),
          ),
          const SizedBox(height: 20),
          ElevatedButton(
            onPressed: () => setState(() => secimYapildi = false),
            style: ElevatedButton.styleFrom(backgroundColor: secilenDuyguRenk, foregroundColor: Colors.white),
            child: const Text("Geri Dön"),
          ),
        ],
      ),
    );
  }
}