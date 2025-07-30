# Deploy to GitHub Pages

This guide will help you deploy your CV website to GitHub Pages for free hosting.

## Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right and select "New repository"
3. Name it `your-username.github.io` (replace `your-username` with your actual GitHub username)
4. Make it **Public** (required for free GitHub Pages)
5. Don't initialize with README (we'll upload our files)
6. Click "Create repository"

## Step 2: Upload Files

### Option A: Using Git (Recommended)
```bash
# Clone the repository
git clone https://github.com/your-username/your-username.github.io.git
cd your-username.github.io

# Copy your files to this directory:
# - index-static.html (rename to index.html)
# - cv.html
# - badges/ folder
# - icons/ folder
# - OlehMykhasiv-CV.pdf

# Rename index-static.html to index.html
mv index-static.html index.html

# Add all files
git add .

# Commit
git commit -m "Initial commit - CV website"

# Push
git push origin main
```

### Option B: Using GitHub Web Interface
1. Go to your repository on GitHub
2. Click "Add file" → "Upload files"
3. Drag and drop these files:
   - `index-static.html` (rename to `index.html` in the upload)
   - `cv.html`
   - `badges/` folder
   - `icons/` folder
   - `OlehMykhasiv-CV.pdf`
4. Click "Commit changes"

## Step 3: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click "Settings" tab
3. Scroll down to "Pages" section (in the left sidebar)
4. Under "Source", select "Deploy from a branch"
5. Under "Branch", select "main" and "/ (root)"
6. Click "Save"

## Step 4: Wait for Deployment

- GitHub Pages will take a few minutes to deploy your site
- You'll see a green checkmark when it's ready
- Your site will be available at: `https://your-username.github.io`

## Step 5: Custom Domain (Optional)

If you have a custom domain:
1. In the Pages settings, enter your domain in "Custom domain"
2. Add a `CNAME` file to your repository with your domain name
3. Update your DNS settings with your domain provider

## File Structure for GitHub Pages

Your repository should look like this:
```
your-username.github.io/
├── index.html (renamed from index-static.html)
├── cv.html
├── badges/
│   ├── Microsoft Certified Azure Data Fundamentals - badge.png
│   ├── Oracle Cloud Data Management Foundations Certified Associate badge.png
│   ├── Oracle Cloud Infrastructure Foundations Associate badge.png
│   ├── databricks1.png
│   ├── databricks2.png
│   └── databricks3.png
├── icons/
│   └── favicon.ico
└── OlehMykhasiv-CV.pdf
```

## Troubleshooting

- **Site not showing**: Wait 5-10 minutes for deployment
- **Images not loading**: Check file paths are correct
- **PDF not displaying**: Some browsers block PDF display in iframes
- **404 errors**: Make sure all files are in the root directory

## Benefits of GitHub Pages

✅ **Free hosting**  
✅ **Custom domain support**  
✅ **SSL certificate included**  
✅ **Fast CDN**  
✅ **Version control**  
✅ **Easy updates**

Your CV will be accessible worldwide at `https://your-username.github.io`! 