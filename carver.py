import sys
import os

# Dosya İmzaları (Magic Bytes)
SIGNATURES = {
    "JPEG": {
        "header": b"\xFF\xD8\xFF",
        "footer": b"\xFF\xD9"
    },
    "PNG": {
        "header": b"\x89PNG\r\n\x1a\n",
        "footer": b"IEND\xaeB`\x82"
    }
}

def carve_files(raw_image_path, output_dir="carved_output"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    print(f"[*] Adli İmaj Taranıyor: {raw_image_path}")
    
    with open(raw_image_path, "rb") as f:
        data = f.read()

    carved_count = 0

    for file_type, sigs in SIGNATURES.items():
        header = sigs["header"]
        footer = sigs["footer"]
        start_idx = 0

        while True:
            start_pos = data.find(header, start_idx)
            if start_pos == -1:
                break

            end_pos = data.find(footer, start_pos)
            if end_pos != -1:
                end_pos += len(footer)
                carved_data = data[start_pos:end_pos]

                ext = file_type.lower()
                out_filename = os.path.join(output_dir, f"recovered_{carved_count}.{ext}")
                with open(out_filename, "wb") as out_f:
                    out_f.write(carved_data)

                print(f"[+] {file_type} tespit edildi ve kurtarıldı: Ofset 0x{start_pos:X} -> {out_filename}")
                carved_count += 1
                start_idx = end_pos
            else:
                start_idx = start_pos + len(header)

    print(f"\n[!] İşlem tamamlandı. Toplam {carved_count} dosya kurtarıldı.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Kullanım: python carver.py <ham_imaj_dosyasi>")
    else:
        carve_files(sys.argv[1])
