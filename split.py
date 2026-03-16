import re
import os

html_path = r"c:\Data\Wardrobe\StyleIQ_final.html"
css_path = r"c:\Data\Wardrobe\style.css"
js_path = r"c:\Data\Wardrobe\script.js"

with open(html_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# Extract CSS
style_match = re.search(r'<style>(.*?)</style>', html_content, re.DOTALL)
if style_match:
    css_content = style_match.group(1).strip()
    with open(css_path, "w", encoding="utf-8") as f:
        f.write(css_content)
    # Replace in HTML
    html_content = html_content[:style_match.start()] + '<link rel="stylesheet" href="style.css"/>' + html_content[style_match.end():]

# Extract JS
# Be careful not to replace the gsap CDN scripts, so match the script block without src
script_match = re.search(r'<script>(.*?)</script>', html_content, re.DOTALL)
if script_match:
    js_content = script_match.group(1).strip()
    with open(js_path, "w", encoding="utf-8") as f:
        f.write(js_content)
    # Replace in HTML
    html_content = html_content[:script_match.start()] + '<script src="script.js"></script>' + html_content[script_match.end():]

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print("Split completed successfully.")
