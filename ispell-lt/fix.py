input_files = [
    "ispell-lt/lietuviu.ivairus",
    "ispell-lt/lietuviu.ivpk",
    "ispell-lt/lietuviu.jargon",
    "ispell-lt/lietuviu.vardai",
    "ispell-lt/lietuviu.veiksmazodziai",
    "ispell-lt/lietuviu.zodziai"
]
output_path = "ispell-lt/lietuviu_combined.txt"

with open(output_path, "w", encoding="utf-8") as dst:
    for input_path in input_files:
        with open(input_path, "r", encoding="windows-1257") as src:
            for line in src:
                line = line.split('/', 1)[0].replace('#', '')
                if line and len(line.split()) == 1:  # Only keep single-word lines
                    word = line.strip()  # Remove spaces before and after the word
                    if word:
                        dst.write(word + '\n')

print("All files converted, cleaned, and combined.")
