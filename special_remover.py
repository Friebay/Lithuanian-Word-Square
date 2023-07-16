with open("wiki_lithuanianletters.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
 # Create a list to store the filtered lines
filtered_lines = []
 # Iterate over each line
for line in lines:
    # Check if the line contains any special characters
    if not any(char in line for char in ['.', ',', '-', "'", '`', '*']):
        # If no special characters found, add the line to the filtered list
        filtered_lines.append(line)
 # Open the file in write mode and overwrite its contents with the filtered lines
with open("wiki_lithuanianletters_no_special.txt", "w", encoding="utf-8") as file:
    file.writelines(filtered_lines)