import PyPDF2
import os
import pandas as pd

def extract_to_separate_files(metadata_file, pdf_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(metadata_file)
    text_paths = []

    print(f"Mengekstrak {len(df)} dokumen ke file .txt...")

    for index, row in df.iterrows():
        pdf_path = os.path.join(pdf_folder, row['filename'])
        txt_filename = f"dokumen_{row['doc_id']}.txt"
        txt_path = os.path.join(output_folder, txt_filename)
        
        content = ""
        try:
            if os.path.exists(pdf_path):
                with open(pdf_path, 'rb') as f:
                    reader = PyPDF2.PdfReader(f)
                    for page in reader.pages:
                        text = page.extract_text()
                        if text:
                            content += text + "\n"
            
                with open(txt_path, 'w', encoding='utf-8') as f_txt:
                    f_txt.write(content)
                
                text_paths.append(txt_path)
                print(f"OK: {txt_filename}")
            else:
                text_paths.append("FILE_NOT_FOUND")
        except Exception as e:
            text_paths.append("ERROR_EXTRACTING")
            print(f"Gagal di {row['filename']}: {e}")

    df['text_path'] = text_paths
    df.to_csv('metadata_final.csv', index=False)
    print("\nSelesai! Cek folder 'extracted_text' dan file 'metadata_final.csv'")

# Eksekusi
extract_to_separate_files('metadata.csv', 'dataset_pdf', 'extracted_text')