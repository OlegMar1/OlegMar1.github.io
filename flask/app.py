from flask import Flask, send_from_directory, render_template_string, url_for
import os

app = Flask(__name__)

# Read the HTML file once at startup
with open('index.html', encoding='utf-8') as f:
    INDEX_HTML = f.read()

@app.route('/')
def home():
    return render_template_string(INDEX_HTML)

@app.route('/badges/<path:filename>')
def badges(filename):
    return send_from_directory(os.path.join(app.root_path, '..', 'badges'), filename)

@app.route('/certificates/<path:filename>')
def certificates(filename):
    return send_from_directory(
        os.path.join(app.root_path, '..', 'certificates'), 
        filename, 
        mimetype='application/pdf'
    )

@app.route('/cv')
def view_cv():
    # HTML page with embedded PDF viewer and download button, with fallback message
    return render_template_string('''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>CV - Oleh Mykhasiv</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.5/font/bootstrap-icons.css">
        <style>
            body { background: #1e1e1e; color: #e0e0e0; }
            .container { max-width: 900px; margin: 40px auto; background: #2a2a2a; padding: 30px; border-radius: 10px; }
            .pdf-viewer { width: 100%; height: 80vh; border: none; border-radius: 8px; box-shadow: 0 0 10px #0005; }
            .back-btn { margin-bottom: 20px; }
        </style>
    </head>
    <body>
        <div class="container text-center">
            <a href="{{ url_for('home') }}" class="btn btn-secondary back-btn"><i class="bi bi-arrow-left"></i> Back to Home</a>
            <h1>CV - Oleh Mykhasiv</h1>
            <a href="{{ url_for('download_cv') }}" class="btn btn-info mb-3" download>Download CV</a>
            <iframe class="pdf-viewer" src="{{ url_for('download_cv') }}">
                <p>Your browser does not support PDF viewing. <a href="{{ url_for('download_cv') }}" download>Download the CV here.</a></p>
            </iframe>
        </div>
    </body>
    </html>
    ''')

@app.route('/download-cv')
def download_cv():
    return send_from_directory(
        os.path.join(app.root_path, '..'),
        'OlehMykhasiv-CV.pdf',
        as_attachment=False,  # Display in browser
        mimetype='application/pdf'
    )

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, '..', 'icons'), 'favicon.ico', mimetype='image/x-icon')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000) 