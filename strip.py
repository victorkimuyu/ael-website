import sys

with open(sys.argv[1], 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip = False
for line in lines:
    if "/* ── Hero Slider Animations ── */" in line:
        skip = True
    
    if skip and "    </style>" in line:
        skip = False
        new_lines.append("    </style>\n")
        continue
        
    if "<section id=\"hero\"" in line:
        skip = True
        new_lines.append("""    <!-- ═══════════════════════════════════════════════════════════
         MAIN CONTENT (PLACEHOLDER)
         ═══════════════════════════════════════════════════════════ -->
    <main class="flex-grow flex items-center justify-center p-8 bg-slate-50 min-h-[50vh]">
        <div class="text-center">
            <h1 class="font-display font-bold text-4xl text-slate-900 mb-4">Contact Us</h1>
            <p class="text-slate-500 max-w-lg mx-auto leading-relaxed">Contact information and form will be placed here.</p>
        </div>
    </main>
""")
        continue
        
    if skip and "</main>" in line:
        skip = False
        continue
        
    if "// ─────────────────────────────────────" in line and "Hero Slider Controller" in line:
        skip = True
    
    if skip and "        })();" in line:
        skip = False
        # wait, the original file had "            })();" but let's just output the end closure:
        new_lines.append("            })();\n")
        continue

    if not skip:
        new_lines.append(line)

content = "".join(new_lines)

content = content.replace(
    '''                    <!-- Home -->
                    <a href="index.html"
                        class="relative px-4 py-2 text-sm  text-primary transition-colors duration-200 after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-6 after:h-0.5 after:bg-action after:rounded-full">
                        Home
                    </a>''',
    '''                    <!-- Home -->
                    <a href="index.html"
                        class="relative px-4 py-2 text-sm text-slate-600 hover:text-primary transition-colors duration-200">
                        Home
                    </a>'''
)

content = content.replace(
    '''                    <!-- Contact Us -->
                    <a href="contact_us.html"
                        class="px-4 py-2 text-sm  text-slate-600 hover:text-primary transition-colors duration-200">
                        Contact Us
                    </a>''',
    '''                    <!-- Contact Us -->
                    <a href="contact_us.html"
                        class="relative px-4 py-2 text-sm text-primary transition-colors duration-200 after:absolute after:bottom-0 after:left-1/2 after:-translate-x-1/2 after:w-6 after:h-0.5 after:bg-action after:rounded-full">
                        Contact Us
                    </a>'''
)

with open(sys.argv[1], 'w', encoding='utf-8') as f:
    f.write(content)
