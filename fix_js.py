import os

files_to_fix = [
    r'04 Maths Extended/Unit 1 - Real Numbers and Radicals/Maths Extended U1 - Real Numbers and Radicals.html',
    r'04 Maths Extended/Unit 2 - Representing Relationships/Maths Extended U2 - Representing Relationships.html'
]

for filepath in files_to_fix:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Disable injectHueVars() from actually injecting anything
    content = content.replace(
        'document.head.appendChild(style);',
        '// document.head.appendChild(style); // disabled by UI redesign'
    )

    # 2. Fix the --hue assignment
    content = content.replace(
        'section.style.setProperty("--hue", "var(" + lesson.hueVar + "-solid)");',
        'section.style.setProperty("--hue", "var(" + lesson.hueVar + ")");'
    )
    content = content.replace(
        'card.style.setProperty("--hue", "var(" + lesson.hueVar + "-solid)");',
        'card.style.setProperty("--hue", "var(" + lesson.hueVar + ")");'
    )

    # 3. Fix the --tint assignment to use the global tint
    content = content.replace(
        'section.style.setProperty("--tint", "var(" + lesson.hueVar + "-tint)");',
        'section.style.setProperty("--tint", "var(--tint)");'
    )
    content = content.replace(
        'card.style.setProperty("--tint", "var(" + lesson.hueVar + "-tint)");',
        'card.style.setProperty("--tint", "var(--tint)");'
    )
    
    # 4. Fix chip hue
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

print('JS logic fixed.')
