# CV-HTML - Oleh Mykhasiv's Personal Website

This project contains my personal CV website with two deployment options: **GitHub Pages** (static) and **Flask** (dynamic).

## Project Structure
```
CV-HTML/
├── flask/           # Flask application files
│   ├── app.py       # Flask application with routes
│   ├── index.html   # Dynamic HTML template
│   ├── requirements.txt
│   ├── run_windows.bat
│   └── run_linux.sh
├── badges/          # 17 certification badges (shared)
├── certificates/    # 17 certificate PDFs (shared)
├── icons/           # Favicon (shared)
├── index.html       # Static version for GitHub Pages
├── OlehMykhasiv-CV.pdf  # CV file (shared)
├── README.md        # This file
└── README-GitHub-Pages.md  # Detailed GitHub Pages guide
```

## Quick Start

### Option 1: GitHub Pages (Recommended for hosting)
- **URL**: `https://olegmar1.github.io`
- **Setup**: Follow instructions in `README-GitHub-Pages.md`
- **Benefits**: Free hosting, SSL, CDN, automatic deployment

### Option 2: Flask (For local development/testing)
- **URL**: `http://localhost:5000`
- **Requirements**: Python 3.7+, pip

#### Using the provided scripts:

**Windows:**
```bash
cd flask
run_windows.bat
```

**Linux/macOS:**
```bash
cd flask
chmod +x run_linux.sh
./run_linux.sh
```

#### Manual setup:
```bash
cd flask
pip install -r requirements.txt
python app.py
```

## Features

### Shared Features (Both Versions)
- ✅ Professional dark theme design
- ✅ **17 cloud and technology certifications** with clickable badges
- ✅ **Interactive certification badges** - Click to view PDF certificates
- ✅ **CV download and preview** functionality
- ✅ **Responsive design** (mobile-friendly)
- ✅ **Contact links** (LinkedIn, GitHub, Telegram)
- ✅ **Hover effects** and smooth animations
- ✅ **Custom favicon** for professional appearance

### Flask Version Extras
- ✅ **Dynamic content rendering** with server-side processing
- ✅ **Custom CV page** with embedded PDF viewer
- ✅ **Server-side file serving** for badges and certificates
- ✅ **Easy local development** and testing
- ✅ **Extensible architecture** for future enhancements

### GitHub Pages Version Extras
- ✅ **Free hosting** with SSL certificate
- ✅ **Global CDN** for fast loading worldwide
- ✅ **Automatic deployment** from Git repository
- ✅ **Custom domain support**
- ✅ **Direct PDF opening** in new window

## Certifications (17 Total)

### Cloud Platforms
- **AWS (6)**: DevOps Engineer Professional, SysOps Administrator Associate, Solutions Architect Associate, Data Analytics Specialty, Security Specialty, AI Practitioner
- **Microsoft Azure (1)**: Data Fundamentals
- **Oracle Cloud (2)**: Data Management Foundations, Infrastructure Foundations

### Infrastructure & Tools
- **HashiCorp (1)**: Terraform Associate

### Data & AI
- **Databricks (5)**: Fundamentals, Lakehouse Fundamentals, Platform Administrator, Generative AI Fundamentals, AI Security Fundamentals

### Programming
- **Python (2)**: PCEP Entry-Level, PCAP Associate

## Static Files
- **Badge images**: 17 certification badges served from `/badges/` URL path
- **Certificate PDFs**: 17 downloadable certificates served from `/certificates/` URL path
- **CV PDF**: Available for download and preview
- **Favicon**: Custom icon for browser tabs

## Technologies Used
- **Frontend**: HTML5, CSS3, Bootstrap 5, Bootstrap Icons
- **Backend**: Python Flask (optional)
- **Hosting**: GitHub Pages (static) / Any Python server (Flask)
- **File Formats**: PNG (badges), PDF (certificates, CV)

## Deployment

### GitHub Pages
1. Create repository: `olegmar1.github.io`
2. Upload static files (root directory files)
3. Enable GitHub Pages in repository settings
4. Site available at: `https://olegmar1.github.io`

### Flask (Production)
- **Heroku**: Easy deployment with Git
- **Railway**: Simple Python app hosting
- **AWS EC2**: Full control, ~$3-10/month
- **DigitalOcean**: Managed droplets

## Development

### Adding New Certifications
1. Add badge image to `badges/` folder
2. Add certificate PDF to `certificates/` folder
3. Update both `index.html` (static) and `flask/index.html` (dynamic)
4. Commit and push for automatic deployment

### Customizing Design
- Modify CSS in the `<style>` sections
- Update Bootstrap classes for layout changes
- Add new sections as needed

## User Experience

### Static Version (GitHub Pages)
- **CV Button**: Opens PDF directly in new window with download option
- **Certification Badges**: Click to open PDF certificates in new tab
- **Hover Effects**: Badges scale up and show tooltips

### Flask Version
- **CV Button**: Opens custom page with embedded PDF viewer
- **Certification Badges**: Click to open PDF certificates in new tab
- **Back Navigation**: "Back to Home" button on CV page

## Notes
- **Shared resources**: Static files (badges, certificates, icons, CV) are shared between both versions
- **No duplication**: Flask app serves files from parent directory to avoid file duplication
- **Consistent experience**: Both versions maintain identical functionality and appearance
- **Easy switching**: Simple to switch between static and dynamic hosting as needed
- **All certifications clickable**: Every badge links to its corresponding PDF certificate 