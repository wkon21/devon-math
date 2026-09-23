import os
import re

root_dir = r'c:\Users\wayne\.gemini\antigravity\scratch\devon-math'

# Regex to remove standard theme :root blocks and body blocks
# We'll just remove the whole :root and @media blocks to keep it simple, 
# and body { ... } blocks.
remove_patterns = [
    re.compile(r':root\s*\{.*?\}(?=\s*@media|\s*:root|\s*body|\s*\*)', re.DOTALL),
    re.compile(r'@media\s*\(prefers-color-scheme:\s*dark\)\s*\{.*?:root:not\(\[data-theme=\"light\"\]\)\s*\{.*?\}.*?\}', re.DOTALL),
    re.compile(r':root\[data-theme=\"dark\"\]\s*\{.*?\}', re.DOTALL),
    re.compile(r'body\s*\{.*?\}', re.DOTALL),
]

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(subdir, file)
            
            # calculate relative depth for style.css
            rel_path = os.path.relpath(filepath, root_dir)
            depth = rel_path.count(os.sep)
            
            css_path = 'style.css' if depth == 0 else ('../' * depth) + 'style.css'
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # check if we already processed it
            if 'href="{}"'.format(css_path) in content or 'href="style.css"' in content:
                continue
                
            # Replace Google Fonts link
            content = re.sub(
                r'<link href="https://fonts.googleapis.com/css2\?family=Fraunces[^"]*" rel="stylesheet">',
                '',
                content
            )

            # Clean up styles
            for pattern in remove_patterns:
                content = pattern.sub('', content)
            
            # Prepend link inside <head> or before <style>
            link_tag = f'<link rel="stylesheet" href="{css_path}">\n<style>'
            content = content.replace('<style>', link_tag, 1)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print('Done refactoring all HTML files.')
