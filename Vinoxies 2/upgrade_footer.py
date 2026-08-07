import os
import glob
import re

directory = '/home/prateek/Vinoxies/'
html_files = glob.glob(os.path.join(directory, '*.html'))
html_files = [f for f in html_files if 'index-v' not in f and 'vionexis_intelligence_website' not in f]

new_footer = """<!-- FOOTER -->
    <footer class="border-t border-white/10 pt-24 pb-12 px-6 relative z-10 bg-gradient-to-b from-transparent to-black/80 backdrop-blur-xl">
        <div class="max-w-7xl mx-auto">
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 lg:gap-8 mb-20">
                
                <!-- Col 1: Brand & Social -->
                <div class="space-y-8">
                    <a href="index.html" class="flex flex-col text-left group inline-block">
                        <span class="text-2xl font-black tracking-widest text-white drop-shadow-md group-hover:text-cyan-400 transition-colors duration-500">VIONEXIS</span>
                        <span class="text-[11px] tracking-[0.3em] text-cyan-400 uppercase font-bold mt-1">Intelligence</span>
                    </a>
                    <p class="text-sm text-gray-400 font-light leading-relaxed max-w-sm">
                        Pioneering the intersection of applied research and enterprise engineering. We build secure, intelligent systems for the data-driven future.
                    </p>
                    <div class="flex items-center gap-4">
                        <a href="#" class="w-10 h-10 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 flex items-center justify-center text-gray-400 hover:text-cyan-400 transition-all hover:scale-110 hover:shadow-[0_0_15px_rgba(6,182,212,0.3)]" title="Twitter / X">
                            <i data-lucide="twitter" class="w-4 h-4"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 flex items-center justify-center text-gray-400 hover:text-cyan-400 transition-all hover:scale-110 hover:shadow-[0_0_15px_rgba(6,182,212,0.3)]" title="LinkedIn">
                            <i data-lucide="linkedin" class="w-4 h-4"></i>
                        </a>
                        <a href="#" class="w-10 h-10 rounded-xl bg-white/5 hover:bg-cyan-500/20 border border-white/10 flex items-center justify-center text-gray-400 hover:text-cyan-400 transition-all hover:scale-110 hover:shadow-[0_0_15px_rgba(6,182,212,0.3)]" title="GitHub">
                            <i data-lucide="github" class="w-4 h-4"></i>
                        </a>
                    </div>
                </div>

                <!-- Col 2: Navigation -->
                <div>
                    <h4 class="text-white font-bold text-base mb-6 uppercase tracking-wider flex items-center gap-2"><div class="w-2 h-2 rounded-full bg-purple-500"></div>Navigation</h4>
                    <ul class="space-y-4">
                        <li><a href="about.html" class="group flex items-center text-sm text-gray-400 hover:text-purple-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-purple-500 mr-0 group-hover:mr-2">▹</span>About Us</a></li>
                        <li><a href="services.html" class="group flex items-center text-sm text-gray-400 hover:text-purple-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-purple-500 mr-0 group-hover:mr-2">▹</span>Services</a></li>
                        <li><a href="capabilities.html" class="group flex items-center text-sm text-gray-400 hover:text-purple-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-purple-500 mr-0 group-hover:mr-2">▹</span>Core Capabilities</a></li>
                        <li><a href="advantage.html" class="group flex items-center text-sm text-gray-400 hover:text-purple-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-purple-500 mr-0 group-hover:mr-2">▹</span>The Advantage</a></li>
                        <li><a href="industries.html" class="group flex items-center text-sm text-gray-400 hover:text-purple-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-purple-500 mr-0 group-hover:mr-2">▹</span>Industries</a></li>
                    </ul>
                </div>

                <!-- Col 3: Company -->
                <div>
                    <h4 class="text-white font-bold text-base mb-6 uppercase tracking-wider flex items-center gap-2"><div class="w-2 h-2 rounded-full bg-emerald-500"></div>Company</h4>
                    <ul class="space-y-4">
                        <li><a href="team.html" class="group flex items-center text-sm text-gray-400 hover:text-emerald-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-emerald-500 mr-0 group-hover:mr-2">▹</span>Leadership Team</a></li>
                        <li><a href="careers.html" class="group flex items-center text-sm text-gray-400 hover:text-emerald-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-emerald-500 mr-0 group-hover:mr-2">▹</span>Careers (We're Hiring)</a></li>
                        <li><a href="contact.html" class="group flex items-center text-sm text-gray-400 hover:text-emerald-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-emerald-500 mr-0 group-hover:mr-2">▹</span>Contact Us</a></li>
                        <li><a href="#" class="group flex items-center text-sm text-gray-400 hover:text-emerald-400 transition-colors"><span class="w-0 group-hover:w-2 transition-all overflow-hidden text-emerald-500 mr-0 group-hover:mr-2">▹</span>Privacy Policy</a></li>
                    </ul>
                </div>

                <!-- Col 4: Newsletter -->
                <div>
                    <h4 class="text-white font-bold text-base mb-6 uppercase tracking-wider flex items-center gap-2"><div class="w-2 h-2 rounded-full bg-cyan-500"></div>Stay Updated</h4>
                    <p class="text-sm text-gray-400 font-light mb-6">Subscribe to our newsletter for the latest in AI research and enterprise engineering.</p>
                    <form class="relative group">
                        <div class="absolute -inset-0.5 bg-gradient-to-r from-purple-500 to-cyan-500 rounded-xl blur opacity-20 group-hover:opacity-50 transition duration-500"></div>
                        <input type="email" placeholder="Enter your business email" class="relative w-full px-5 py-4 rounded-xl bg-slate-900/90 border border-white/10 text-white placeholder-gray-500 text-sm focus:outline-none focus:border-cyan-400 transition-colors pr-12 shadow-inner">
                        <button type="button" class="absolute right-2 top-1/2 -translate-y-1/2 w-10 h-10 rounded-lg bg-gradient-to-br from-cyan-500 to-purple-500 text-white flex items-center justify-center hover:shadow-[0_0_15px_rgba(6,182,212,0.5)] transition-all hover:scale-105">
                            <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </button>
                    </form>
                </div>

            </div>

            <!-- Bottom Copyright -->
            <div class="border-t border-white/10 pt-8 flex flex-col md:flex-row items-center justify-between gap-6">
                <div class="flex items-center gap-3 text-xs text-gray-500">
                    <div class="w-1.5 h-1.5 rounded-full bg-cyan-500 pulse-dot"></div>
                    <span class="font-bold text-white tracking-widest uppercase">VIONEXIS INTELLIGENCE</span>
                    <span class="hidden md:inline text-gray-600">|</span>
                    <span class="hidden md:inline font-medium tracking-wide">Architecting the Data-Driven Future</span>
                </div>
                <div class="text-xs text-gray-500 font-medium tracking-wide">
                    © 2026 Vionexis Intelligence. All rights reserved.
                </div>
            </div>
        </div>
    </footer>"""

for filepath in html_files:
    with open(filepath, 'r') as f:
        content = f.read()
    
    content = re.sub(
        r'<!-- FOOTER -->\s*<footer.*?</footer>',
        new_footer,
        content,
        flags=re.DOTALL
    )

    with open(filepath, 'w') as f:
        f.write(content)

print("Footer upgraded successfully.")
