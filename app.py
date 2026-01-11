from flask import Flask, render_template, request, send_from_directory, abort
import os
from ir_program import IREngine

# ! Konfigurasi Flask
app = Flask(__name__, template_folder='view') 
app.config['PDF_FOLDER'] = 'dataset_pdf'

# ! Init Engine (Global)
metadata_file = 'metadata_final.csv'
if not os.path.exists(metadata_file):
    print(f"[ERROR] File {metadata_file} tidak ditemukan. Pastikan ekstraksi teks sudah dijalankan!")
    engine = None
else:
    print("[INFO] Memuat engine IR...")
    engine = IREngine(metadata_file)
    engine.build_inverted_index()
    engine.prepare_search()
    print("[INFO] Engine siap!")

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', results=None)

@app.route('/search', methods=['POST'])
def search():
    if not engine:
        return "Internal Server Error: Engine not loaded.", 500
    
    query = request.form.get('query', '')
    if not query:
        return render_template('index.html', results=None)

    # ! Lakukan pencarian
    search_results = engine.search(query, top_n=3)
    
    # ! Format hasil untuk view
    formatted_results = []
    for doc_id, score in search_results:
        row = engine.df.iloc[doc_id]
        summary = engine.generate_summary(doc_id)
        
        formatted_results.append({
            'doc_id': doc_id,
            'score': score,
            'title': row['title'],
            'url': row['url'],
            'filename': row['filename'], 
            'summary': summary
        })

    return render_template('index.html', results=formatted_results, query=query)

@app.route('/download/<filename>')
def download_file(filename):
    try:
        return send_from_directory(app.config['PDF_FOLDER'], filename, as_attachment=True)
    except FileNotFoundError:
        abort(404)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
