import os
import shutil
import glob
import re

# 1. Copy Images
src_dir = r"C:\Users\shani\.gemini\antigravity\brain\13681cc9-a179-430d-a97c-38946266a37a"
dest_dir = r"C:\Data\Wardrobe\images"
os.makedirs(dest_dir, exist_ok=True)

image_mapping = {
    "spinning_shirt_*.png": "shirt.png",
    "outfit_casual_*.png": "casual.png",
    "outfit_work_*.png": "work.png",
    "outfit_evening_*.png": "evening.png",
    "outfit_weekend_*.png": "weekend.png"
}

for pattern, dest_name in image_mapping.items():
    files = glob.glob(os.path.join(src_dir, pattern))
    if files:
        shutil.copy(files[0], os.path.join(dest_dir, dest_name))

# 2. Duplicate HTML
base_html_path = r"C:\Data\Wardrobe\StyleIQ_v3_4.html"
final_html_path = r"C:\Data\Wardrobe\StyleIQ_final.html"

with open(base_html_path, "r", encoding="utf-8") as f:
    html = f.read()

# 3. Replacements

# Team members
html = html.replace('Nour Al-Sayed', 'Usman Wajid')
html = html.replace('<div class="t-initials">NA</div>', '<div class="t-initials">UW</div>')

html = html.replace('Rayan Idris', 'Ahmad Masood')
html = html.replace('<div class="t-initials">RI</div>', '<div class="t-initials">AM</div>')

html = html.replace('Sophie Brennan', 'Abdulrehman')
html = html.replace('<div class="t-initials">SB</div>', '<div class="t-initials">AR</div>')

mw_card = '<div class="t-card reveal-up" style="--d:.3s"><div class="t-top" style="background:linear-gradient(135deg,#7c2d12,#c2410c)"><div class="t-initials">MW</div></div><div class="t-body"><div class="t-name">Marcus Wei</div><div class="t-role">CFO &amp; Marketing</div><div class="t-bio">CFA and former fintech CMO. Drives growth strategy and brand partnerships.</div></div></div>'
html = html.replace(mw_card, '')

# Update Address
html = html.replace('Dubai, UAE', 'Lahore, Pakistan')

# Provide missing Feature 1 context in big card if needed (already exists as 01)
# Add Feature 7
feat_6 = '<div class="feat-cell reveal-up" style="--d:.40s"><div class="feat-num">06</div><div class="feat-icon-wrap">🛍️</div><h3>Smart Shopping</h3><p>StyleIQ spots the one missing piece that unlocks 20 new outfit combos and links you directly to it from your favourite stores.</p><span class="feat-pill">Affiliate Shopping</span></div>'
feat_7 = '<div class="feat-cell reveal-up" style="--d:.48s"><div class="feat-num">07</div><div class="feat-icon-wrap">🔄</div><h3>Smart Sync</h3><p>Automatically sync your outfits with your Google/Apple Calendar. Always be prepared for what\'s next.</p><span class="feat-pill">Calendar Integration</span></div>'
html = html.replace(feat_6, feat_6 + '\n      ' + feat_7)

# Make sure Team grid css is updated for 3 members, replace grid-template-columns:repeat(4,1fr) with 3
html = html.replace('.team-row{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;max-width:1200px;margin:0 auto 48px}', '.team-row{display:grid;grid-template-columns:repeat(3,1fr);gap:20px;max-width:1200px;margin:0 auto 48px; justify-content:center;}')

# Replace Shirt SVG with img
shirt_svg_pattern = r'<svg id="shirt-svg".*?</svg>'
shirt_img = r'<img id="shirt-svg" src="images/shirt.png" style="width:300px; height:300px; object-fit:contain; filter:drop-shadow(0 20px 40px rgba(13,92,58,.2)); position:relative; z-index:2; will-change:transform;" alt="Spinning Shirt">'
html = re.sub(shirt_svg_pattern, shirt_img, html, flags=re.DOTALL)

# Replace Lookbook SVGs/Images with the new PNGs
html = html.replace('<!-- !! <img src="outfit1.png"> -->👗', '<img src="images/casual.png" style="width:100%; height:100%; object-fit:cover;">')
html = html.replace('<!-- !! <img src="outfit2.png"> -->👔', '<img src="images/work.png" style="width:100%; height:100%; object-fit:cover;">')
html = html.replace('<!-- !! <img src="outfit3.png"> -->🧥', '<img src="images/evening.png" style="width:100%; height:100%; object-fit:cover;">')
html = html.replace('<!-- !! <img src="outfit4.png"> -->👖', '<img src="images/weekend.png" style="width:100%; height:100%; object-fit:cover;">')

# Replace clothesline items with our PNGs too since they look cooler
clothes_svg1 = r'<svg viewBox="0 0 100 120" xmlns="http://www.w3.org/2000/svg"><path d="M30 20L10 40L25 48L28 35L28 100L72 100L72 35L75 48L90 40L70 20C62 14 38 14 30 20Z" fill="#1d4ed8"/><path d="M38 20Q50 30 62 20Q56 12 50 12Q44 12 38 20Z" fill="#1e3a5f"/><circle cx="50" cy="55" r="2" fill="rgba(255,255,255,.5)"/><circle cx="50" cy="65" r="2" fill="rgba(255,255,255,.5)"/></svg>'
html = html.replace(clothes_svg1, '<img src="images/shirt.png" style="width:100px; height:auto; object-fit:contain; filter:drop-shadow(0 4px 6px rgba(0,0,0,0.1));">')

with open(final_html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("done")
