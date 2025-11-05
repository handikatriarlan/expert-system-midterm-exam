from datetime import datetime
from typing import Set, List, Dict, Tuple


class KnowledgeBase:
    """Class untuk menyimpan basis pengetahuan sistem pakar"""
    
    def __init__(self):
        # --- Definisi Rules dengan informasi tambahan ---
        self.rules = [
            {
                "id": "R1",
                "if": {"Pembersih dengan Salicylic Acid", "Spot Treatment dengan Benzoyl Peroxide"},
                "then": "Jerawat",
                "confidence": 0.95,
                "explanation": "Kombinasi Salicylic Acid dan Benzoyl Peroxide adalah penanganan khas untuk jerawat aktif",
                "recommendation": "Gunakan pembersih 2x sehari, spot treatment pada area berjerawat"
            },
            {
                "id": "R2",
                "if": {"Flek Hitam", "Bintik Putih"},
                "then": "Pigmentasi Karena Hormon",
                "confidence": 0.85,
                "explanation": "Kombinasi flek hitam dan bintik putih mengindikasikan ketidakseimbangan pigmentasi hormonal",
                "recommendation": "Konsultasi dengan dokter kulit, pertimbangkan perawatan hormon"
            },
            {
                "id": "R3",
                "if": {"Pembersih dengan Salicylic Acid", "Spot Treatment dengan Benzoyl Peroxide"},
                "then": "Bekas Jerawat",
                "confidence": 0.90,
                "explanation": "Perawatan ini juga efektif untuk mengatasi bekas jerawat dan hiperpigmentasi pasca-jerawat",
                "recommendation": "Tambahkan vitamin C serum dan gunakan sunscreen SPF 30+"
            },
            {
                "id": "R4",
                "if": {"Pori-pori Besar", "Kulit Kusam", "Kulit Reda"},
                "then": "Kulit Terkontaminasi Debu",
                "confidence": 0.88,
                "explanation": "Pori-pori besar dengan kulit kusam dan reda menunjukkan paparan debu berlebihan",
                "recommendation": "Deep cleansing rutin, gunakan clay mask 2x seminggu, tingkatkan hidrasi"
            },
            {
                "id": "R5",
                "if": {"Pembersih dengan Salicylic Acid", "Spot Treatment"},
                "then": "Kulit Terbakar Matahari",
                "confidence": 0.80,
                "explanation": "Perawatan dengan asam ringan membantu regenerasi kulit yang terbakar matahari",
                "recommendation": "Hindari paparan sinar matahari langsung, gunakan aloe vera gel, sunscreen wajib"
            },
        ]
        
        # --- Definisi gejala yang tersedia ---
        self.available_symptoms = {
            "Pembersih dengan Salicylic Acid",
            "Spot Treatment dengan Benzoyl Peroxide",
            "Spot Treatment",
            "Flek Hitam",
            "Bintik Putih",
            "Pori-pori Besar",
            "Kulit Kusam",
            "Kulit Reda",
            "Gatal-gatal"
        }


class InferenceEngine:
    """Class untuk menjalankan mekanisme inferensi forward chaining"""
    
    def __init__(self, knowledge_base: KnowledgeBase):
        self.kb = knowledge_base
        self.trace = []  # Menyimpan jejak inferensi
        
    def forward_chaining(self, initial_facts: Set[str]) -> Tuple[Set[str], List[str], List[Dict]]:
        """
        Melakukan forward chaining dengan pelacakan detail
        
        Args:
            initial_facts: Set fakta awal dari user
            
        Returns:
            Tuple berisi (fakta_akhir, rules_terpicu, detail_trace)
        """
        working_memory = set(initial_facts)  # Working memory
        fired_rules = []  # Rules yang sudah terpicu
        inference_trace = []  # Detail trace untuk setiap iterasi
        
        iteration = 0
        changed = True
        
        while changed:
            changed = False
            iteration += 1
            
            print(f"\n{'='*60}")
            print(f"ITERASI {iteration}")
            print(f"{'='*60}")
            print(f"Working Memory: {sorted(working_memory)}")
            
            for rule in self.kb.rules:
                # Skip jika rule sudah pernah terpicu
                if rule["id"] in fired_rules:
                    continue
                
                # Cek apakah semua kondisi terpenuhi
                if rule["if"].issubset(working_memory):
                    conclusion = rule["then"]
                    
                    # Jika kesimpulan belum ada di working memory
                    if conclusion not in working_memory:
                        working_memory.add(conclusion)
                        fired_rules.append(rule["id"])
                        changed = True
                        
                        # Catat trace
                        trace_entry = {
                            "iteration": iteration,
                            "rule_id": rule["id"],
                            "conditions": list(rule["if"]),
                            "conclusion": conclusion,
                            "confidence": rule["confidence"],
                            "explanation": rule["explanation"],
                            "recommendation": rule["recommendation"]
                        }
                        inference_trace.append(trace_entry)
                        
                        print(f"\n✓ Rule {rule['id']} TERPICU!")
                        print(f"  Kondisi: {' AND '.join(sorted(rule['if']))}")
                        print(f"  Kesimpulan: {conclusion}")
                        print(f"  Confidence: {rule['confidence']*100:.1f}%")
                        print(f"  Penjelasan: {rule['explanation']}")
        
        return working_memory, fired_rules, inference_trace
    
    def generate_decision_tree(self, initial_facts: Set[str], fired_rules: List[str]) -> str:
        """Generate representasi pohon keputusan dalam bentuk teks"""
        tree = "\n" + "="*60 + "\n"
        tree += "POHON KEPUTUSAN (DECISION TREE)\n"
        tree += "="*60 + "\n\n"
        tree += "Fakta Awal:\n"
        for fact in sorted(initial_facts):
            tree += f"  └─ {fact}\n"
        tree += "\n"
        
        if not fired_rules:
            tree += "Tidak ada rules yang terpicu.\n"
            return tree
        
        tree += "Proses Inferensi:\n"
        for i, rule_id in enumerate(fired_rules, 1):
            rule = next(r for r in self.kb.rules if r["id"] == rule_id)
            tree += f"\n{i}. Rule {rule_id}:\n"
            tree += f"   IF:\n"
            for condition in sorted(rule["if"]):
                tree += f"     ├─ {condition}\n"
            tree += f"   THEN:\n"
            tree += f"     └─ {rule['then']} (confidence: {rule['confidence']*100:.0f}%)\n"
        
        return tree


class ExpertSystem:
    """Class utama sistem pakar"""
    
    def __init__(self):
        self.kb = KnowledgeBase()
        self.engine = InferenceEngine(self.kb)
        
    def run_with_facts(self, facts: Set[str], show_tree: bool = True):
        """Menjalankan sistem dengan fakta yang diberikan"""
        print("\n" + "="*60)
        print("SISTEM PAKAR DIAGNOSIS KULIT")
        print("Forward Chaining Method")
        print("="*60)
        
        print(f"\nWaktu: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"\nFAKTA AWAL ({len(facts)} fakta):")
        for i, fact in enumerate(sorted(facts), 1):
            print(f"  {i}. {fact}")
        
        # Jalankan forward chaining
        final_facts, fired_rules, trace = self.engine.forward_chaining(facts)
        
        # Tampilkan hasil
        print("\n" + "="*60)
        print("HASIL DIAGNOSIS")
        print("="*60)
        
        if not fired_rules:
            print("\n❌ Tidak ada aturan yang terpenuhi.")
            print("Tidak dapat menentukan diagnosis berdasarkan fakta yang diberikan.")
            print("\nSaran: Tambahkan gejala atau perawatan yang sedang digunakan.")
        else:
            print(f"\n✓ Total {len(fired_rules)} aturan terpicu: {', '.join(fired_rules)}")
            
            # Temukan diagnosis (fakta baru yang ditambahkan)
            diagnoses = final_facts - facts
            
            if diagnoses:
                print(f"\n📋 DIAGNOSIS TERDETEKSI ({len(diagnoses)}):")
                for i, diagnosis in enumerate(sorted(diagnoses), 1):
                    # Cari rule yang menghasilkan diagnosis ini
                    related_rules = [t for t in trace if t["conclusion"] == diagnosis]
                    if related_rules:
                        rule_info = related_rules[-1]  # Ambil yang terakhir
                        print(f"\n{i}. {diagnosis}")
                        print(f"   Confidence: {rule_info['confidence']*100:.1f}%")
                        print(f"   Penjelasan: {rule_info['explanation']}")
                        print(f"   Rekomendasi: {rule_info['recommendation']}")
            
            print(f"\n📊 FAKTA AKHIR ({len(final_facts)} fakta):")
            for fact in sorted(final_facts):
                marker = "🆕" if fact not in facts else "  "
                print(f"  {marker} {fact}")
        
        # Tampilkan pohon keputusan
        if show_tree:
            tree = self.engine.generate_decision_tree(facts, fired_rules)
            print(tree)
        
        return final_facts, fired_rules, trace
    
    def interactive_mode(self):
        """Mode interaktif untuk input dari user"""
        print("\n" + "="*60)
        print("MODE INTERAKTIF - SISTEM PAKAR DIAGNOSIS KULIT")
        print("="*60)
        
        print("\nGejala dan Perawatan yang tersedia:")
        for i, symptom in enumerate(sorted(self.kb.available_symptoms), 1):
            print(f"  {i}. {symptom}")
        
        print("\nMasukkan nomor gejala/perawatan yang dialami (pisahkan dengan koma)")
        print("Contoh: 1,3,5")
        print("Atau ketik 'default' untuk menggunakan contoh kasus")
        
        user_input = input("\nPilihan Anda: ").strip()
        
        if user_input.lower() == 'default':
            facts = {"Kulit Kusam", "Gatal-gatal", "Pori-pori Besar"}
            print("\nMenggunakan fakta default: Kulit Kusam, Gatal-gatal, Pori-pori Besar")
        else:
            try:
                indices = [int(x.strip()) for x in user_input.split(',')]
                symptoms_list = sorted(self.kb.available_symptoms)
                facts = {symptoms_list[i-1] for i in indices if 1 <= i <= len(symptoms_list)}
                
                if not facts:
                    print("\n❌ Tidak ada fakta yang valid dipilih.")
                    return
            except (ValueError, IndexError):
                print("\n❌ Input tidak valid.")
                return
        
        self.run_with_facts(facts)


# --- Main Program ---
if __name__ == "__main__":
    # Inisialisasi sistem pakar
    expert_system = ExpertSystem()
    
    # Contoh penggunaan dengan fakta yang diberikan di soal
    print("\n" + "🔬 DEMO: KASUS DARI SOAL")
    facts = {"Kulit Kusam", "Gatal-gatal", "Pori-pori Besar"}
    expert_system.run_with_facts(facts, show_tree=True)
    
    # Tanya user apakah ingin mencoba kasus lain
    print("\n" + "="*60)
    try_another = input("\nIngin mencoba kasus lain? (y/n): ").strip().lower()
    
    if try_another == 'y':
        expert_system.interactive_mode()
    
    print("\n" + "="*60)
    print("Terima kasih telah menggunakan Sistem Pakar Diagnosis Kulit!")
    print("="*60)
