filemame = "all"

# Save to file "w" = write mode
def save_words_in_column(filename, words):
    with open(filename, "w", encoding="utf-8") as file:
        for word in words:
            file.write(word + "\n")
            
            
def count_words(words):
    return len(words)

# Open the file "r" = read mode
with open(filemame + ".txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
    words = []
    
    for line in lines:
        line_words = line.strip().split()
        
        # Check if the line has words combined by underscores
        combined_words = []
        for word in line_words:
            if "/" in word:
                combined_words.extend(word.split("/"))
            else:
                combined_words.append(word)
        
        # Extend or append the individual words based on the number of words in the line
        if 2 <= len(combined_words) <= 10:
            words.extend(combined_words)
        else:
            words.append(line.strip())

            
words = [word.lower() for word in words]

unique_words = set()
non_repeating_words = []
repeating_words = []

for word in words:
    # Check if the word is not already in the set
    if word not in unique_words:
        # Add the word to the set and list
        unique_words.add(word)
        non_repeating_words.append(word)
    else:
        repeating_words.append(word)

 # Call the function to save words in a column format
save_words_in_column(filemame + "_cleaned.txt", non_repeating_words)

print(repeating_words[:10])
    
count = count_words(words)
cleaned_count = count_words(non_repeating_words)

print("Number of words in " + filemame + ".txt:", count)
print("Number of words in " + filemame + "_cleaned.txt:", cleaned_count)