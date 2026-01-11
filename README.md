# Error Solution Finder (Sistem Information Retrieval)

![Project Banner](https://via.placeholder.com/1200x400?text=Error+Solution+Finder)

Aplikasi pencarian solusi error pemrograman berbasis web yang menggunakan **Semantic Search** (Word Embedding & Cosine Similarity) untuk menemukan dokumen relevan dari korpus solusi error.

---

## 🇮🇩 Bahasa Indonesia

### Deskripsi
Proyek ini adalah sistem Information Retrieval (IR) yang dimodifikasi menjadi aplikasi web menggunakan **Flask** dan **TailwindCSS**. Sistem ini dirancang untuk membantu developer mencari solusi dari berbagai pesan error pemrograman (seperti Java, Python, C++, dll) dengan menggunakan pemrosesan bahasa alami (NLP).

### Fitur Utama
- **Pencarian Semantik**: Menggunakan model `sentence-transformers` untuk memahami makna query, bukan hanya pencocokan kata kunci.
- **Antarmuka Premium**: Desain modern dengan **Dark Mode** menggunakan TailwindCSS.
- **Ringkasan Otomatis**: Menampilkan ringkasan solusi error langsung di kartu hasil.
- **Download PDF**: Akses langsung ke dokumen sumber (PDF) dari hasil pencarian.
- **Skor Relevansi**: Menampilkan tingkat kemiripan (Similarity Score) antara query dan dokumen.

### Teknologi
- **Backend**: Python, Flask, Pandas, NLTK, Sentence-Transformers (BERT).
- **Frontend**: HTML5, TailwindCSS (CDN), Jinja2.
- **Data**: Korpus 40 dokumen PDF tentang error pemrograman.

### Cara Menjalankan
1.  Clone repositori ini.
2.  Install dependensi:
    ```bash
    pip install -r requirement.txt
    ```
3.  Jalankan aplikasi:
    ```bash
    python app.py
    ```
4.  Buka browser di `http://localhost:5000`.

---

## en English

### Description
This project is an Information Retrieval (IR) system transformed into a web application using **Flask** and **TailwindCSS**. It is designed to help developers find solutions to various programming error messages (e.g., Java, Python, C++) using Natural Language Processing (NLP).

### Key Features
- **Semantic Search**: Uses `sentence-transformers` models to understand query meaning, enabling finding results beyond exact keyword matches.
- **Premium UI**: Modern **Dark Mode** design built with TailwindCSS.
- **Auto Summary**: Displays specific error solution summaries directly on result cards.
- **PDF Download**: Direct access to source documents (PDFs) from search results.
- **Relevance Scoring**: Shows the Similarity Score between the user query and the documents.

### Tech Stack
- **Backend**: Python, Flask, Pandas, NLTK, Sentence-Transformers (BERT).
- **Frontend**: HTML5, TailwindCSS (CDN), Jinja2.
- **Data**: Corpus of 40 PDF documents regarding programming errors.

### How to Run
1.  Clone this repository.
2.  Install dependencies:
    ```bash
    pip install -r requirement.txt
    ```
3.  Run the application:
    ```bash
    python app.py
    ```
4.  Open your browser at `http://localhost:5000`.

---

## 🇯🇵 日本語

### 概要
このプロジェクトは、**Flask** と **TailwindCSS** を使用してWebアプリケーション化された情報検索（IR）システムです。自然言語処理（NLP）を活用し、開発者が様々なプログラミングエラー（Java、Python、C++など）の解決策を効率的に検索できるように設計されています。

### 主な機能
- **セマンティック検索**: `sentence-transformers` モデルを使用し、単なるキーワード一致ではなく、検索クエリの意味を理解して結果を表示します。
- **プレミアムUI**: TailwindCSSを使用したモダンな**ダークモード**デザイン。
- **自動要約**: エラー解決策の要約を結果カードに直接表示します。
- **PDFダウンロード**: 検索結果からソースドキュメント（PDF）へ直接アクセス可能です。
- **関連性スコア**: ユーザーのクエリとドキュメント間の類似度スコアを表示します。

### 使用技術
- **バックエンド**: Python, Flask, Pandas, NLTK, Sentence-Transformers (BERT).
- **フロントエンド**: HTML5, TailwindCSS (CDN), Jinja2.
- **データ**: プログラミングエラーに関する40のPDFドキュメントコーパス。

### 実行方法
1.  このリポジトリをクローンします。
2.  依存関係をインストールします：
    ```bash
    pip install -r requirement.txt
    ```
3.  アプリケーションを実行します：
    ```bash
    python app.py
    ```
4.  ブラウザで `http://localhost:5000` を開きます。
