import asyncio
from pyppeteer import launch
import os
import pandas as pd 

async def load_links(file_path):
    with open(file_path, 'r') as f:
        links = [line.strip() for line in f if line.strip()]
    return links

async def web_to_pdf(links, output_folder="dataset_pdf"):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    metadata_file = 'metadata.csv'
    existing_urls = set()
    metadata_list = []

    if os.path.exists(metadata_file):
        try:
            df_existing = pd.read_csv(metadata_file)
            metadata_list = df_existing.to_dict('records')
            existing_urls = set(df_existing['url'].tolist())
            print(f"[INFO] Ditemukan {len(existing_urls)} dokumen lama di metadata.")
        except Exception as e:
            print(f"[WARNING] Gagal membaca metadata lama, memulai dari nol: {e}")

    browser = await launch({
        'headless': True,
        'executablePath': 'C:/Program Files/Google/Chrome/Application/chrome.exe', 
        'args': ['--no-sandbox', '--disable-setuid-sandbox']
    })
    
    page = await browser.newPage()
    await page.setUserAgent('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36')

    bad_keywords = ["404", "not found", "page is gone","access denied", "page not found"]

    for i, url in enumerate(links):
        if url in existing_urls:
            print(f"[{i+1}/{len(links)}] Skip: URL sudah ada di korpus -> {url}")
            continue

        try:
            print(f"[{i+1}/{len(links)}] Mengecek: {url}")
            response = await page.goto(url, {'waitUntil': 'networkidle2', 'timeout': 90000})
            
            if response.status >= 400:
                print(f"!!! Skip: HTTP Status {response.status} pada {url}")
                continue

            title = await page.title()
            if any(word in title.lower() for word in bad_keywords):
                print(f"!!! Skip: Judul terdeteksi error ('{title}') pada {url}")
                continue
            
            new_id = len(metadata_list) + 1
            filename = f"dokumen_{new_id}.pdf"
            path = os.path.join(output_folder, filename)
            
            await page.pdf({
                'path': path,
                'format': 'A4',
                'printBackground': True
            })

            metadata_list.append({
                'doc_id': new_id,
                'title': title,
                'url': url,
                'filename': filename
            })

            print(f"+++ Sukses disimpan: {path} | Judul: {title}")
            await asyncio.sleep(1) 
        except Exception as e:
            print(f"Gagal memproses {url}: {e}")

    await browser.close()

    if metadata_list:
        df = pd.DataFrame(metadata_list)
        df.to_csv(metadata_file, index=False)
        print(f"\n[INFO] Koleksi diperbarui. Total: {len(metadata_list)} dokumen valid di 'metadata.csv'.")

async def main():
    link_file = 'link_document.txt' 
    if not os.path.exists(link_file):
        print(f"[ERROR] File {link_file} tidak ditemukan!")
        return
    urls = await load_links(link_file)
    await web_to_pdf(urls)

if __name__ == "__main__":
    asyncio.run(main())