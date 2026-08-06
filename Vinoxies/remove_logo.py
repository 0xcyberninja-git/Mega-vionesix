import os
import glob
import re

directory = '/home/prateek/Vinoxies/'
html_files = glob.glob(os.path.join(directory, '*.html'))
html_files = [f for f in html_files if 'index-v' not in f and 'vionexis_intelligence_website' not in f]

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Remove navbar logo block
    content = re.sub(
        r'<div[^>]*class="[^"]*w-10 h-10[^"]*group-hover:rotate-12[^"]*"[^>]*>.*?<img src="Black White Modern Letter AG Logo\.png"[^>]*>.*?</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # Remove footer logo block (slightly different classes)
    content = re.sub(
        r'<div class="w-10 h-10 flex-shrink-0 bg-white/10 p-1 rounded-xl flex items-center justify-center">\s*<img src="Black White Modern Letter AG Logo\.png"[^>]*>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w') as f:
        f.write(content)

print("Logos removed successfully.")
