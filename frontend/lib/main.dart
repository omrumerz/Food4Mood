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
      title: 'Food4Mood', 
      theme: ThemeData(
        useMaterial3: true, 
        colorSchemeSeed: Colors.deepPurple,
        scaffoldBackgroundColor: const Color(0xFFF8F9FA),
      ),
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
  final TextEditingController _controller = TextEditingController();
  bool _loading = false;
  bool secimYapildi = false;
  String secilenDuyguIcon = "";
  String secilenDuyguYazi = "";
  Color secilenDuyguRenk = Colors.deepPurple;
  
  List<dynamic> tarifler = [];
  String ihtiyac = "";

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

  Future<void> analizEt(String metin) async {
    if (metin.isEmpty) return;
    setState(() => _loading = true);
    try {
      final response = await http.get(Uri.parse('https://food4mood-api.onrender.com/analiz?metin=$metin'));
      if (response.statusCode == 200) {
        final data = json.decode(utf8.decode(response.bodyBytes));
        _showResultModal(data);
      }
    } catch (e) {
      debugPrint("Hata: $e");
    } finally {
      setState(() => _loading = false);
    }
  }

  void _showResultModal(Map<String, dynamic> data) {
    showModalBottomSheet(
      context: context,
      isScrollControlled: true,
      shape: const RoundedRectangleBorder(borderRadius: BorderRadius.vertical(top: Radius.circular(25))),
      builder: (context) {
        final info = data['besin_bilgisi'];
        return Padding(
          padding: const EdgeInsets.all(20.0),
          child: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Container(width: 40, height: 4, decoration: BoxDecoration(color: Colors.grey[300], borderRadius: BorderRadius.circular(10))),
              const SizedBox(height: 15),
              Text("Tespit Edilen Mod: ${data['tespit_edilen_duygu'].toUpperCase()}", 
                   style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.orange)),
              const Divider(),
              Text("Önerilen: ${info['foods'].join(', ')}", textAlign: TextAlign.center, style: const TextStyle(fontSize: 16)),
              const SizedBox(height: 15),
              const Text("Tarifler (Detay için tıkla):", style: TextStyle(fontWeight: FontWeight.bold)),
              const SizedBox(height: 10),
              Flexible(
                child: ListView.builder(
                  shrinkWrap: true,
                  itemCount: info['recipes'].length,
                  itemBuilder: (context, index) {
                    final r = info['recipes'][index];
                    return Card(
                      child: ListTile(
                        leading: const Icon(Icons.restaurant, color: Colors.orange),
                        title: Text(r['name']),
                        subtitle: Text("${r['duration']} • ${r['calories']}"),
                        trailing: const Icon(Icons.chevron_right),
                        onTap: () {
                          Navigator.pop(context); // Modalı kapat
                          Navigator.push(context, MaterialPageRoute(builder: (context) => TarifDetaySayfasi(tarif: r)));
                        },
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 20),
            ],
          ),
        );
      },
    );
  }

  Future<void> oneriyiGetir(Map<String, dynamic> duygu) async {
    setState(() {
      _loading = true;
      secimYapildi = true;
      secilenDuyguYazi = duygu["label"].split(" ")[0];
      secilenDuyguIcon = duygu["label"].split(" ")[1];
      secilenDuyguRenk = Color(duygu["renk"]);
    });

    try {
      final response = await http.get(Uri.parse('https://food4mood-api.onrender.com/oner?mood=${duygu["id"]}'));
      if (response.statusCode == 200) {
        final data = json.decode(utf8.decode(response.bodyBytes));
        setState(() {
          ihtiyac = data['nutrient'];
          tarifler = data['recipes'];
        });
      }
    } catch (e) {
      debugPrint("Hata: $e");
    } finally {
      setState(() => _loading = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Food4Mood", style: TextStyle(fontWeight: FontWeight.bold)),
        centerTitle: true,
        elevation: 0,
        backgroundColor: Colors.transparent,
      ),
      body: secimYapildi ? _tarifListesiEkrani() : _duyguSecimEkrani(),
    );
  }

  Widget _duyguSecimEkrani() {
    return SingleChildScrollView(
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
              children: [
                TextField(
                  controller: _controller,
                  decoration: InputDecoration(
                    hintText: "Bugün nasıl hissediyorsun?",
                    prefixIcon: const Icon(Icons.sentiment_satisfied_alt),
                    suffixIcon: IconButton(
                      icon: _loading ? const SizedBox(width: 20, height: 20, child: CircularProgressIndicator(strokeWidth: 2)) : const Icon(Icons.auto_awesome),
                      onPressed: () => analizEt(_controller.text),
                    ),
                    border: OutlineInputBorder(borderRadius: BorderRadius.circular(20), borderSide: BorderSide.none),
                    filled: true, fillColor: Colors.white,
                  ),
                ),
                const SizedBox(height: 20),
                const Text("Veya bir mod seçin", style: TextStyle(fontSize: 16, fontWeight: FontWeight.w600, color: Colors.grey)),
              ],
            ),
          ),
          Wrap(
            spacing: 12, runSpacing: 12, alignment: WrapAlignment.center,
            children: duygular.map((duygu) => SizedBox(
              width: 105, height: 105,
              child: ElevatedButton(
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(duygu["renk"]),
                  elevation: 2,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(22)),
                  padding: EdgeInsets.zero,
                ),
                onPressed: () => oneriyiGetir(duygu),
                child: Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Text(duygu["label"].split(" ")[1], style: const TextStyle(fontSize: 40)),
                    const SizedBox(height: 4),
                    Text(duygu["label"].split(" ")[0], style: const TextStyle(fontSize: 11, color: Colors.black87, fontWeight: FontWeight.bold)),
                  ],
                ),
              ),
            )).toList(),
          ),
          const SizedBox(height: 30),
        ],
      ),
    );
  }

  Widget _tarifListesiEkrani() {
    return Padding(
      padding: const EdgeInsets.all(20),
      child: Column(
        children: [
          Text(secilenDuyguIcon, style: const TextStyle(fontSize: 60)),
          Text(secilenDuyguYazi, style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: secilenDuyguRenk)),
          Text("🔬 İhtiyacın: $ihtiyac", style: const TextStyle(fontStyle: FontStyle.italic, color: Colors.blueGrey)),
          const Divider(height: 40),
          Expanded(
            child: _loading 
              ? const Center(child: CircularProgressIndicator())
              : ListView.builder(
                  itemCount: tarifler.length,
                  itemBuilder: (context, index) {
                    final t = tarifler[index];
                    return Card(
                      elevation: 2,
                      margin: const EdgeInsets.only(bottom: 12),
                      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                      child: ListTile(
                        contentPadding: const EdgeInsets.symmetric(horizontal: 20, vertical: 8),
                        leading: const CircleAvatar(backgroundColor: Colors.orangeAccent, child: Icon(Icons.restaurant_menu, color: Colors.white)),
                        title: Text(t['name'], style: const TextStyle(fontWeight: FontWeight.bold)),
                        subtitle: Text("${t['duration']} | ${t['calories']}"),
                        trailing: const Icon(Icons.arrow_forward_ios, size: 16),
                        onTap: () => Navigator.push(context, MaterialPageRoute(builder: (context) => TarifDetaySayfasi(tarif: t))),
                      ),
                    );
                  },
                ),
          ),
          const SizedBox(height: 10),
          TextButton.icon(
            onPressed: () => setState(() => secimYapildi = false), 
            icon: const Icon(Icons.refresh),
            label: const Text("Modumu Değiştir"),
          ),
        ],
      ),
    );
  }
}

class TarifDetaySayfasi extends StatelessWidget {
  final Map<String, dynamic> tarif;
  const TarifDetaySayfasi({super.key, required this.tarif});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(tarif['name']), centerTitle: true),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(24),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                _infoChip(Icons.access_time_rounded, "Süre", tarif['duration'], Colors.blue),
                _infoChip(Icons.local_fire_department_rounded, "Enerji", tarif['calories'], Colors.orange),
              ],
            ),
            const SizedBox(height: 35),
            const Row(
              children: [
                Icon(Icons.menu_book_rounded, color: Colors.deepPurple),
                SizedBox(width: 10),
                Text("Nasıl Hazırlanır?", style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
              ],
            ),
            const Divider(height: 30),
            Container(
              padding: const EdgeInsets.all(20),
              decoration: BoxDecoration(
                color: Colors.white,
                borderRadius: BorderRadius.circular(20),
                boxShadow: [BoxShadow(color: Colors.black.withOpacity(0.05), blurRadius: 10)],
              ),
              child: Text(
                tarif['steps'], 
                style: const TextStyle(fontSize: 16, height: 1.7, color: Colors.black87),
              ),
            ),
            const SizedBox(height: 40),
            SizedBox(
              width: double.infinity,
              height: 55,
              child: ElevatedButton.icon(
                onPressed: () => Navigator.pop(context),
                icon: const Icon(Icons.check_circle_outline),
                label: const Text("Tarifi Tamamladım!", style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.green[600],
                  foregroundColor: Colors.white,
                  shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget _infoChip(IconData icon, String label, String value, Color color) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 25, vertical: 15),
      decoration: BoxDecoration(
        color: color.withOpacity(0.1),
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: color.withOpacity(0.2)),
      ),
      child: Column(
        children: [
          Icon(icon, color: color, size: 28),
          const SizedBox(height: 4),
          Text(label, style: TextStyle(fontSize: 12, color: Colors.grey[600])),
          Text(value, style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
        ],
      ),
    );
  }
}