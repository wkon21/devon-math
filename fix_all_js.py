import os

root_dir = r'c:\Users\wayne\.gemini\antigravity\scratch\devon-math'

for subdir, dirs, files in os.walk(root_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(subdir, file)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()

            content = content.replace(
                'document.head.appendChild(style);',
                '// document.head.appendChild(style); // disabled by UI redesign'
            )
            content = content.replace(
                'section.style.setProperty("--hue", "var(" + lesson.hueVar + "-solid)");',
                'section.style.setProperty("--hue", "var(" + lesson.hueVar + ")");'
            )
            content = content.replace(
                'card.style.setProperty("--hue", "var(" + lesson.hueVar + "-solid)");',
                'card.style.setProperty("--hue", "var(" + lesson.hueVar + ")");'
            )
            content = content.replace(
                'section.style.setProperty("--tint", "var(" + lesson.hueVar + "-tint)");',
                'section.style.setProperty("--tint", "var(--tint)");'
            )
            content = content.replace(
                'card.style.setProperty("--tint", "var(" + lesson.hueVar + "-tint)");',
                'card.style.setProperty("--tint", "var(--tint)");'
            )
            content = content.replace(
                'chip.style.setProperty("--chip-hue", "var(" + lesson.hueVar + "-solid)");',
                'chip.style.setProperty("--chip-hue", "var(" + lesson.hueVar + ")");'
            )
            content = content.replace(
                'chip.style.setProperty("--chip-tint", "var(" + lesson.hueVar + "-tint)");',
                'chip.style.setProperty("--chip-tint", "var(--tint)");'
            )

            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print('JS logic fixed for all HTML files.')
