import csv
import os

# Ayarlar
FILE_NAME = "favorites.csv"

def run_project():
    if not os.path.exists(FILE_NAME):
        print(f"HATA: '{FILE_NAME}' dosyası bulunamadı! Dosyayı klasöre attığından emin ol.")
        return

    counts = {}
    
    try:
        
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            # Excel'in kafasına göre koyduğu virgül/noktalı virgülü otomatik çözer
            content = file.read(1024)
            file.seek(0)
            dialect = csv.Sniffer().sniff(content)
            reader = csv.DictReader(file, dialect=dialect)
            
            for row in reader:
                # Sütun ismini (language) bul ve temizle
                col_name = next((k for k in row if "language" in k.lower()), None)
                if col_name:
                    lang = row[col_name].strip()
                    if lang:
                        counts[lang] = counts.get(lang, 0) + 1

        
        if not counts:
            print("Dosya okundu ama içinde sayılacak dil bulunamadı.")
            return

        total = sum(counts.values())
        sorted_langs = sorted(counts, key=counts.get, reverse=True)

        print("\n--- PROGRAMMING LANGUAGE POLL REPORT ---")
        with open("report.txt", "w", encoding="utf-8") as out:
            for rank, lang in enumerate(sorted_langs, start=1):
                count = counts[lang]
                perc = (count / total) * 100
                line = f"{rank}. {lang}: {count} students ({perc:.1f}%)\n"
                print(line, end="")
                out.write(line)
        
        print(f"\nİşlem tamam! Toplam {total} kayıt işlendi.")
        print("'report.txt' dosyası klasörüne oluşturuldu.")

    except Exception as e:
        print(f"Bir hata oluştu: {e}")

if __name__ == "__main__":
    run_project()