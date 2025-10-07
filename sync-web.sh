#!/bin/bash
# LegalGapDB - Sync Root to Web Directory for GitHub Pages
# This script ensures all HTML/CSS/JS files are available in web/ for GitHub Pages deployment

echo "🔄 LegalGapDB Web Sync Script"
echo "================================"

# Create web directory structure if it doesn't exist
mkdir -p web/css web/js

# Copy all HTML files from root to web/
echo "📄 Syncing HTML files..."
for file in *.html; do
    if [ -f "$file" ]; then
        cp "$file" web/
        echo "✅ Copied $file"
    fi
done

# Copy CSS files
echo "🎨 Syncing CSS files..."
if [ -d "css" ]; then
    cp css/* web/css/ 2>/dev/null
    echo "✅ Copied CSS files"
fi

# Copy JS files (but preserve existing web/js/main.js if different)
echo "⚙️ Syncing JS files..."
if [ -d "js" ]; then
    # Check if root js/main.js is newer than web/js/main.js
    if [ js/main.js -nt web/js/main.js ] 2>/dev/null || [ ! -f web/js/main.js ]; then
        cp js/* web/js/ 2>/dev/null
        echo "✅ Updated JS files"
    else
        echo "ℹ️ JS files already up to date"
    fi
fi

# Verify all files are in place
echo ""
echo "📋 Verification:"
echo "Root HTML files: $(ls -1 *.html 2>/dev/null | wc -l)"
echo "Web HTML files:  $(ls -1 web/*.html 2>/dev/null | wc -l)"

# Check for missing files
echo ""
echo "🔍 Missing files check:"
for file in *.html; do
    if [ -f "$file" ] && [ ! -f "web/$file" ]; then
        echo "❌ Missing in web/: $file"
    fi
done

echo ""
echo "✅ Sync completed!"
echo "💡 Run 'git add web/ && git commit -m \"sync: Update web/ directory\"' to commit changes"