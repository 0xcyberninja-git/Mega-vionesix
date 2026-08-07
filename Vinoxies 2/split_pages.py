import re
import os

with open('/home/prateek/Vinoxies/vionexis_intelligence_website.html', 'r') as f:
    content = f.read()

# Replace Cybersecurity and Cloud with Data Science and Data Analytics in global text
content = content.replace("AI Research & Cybersecurity", "AI Research & Data Science")
content = content.replace("Intelligence. Security. Transformation.", "Intelligence. Data. Transformation.")
content = content.replace("Cybersecurity", "Data Science")
content = content.replace("Cloud Platforms", "Data Analytics")
content = content.replace("cybersecurity", "data science")
content = content.replace("Security by Design, Cloud Security, Vulnerability Assessment & AI Defense.", "Machine Learning, Statistical Modeling, Deep Learning & Predictive Analysis.")
content = content.replace("Enterprise data platforms, ETL pipelines, and cloud-native architecture.", "Real-time insights, Business Intelligence, Data Warehousing & Visualizations.")

# Specific mentions
content = content.replace('<i data-lucide="shield-check"', '<i data-lucide="bar-chart"')
content = content.replace('<i data-lucide="layers"', '<i data-lucide="pie-chart"')
content = content.replace('<i data-lucide="cloud-cog"', '<i data-lucide="database"')
content = content.replace('<i data-lucide="shield-alert"', '<i data-lucide="line-chart"')

# Replace Software & Cloud with Big Data Engineering
content = content.replace("Software & Cloud", "Big Data Engineering")
content = content.replace("Modern, resilient microservice architectures for cloud reliability.", "Scalable data lakes, stream processing, and distributed systems.")

# Replacements in capabilities bullets
content = content.replace("Vulnerability Assessment", "Predictive Modeling")
content = content.replace("Cloud Security", "Data Mining")
content = content.replace("AI Model Guardrails", "Advanced Analytics")
content = content.replace("DevSecOps Pipelines", "Data Strategy")

# Replace job titles and text
content = content.replace("Cyber Analyst", "Data Scientist")
content = content.replace("Security Engineer", "Data Analyst")
content = content.replace("Cloud Solutions Architect", "Data Engineer")

# Replace navigation links
nav_replacements = {
    'href="#about"': 'href="about.html"',
    'href="#capabilities"': 'href="capabilities.html"',
    'href="#why-us"': 'href="advantage.html"',
    'href="#industries"': 'href="industries.html"',
    'href="#team"': 'href="team.html"',
    'href="#careers"': 'href="careers.html"',
    'href="#contact"': 'href="contact.html"',
    'href="#" class="flex items-center gap-3 group"': 'href="index.html" class="flex items-center gap-3 group"',
    'href="#" class="flex items-center gap-3 group inline-flex"': 'href="index.html" class="flex items-center gap-3 group inline-flex"',
}

for old, new in nav_replacements.items():
    content = content.replace(old, new)

# Find main content using regex
main_match = re.search(r'<main.*?>(.*?)</main>', content, re.DOTALL)
if not main_match:
    print("Could not find main section")
    exit(1)

main_content = main_match.group(1)

# Extract sections
hero_match = re.search(r'(<!-- HERO -->.*?)(?=<!-- MISSION & VISION -->|<!-- OVERVIEW & VISION -->)', main_content, re.DOTALL)
if hero_match:
    hero_html = hero_match.group(1)
else:
    hero_match = re.search(r'(<!-- HERO -->.*?)(?=<!--)', main_content, re.DOTALL)
    hero_html = hero_match.group(1)

section_htmls = {}
section_htmls['index'] = hero_html

sections = ['about', 'capabilities', 'team', 'why-us', 'industries', 'careers', 'contact']

for i, section_id in enumerate(sections):
    pattern = f'(<section id="{section_id}".*?>.*?</section>)'
    match = re.search(pattern, main_content, re.DOTALL)
    if match:
        section_htmls[section_id] = match.group(1)
    else:
        print(f"Could not find section {section_id}")

pages_map = {
    'index': 'index.html',
    'about': 'about.html',
    'capabilities': 'capabilities.html',
    'team': 'team.html',
    'why-us': 'advantage.html',
    'industries': 'industries.html',
    'careers': 'careers.html',
    'contact': 'contact.html'
}

for section_id, filename in pages_map.items():
    page_content = content.replace(main_content, f"\n{section_htmls.get(section_id, '')}\n")
    with open(f'/home/prateek/Vinoxies/{filename}', 'w') as f:
        f.write(page_content)
        
print("Pages generated successfully.")
