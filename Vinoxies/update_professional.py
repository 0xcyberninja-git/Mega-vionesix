import os
import glob
import re

directory = '/home/prateek/Vinoxies/'
html_files = glob.glob(os.path.join(directory, '*.html'))

# Exclude older versions if they exist
html_files = [f for f in html_files if 'index-v' not in f and 'vionexis_intelligence_website' not in f]

# 1. New Navigation Links
new_desktop_nav = """<nav class="hidden md:flex items-center gap-6 lg:gap-8">
                <a href="about.html" class="nav-link">About Us</a>
                <a href="services.html" class="nav-link">Services</a>
                <a href="capabilities.html" class="nav-link">Capabilities</a>
                <a href="advantage.html" class="nav-link">Advantage</a>
                <a href="industries.html" class="nav-link">Industries</a>
                <a href="team.html" class="nav-link">Team</a>
                <a href="careers.html" class="nav-link">Careers</a>
            </nav>"""

new_mobile_nav = """<div id="mobile-menu" class="fixed inset-0 z-40 bg-black/95 backdrop-blur-xl transition-all duration-300 translate-x-full flex flex-col justify-center items-center gap-6 md:hidden">
        <a href="about.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">About Us</a>
        <a href="services.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">Services</a>
        <a href="capabilities.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">Capabilities</a>
        <a href="advantage.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">Advantage</a>
        <a href="industries.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">Industries</a>
        <a href="team.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">Team</a>
        <a href="careers.html" class="text-2xl font-bold text-white mobile-nav-link hover:text-cyan-400 transition-colors">Careers</a>
        <a href="contact.html" class="mt-8 btn-glow text-sm py-4 px-8 mobile-nav-link"><span>Contact Us</span></a>
    </div>"""

def update_nav(content):
    # Replace desktop nav
    content = re.sub(r'<nav class="hidden md:flex items-center gap-8">.*?</nav>', new_desktop_nav, content, flags=re.DOTALL)
    # Replace mobile nav
    content = re.sub(r'<div id="mobile-menu".*?</div>', new_mobile_nav, content, flags=re.DOTALL)
    return content

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = update_nav(content)
    
    if 'index.html' in filepath:
        # Update Hero Section
        content = re.sub(
            r'<span>AI-First Research & Enterprise Engineering</span>',
            r'<span>Next-Generation AI & Data Science Consultancy</span>',
            content
        )
        content = re.sub(
            r'Research\.\s*Intelligence\.\s*Transformation\.',
            r'Architecting the Data-Driven Future.',
            content
        )
        content = re.sub(
            r'Pioneering the intersection of applied research and enterprise engineering\. We build intelligent, secure, and infinitely scalable solutions for the world\'s most demanding environments\.',
            r'We engineer autonomous AI systems, predictive analytics, and enterprise data architectures to turn complex raw data into profound strategic advantages. We do not just predict the future; we build the intelligence to command it.',
            content
        )
        # Fix the 3 cards in index
        content = re.sub(
            r'<h3 class="text-lg font-bold text-white mb-2">Applied AI</h3>.*?<p class="text-sm text-gray-400">Agentic AI, Generative LLMs, Computer Vision, and Predictive\s*Analytics.</p>',
            r'<h3 class="text-lg font-bold text-white mb-2">Applied AI & LLMs</h3>\n                    <p class="text-sm text-gray-400">Agentic workflows, fine-tuned Generative Models, and cognitive architectures.</p>',
            content, flags=re.DOTALL
        )
        content = re.sub(
            r'<h3 class="text-lg font-bold text-white mb-2">Data Science</h3>.*?<p class="text-sm text-gray-400">Machine Learning, Statistical Modeling, Deep Learning & Predictive Analysis.</p>',
            r'<h3 class="text-lg font-bold text-white mb-2">Data Science</h3>\n                    <p class="text-sm text-gray-400">Advanced machine learning, statistical modeling, and predictive analytics.</p>',
            content, flags=re.DOTALL
        )
        content = re.sub(
            r'<h3 class="text-lg font-bold text-white mb-2">Data Analytics</h3>.*?<p class="text-sm text-gray-400">Real-time insights, Business Intelligence, Data Warehousing & Visualizations.</p>',
            r'<h3 class="text-lg font-bold text-white mb-2">Data Analytics & BI</h3>\n                    <p class="text-sm text-gray-400">Real-time dashboards, big data processing, and actionable business intelligence.</p>',
            content, flags=re.DOTALL
        )

    if 'about.html' in filepath:
        # Update Mission and Vision
        content = re.sub(
            r'<h2 class="text-2xl md:text-3xl font-extrabold text-white mb-6">To define the future through\s*AI-first research and engineering\.</h2>',
            r'<h2 class="text-2xl md:text-3xl font-extrabold text-white mb-6">To architect intelligent enterprise ecosystems by bridging advanced data science with scalable engineering.</h2>',
            content
        )
        content = re.sub(
            r'Designing intelligent technologies that\s*solve complex real-world challenges, fostering continuous innovation and delivering\s*measurable enterprise impact\.',
            r'We transform organizations by deploying cutting-edge machine learning models, predictive analytics, and robust data pipelines that solve humanity\'s most complex challenges while driving measurable, exponential growth.',
            content
        )
        content = re.sub(
            r'<strong class="text-white">Advanced Research:</strong>\s*Bridging the gap between academic theory and practical deployment\.',
            r'<strong class="text-white">Algorithmic Precision:</strong> Designing high-fidelity predictive models tailored for direct enterprise impact.',
            content
        )
        content = re.sub(
            r'<strong class="text-white">Applied\s*Engineering:</strong> Building robust, secure systems designed to scale\s*globally\.',
            r'<strong class="text-white">Data-Centric Engineering:</strong> Building resilient, scalable data infrastructures that serve as the foundation for agentic AI.',
            content
        )
        
        content = re.sub(
            r'<h2 class="text-2xl md:text-3xl font-extrabold text-white mb-6">A world transformed by\s*intelligent systems, built ethically and with purpose\.</h2>',
            r'<h2 class="text-2xl md:text-3xl font-extrabold text-white mb-6">A future where every critical enterprise decision is powered by intelligent, autonomous data science.</h2>',
            content
        )
        content = re.sub(
            r'To be the globally recognized vanguard\s*of artificial intelligence and data science, driving the next era of ethical digital\s*transformation across global markets\.',
            r'To be the vanguard of applied artificial intelligence, setting the definitive gold standard for scalable data analytics and autonomous systems that empower enterprises to thrive in a hyper-connected world.',
            content
        )
        content = re.sub(
            r'<strong class="text-white">Global Trust:</strong>\s*Setting the definitive gold standard for secure, reliable AI ecosystems\.',
            r'<strong class="text-white">Uncompromising Integrity:</strong> Ensuring all data models and AI deployments are transparent, ethical, and unbiased.',
            content
        )
        content = re.sub(
            r'<strong class="text-white">Ethical Scale:</strong>\s*Ensuring rapid technological advancements benefit humanity safely\.',
            r'<strong class="text-white">Exponential Scale:</strong> Democratizing access to enterprise-grade machine learning and analytical infrastructure.',
            content
        )

    with open(filepath, 'w') as f:
        f.write(content)

# Create services.html using capabilities.html as a base layout template
with open('/home/prateek/Vinoxies/capabilities.html', 'r') as f:
    services_content = f.read()

# Replace the specific section with our new services content
services_html = """
        <section id="services" class="py-24 px-6 max-w-7xl mx-auto">
            <div class="text-center mb-16 reveal">
                <span class="sbadge text-purple-400 bg-purple-950/50 border border-purple-500/30">Our Offerings</span>
                <h2 class="text-3xl md:text-5xl font-extrabold text-white mt-4 mb-4">Professional Services</h2>
                <p class="text-gray-400 max-w-2xl mx-auto text-sm md:text-base">Comprehensive AI and Data Science solutions tailored to transform raw data into a dominant competitive advantage.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 reveal stagger">
                <div class="glass spot p-8 rounded-3xl border border-white/10 hover:border-purple-500/50 transition-colors">
                    <div class="w-14 h-14 rounded-2xl bg-purple-500/20 text-purple-400 flex items-center justify-center mb-6"><i data-lucide="line-chart" class="w-7 h-7"></i></div>
                    <h3 class="text-xl font-bold text-white mb-3">Predictive Analytics</h3>
                    <p class="text-sm text-gray-400 mb-4">Leverage historical data to forecast trends, anticipate customer behavior, and optimize supply chains with unparalleled accuracy.</p>
                </div>
                <div class="glass spot p-8 rounded-3xl border border-white/10 hover:border-cyan-500/50 transition-colors">
                    <div class="w-14 h-14 rounded-2xl bg-cyan-500/20 text-cyan-400 flex items-center justify-center mb-6"><i data-lucide="bot" class="w-7 h-7"></i></div>
                    <h3 class="text-xl font-bold text-white mb-3">Generative AI Solutions</h3>
                    <p class="text-sm text-gray-400 mb-4">Custom LLMs, RAG architectures, and autonomous agentic workflows designed to automate complex cognitive tasks.</p>
                </div>
                <div class="glass spot p-8 rounded-3xl border border-white/10 hover:border-emerald-500/50 transition-colors">
                    <div class="w-14 h-14 rounded-2xl bg-emerald-500/20 text-emerald-400 flex items-center justify-center mb-6"><i data-lucide="database" class="w-7 h-7"></i></div>
                    <h3 class="text-xl font-bold text-white mb-3">Enterprise Data Engineering</h3>
                    <p class="text-sm text-gray-400 mb-4">Scalable data lakes, high-speed ETL/ELT pipelines, and real-time streaming architectures to power your AI models.</p>
                </div>
                <div class="glass spot p-8 rounded-3xl border border-white/10 hover:border-rose-500/50 transition-colors">
                    <div class="w-14 h-14 rounded-2xl bg-rose-500/20 text-rose-400 flex items-center justify-center mb-6"><i data-lucide="eye" class="w-7 h-7"></i></div>
                    <h3 class="text-xl font-bold text-white mb-3">Computer Vision & NLP</h3>
                    <p class="text-sm text-gray-400 mb-4">Extract deep meaning from unstructured data through advanced image recognition, video analytics, and natural language processing.</p>
                </div>
                <div class="glass spot p-8 rounded-3xl border border-white/10 hover:border-amber-500/50 transition-colors">
                    <div class="w-14 h-14 rounded-2xl bg-amber-500/20 text-amber-400 flex items-center justify-center mb-6"><i data-lucide="pie-chart" class="w-7 h-7"></i></div>
                    <h3 class="text-xl font-bold text-white mb-3">Business Intelligence</h3>
                    <p class="text-sm text-gray-400 mb-4">Interactive, highly visual dashboards and strategic data consulting to track KPIs and drive C-suite decision-making.</p>
                </div>
                <div class="glass spot p-8 rounded-3xl border border-white/10 hover:border-indigo-500/50 transition-colors">
                    <div class="w-14 h-14 rounded-2xl bg-indigo-500/20 text-indigo-400 flex items-center justify-center mb-6"><i data-lucide="cpu" class="w-7 h-7"></i></div>
                    <h3 class="text-xl font-bold text-white mb-3">MLOps & Deployment</h3>
                    <p class="text-sm text-gray-400 mb-4">End-to-end model lifecycle management, ensuring your algorithms are seamlessly integrated, monitored, and scaled in production.</p>
                </div>
            </div>
        </section>
"""

services_content = update_nav(services_content)
services_content = re.sub(r'<section id="capabilities".*?</section>', services_html, services_content, flags=re.DOTALL)
with open('/home/prateek/Vinoxies/services.html', 'w') as f:
    f.write(services_content)

print("Updates applied successfully.")
